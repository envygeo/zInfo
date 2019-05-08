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

def parse_ini(filename):
    print(filename)
    config.read(filename)
    section = 'project' # Heading that denotes a Project metadata block
    if section in config.sections():
        fields = config.options(section)
        for f in fields:
            v = config.get(section, f)
            print('{:>20}: {}'.format(f, v))



if __name__ == "__main__":
    #print(baseDir)
    metafiles = find_metafiles(baseDir, INI)
    #print(metafiles)

    [parse_ini(f) for f in metafiles]



