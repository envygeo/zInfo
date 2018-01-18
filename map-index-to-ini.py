'''Stub: Read the Map-Index spreadsheet and save into project .ini files
in the relevant folders.
'''
import os
import configparser
config = configparser.ConfigParser()

base_dir = r'\\ENVGEOSERVER\Maps'
metafile = 'project.ini'
xls_path = 'Index\Map-Index.xlsx'

