import pandas as pd
import os,shutil
PATH = "D:/AI_Data/3000+123/"
SUB_PATH = ['CA Lung/','Extra/','Heart/','Intra/','No Finding/','Pneumonia/','TB/']
SUB_Folder = ['train/','test/','valid/']
LABEL = ['CA','Extra','Heart','Intra','No Finding','Pneumonia','TB']
BASE = pd.DataFrame(columns=["Image File","Finding Label"])
num =0

for i in range(0,7):
    for f in os.listdir(PATH+SUB_PATH[i]+"train/"):
        BASE.loc[num] = [f,LABEL[i]]
        print(LABEL[i],"train",num)
        num+=1
    for f in os.listdir(PATH+SUB_PATH[i]+"test/"):
        BASE.loc[num] = [f,LABEL[i]]
        print(LABEL[i],"test",num)
        num+=1
    for f in os.listdir(PATH+SUB_PATH[i]+"valid/"):
        BASE.loc[num] = [f,LABEL[i]]
        print(LABEL[i],"valid",num)
        num+=1


print(BASE)
BASE.to_csv('19200_CSV_7_Classes.csv')