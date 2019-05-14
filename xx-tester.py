import os
import glob
import inspect
import configparser
config = configparser.ConfigParser()

INI = 'project.ini' # name of metadata file indicating a project folder


def get_script_dir():
    """Return folder of this running script's location"""
    # thanks @Jose, https://stackoverflow.com/a/44592299/14420
    ourscript = inspect.getframeinfo(inspect.currentframe()).filename
    dir = os.path.dirname(os.path.abspath(ourscript))
    return dir

baseDir = os.path.join(get_script_dir(), 'test\\in')

dirFile = os.path.join(baseDir, 'test\\out', 'Map-Project-Index.html')


def find_metafiles(target, ini):
    '''Return list of project metadata files under target'''
    return glob.glob(f'{baseDir}/**/{INI}', recursive=True)

def metablock_to_html(metablock):
    '''convert a project metadata block to html fragment'''

    return html

def parse_ini(filename):
    '''return dictionary of the Project in this ini'''
    print(filename)
    config.read(filename)
    section = 'project' # Heading that denotes a Project metadata block
    project_dict = {}
    if section in config.sections():
        fields = config.options(section)
        for f in fields:
            v = config.get(section, f)
            print('{:>20}: {}'.format(f, v))
            project_dict[f]=v
    return project_dict

def write(data, fname):
    with open(fname, 'w') as w:
        w.write(data)


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

def dict2html(dictionary):
    for d in dictionary:
        html = f'<h2>{d}</h2>'
        for i in dictionary[d]:
            html += f'<li>{i}</li>'
    return html


if __name__ == "__main__":
    #print(baseDir)
    metafiles = find_metafiles(baseDir, INI)
    #print(metafiles)
    projects_d = {}
    projects_d[metafiles[0]] = [parse_ini(f) for f in metafiles]
    html = dict2html(projects_d)



