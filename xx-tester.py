import os
import configparser
config = configparser.ConfigParser()

baseDir = r'\\ENVGEOSERVER\Maps'
dirFile = os.path.join(baseDir, 'Map-Project-Index.html')
metafile = 'project.ini'

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
            
    

