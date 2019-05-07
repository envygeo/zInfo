import os
import glob
import inspect
import configparser
config = configparser.ConfigParser()

def get_script_dir():
    """Return folder of this running script's location"""
    # thanks @Jose, https://stackoverflow.com/a/44592299/14420
    ourscript = inspect.getframeinfo(inspect.currentframe()).filename
    dir = os.path.dirname(os.path.abspath(ourscript))
    return dir

baseDir = os.path.join(get_script_dir(), 'test/in')

dirFile = os.path.join(baseDir, 'test/out', 'Map-Project-Index.html')
metafile = 'project.ini'

def find_metafiles(target, ini):
    '''Return list of project.ini files under target'''
    return filename in glob.glob(os.path.join(target, ini) , recursive=True)


def main():
    folders = ['Index']
    section = 'project'
    for d in folders:
        location = os.path.join(baseDir, d)
        print(location)
        config.read(os.path.join(location, metafile))
        if section in config.sections():
            fields = config.options(section)
            for f in fields:
                v = config.get(section, f)
                print('{:>20}: {}'.format(f, v))


if __name__ == "__main__":
    #ROOT = get_script_dir()
    #print(ROOT)
    main()

