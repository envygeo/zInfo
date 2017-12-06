import os
import configparser
config = configparser.ConfigParser()

baseDir = r'\\ENVGEOSERVER\Maps'
dirFile = os.path.join(baseDir, 'Map-Project-Index.html')
metafile = 'project.ini'

folders = ['Index']
for d in folders:
    location = os.path.join(baseDir, d)
    print(location)
    config.read(os.path.join(location, metafile))
    if 'project' in config.sections():
        for key in config['project']: print(key)
    

