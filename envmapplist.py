'''
Generate html index of Geomatics Unit map projects.

Matt Wilkie, 2017-12-05
Forked from envapplist.py by Jon Hourd
'''
import os
import configparser
config = configparser.ConfigParser()

baseDir = r'\\ENVGEOSERVER\Maps'
dirFile = os.path.join(baseDir, 'Map-Project-Index.html')
metafile = 'project.ini'

htmlheader = """<HTML>
<body>
    <h1>Environment System List</h1>
    <h2>"setup.bat" links will only work using Internet Explorer.</h2>
    For Firefox or Chrome:<br>
    1. Copy the link<br>
    2. Press "Windows Key" + "R"<br>
    3. Paste link and click "OK"<br>
    <br>
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

appList = [['Title', 'Link (IE only)', 'Contact', 'Document Dir']]
for envApp in  filter(lambda x: os.path.isdir(os.path.join(baseDir, x)), os.listdir(baseDir)):
    infoFile = baseDir + envApp + metafile
    if os.path.isfile(infoFile):
        print(infoFile)
        with open(infoFile) as f:
            lines = f.read().splitlines()
            title, link, contact = lines
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
            contactLink = '<a href="mailto:service.desk@gov.yk.ca?Subject=Environment Application: {1}" target="_top">{0}</a>'.format(contact, title)
        else:
            contactLink = '<a href="mailto:{0}?Subject={1}" target="_top">{0}</a>'.format(contact, title)
        docDir = baseDir + envApp + '/Doc'
        if os.path.isdir(docDir):
            print(docDir)
        docLink = '<a href="file:///{}">{}</a>'.format(docDir, docDir.replace('/','\\'))
        appList.append([title, fullLink, contactLink, docLink if os.path.isdir(docDir) else ''])
        
tr = "<tr>{0}</tr>"
td = "<td>{0}</td>"
apps = [tr.format('\n'.join([td.format(a) for a in app])) for app in appList]
output = htmlheader;
output += ''.join(apps);
output += htmlfooter;
print(output)
with open(dirFile, 'w') as w:
    w.write(output)
