import os
import pandas as pd

csv_file = pd.read_csv('TB_List.csv')
num=0
i=0
path = "D:/AI_Data/Raw_Data/2_TB/"
for f in os.listdir(path):
    if f == csv_file['Image File'][i]:
        #print("File OK",num+1)
        num+=1
        i+=1

print("Found ",num )