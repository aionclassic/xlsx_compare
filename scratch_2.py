import pandas as pd
import time
import os

name_column = 'number'  # название столбца для пересечения

list_file = []
data_directory = '111'
for root, dirs, files in os.walk(data_directory):
    for filename in files:
        list_file.append(os.path.join(root, filename))

ii=0
for i in list_file:
    ii += 1
    globals()[f'df{ii}'] = pd.read_excel(i)
    globals()[f'set_data_df{ii}'] = set(eval(f'df{ii}[name_column]'))





print(set_data_df1 & set_data_df2 & set_data_df3 & set_data_df4)


