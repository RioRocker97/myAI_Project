import pandas as pd

old_csv = pd.read_csv('Raw_Data_100.csv')

for i in range(0,old_csv['Image File'].size):
    old = old_csv['Image File'][i].split('.')[0]
    new = old+'.jpg'
    #old_path = old_csv['full_path'][i].split('.')[0]
    #new_path = old_path+'.jpg'
    old_csv['Image File'][i] = new
    #old_csv['full_path'][i] = new_path
    #old_path = old_csv['full_path'][i]
    #new_path = '../'+old_path
    #old_csv['full_path'][i] = new_path

new_csv = old_csv.drop(columns='Unnamed: 0')
new_csv.to_csv('Raw_Data_JPG_100.csv')
print(new_csv)