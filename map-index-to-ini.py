'''Stub: Read the Map-Index spreadsheet and save into project .ini files
in the relevant folders.
'''
import os
import configparser
import pandas as pd

config = configparser.ConfigParser()

base_dir = r'\\ENVGEOSERVER\Maps'
metafile = 'zinfo.ini'
xls_path = 'Index\Map-Index.xlsx'

def thank_you():
    print('''Thank you to:
    @waitingkuo - https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
    ''')

def main():
    xls = pd.ExcelFile(os.path.join(base_dir, xls_path))
    df = xls.parse(sheet_name='Sheet1')
    
    old_headings = ['Job Name', 'Old Map ID', 'New Map ID', 'Series ID', 'Link','Description', 'Client']
    new_headings = ['Title', 'Old_ID', 'Map_ID', 'Series_ID', 'Link', 'Description','Contact']
    
    config['Project'] = {}
    for index, row in df.iterrows():
        if index < 20:
            project = config['Project']
            column = 0
            for nh in new_headings:
                project[nh] = '{}'.format(row[column])
                column = column +1
    
            for k in project:
                print('"{}": {}'.format(k,project[k]))

    
    
if __name__ == "__main__":
    main()    