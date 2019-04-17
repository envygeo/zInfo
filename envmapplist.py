'''
Generate html index of Geomatics Unit map projects.

Matt Wilkie, 2017-12-05
Forked from envapplist.py by Jon Hourd

Search folder tree for known metadata file and parse it's contents into
html. Sample project.ini:

    [project]
    title = Map Index
    owner = Matt Wilkie
    client = Geomatics Unit
    branch = IMT
    date_initiated = 2009-02-26
'''
import os
import configparser
config = configparser.ConfigParser()

baseDir = r'\\ENVGEOSERVER\Maps'
idxFile = os.path.join(baseDir, 'Map-Project-Index.html')
metafile = 'project.ini'

htmlheader = """<HTML>
<body>
    <h1>ENV Geomatics Maps & Projects</h1>
    <p>&nbsp;</p>
    <table border="1" cellpadding="10">
"""
htmlfooter = """
    </table>
    <script type="text\javascript">
        function ClipBoard()
        {
            Copied = linktext.createTextRange();
            Copied.execCommand("Copy");
        }
    </script>
</body>
</HTML>"""

def main():
    appList = [['Title', 'Link (IE only)', 'Contact', 'Document Dir']]
    for envApp in  filter(lambda x: os.path.isdir(os.path.join(baseDir, x)), os.listdir(baseDir)):
        infoFile = os.path.join(baseDir, envApp, metafile)
        if os.path.isfile(infoFile):
            print(infoFile)
            d = read_ini(infoFile)
            #with open(infoFile) as f:
            #    lines = f.read().splitlines()
            #    title, link, contact = lines
            title = d['title']
            link = d['branch']
            contact = d['owner']


            # Check for Doc Directory
            print(title)
            if 'http' in link:
                fullLink = '<a href="{0}">{0}</a>'.format(link)
            else:
                winPath = '{0}{1}/{2}'.format(baseDir, envApp, link).replace('/', '\\')
                fullLink = '<a href="file:///{0}{1}/{2}">'.format(baseDir, envApp, link.replace('\\', '/'))
                fullLink += winPath
                fullLink += '</a>'
            print(link)
            print(contact)
            if 'gov.yk.ca' not in contact:
                contactLink = '<a href="mailto:env-gis-unit@gov.yk.ca?Subject=ENV-Map-ID: {1}" target="_top">{0}</a>'.format(contact, title)
            else:
                contactLink = '<a href="mailto:{0}?Subject={1}" target="_top">{0}</a>'.format(contact, title)
            docDir = baseDir + envApp + '/Doc'
            if os.path.isdir(docDir):
                print(docDir)
            #docLink = '<a href="file:///{}">{}</a>'.format(docDir, docDir.replace('/','\\'))
            docLink = '<a href="file:///{}">{}</a>'.format(infoFile, infoFile)
            appList.append([title, fullLink, contactLink, docLink if os.path.isdir(docDir) else ''])

    tr = "<tr>{0}</tr>"
    td = "<td>{0}</td>"
    apps = [tr.format('\n'.join([td.format(a) for a in app])) for app in appList]
    output = htmlheader;
    output += ''.join(apps);
    output += htmlfooter;
    return output

def read_ini(fname):
    '''parse ini into dictionary'''
    config.read(fname)
    print(config.sections())
    for k in config['project']:
        print(k)
    return config['project']



def write(data, fname):
    with open(fname, 'w') as w:
        w.write(data)

if __name__ == '__main__':
    html = main()
    write(html, idxFile)

