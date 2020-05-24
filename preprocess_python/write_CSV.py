import pandas as pd
import os

csv_file = pd.read_csv('TB_List.csv')
num=0
path = "2_TB/"
for name in os.listdir(path):
    src = path+name
    filename = "TB_"+str(num+1)+".png"
    dst = path+filename
    csv_file['Image File'][num] = filename
    os.rename(src,dst)
    print("Rename OK",num+1)
    num+=1
csv_file = csv_file.drop(columns='Unnamed: 0')
#csv_file = csv_file.drop(columns='index')
csv_file.to_csv('new_tb_list.csv')