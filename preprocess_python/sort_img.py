import pandas as pd
import shutil, os
csv_file = pd.read_csv('TB_List.csv')
path = "D:/AI_Data/ChestXray-NIHCC/Every Pic/images/"
new_path = "D:/AI_Data/Raw_Data/2_TB/"
i=0
j=0
dt_len = csv_file['Image File'].size
for f in os.listdir(path):
    if f == csv_file['Image File'][j] :
        print("Found",j+1,"pic")
        full_f = path+ f
        shutil.copy(full_f,new_path)
        j+=1
        i=0
    i+=1