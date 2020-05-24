import pandas as pd
import os,shutil

PATH = "D:/AI_Data/3000+123/balnace_set/"
SUB = ['CA Lung/','Extra/','Heart/','Intra/','No Finding/','Pneumonia/','TB/']
FOLDER = ['CA','Extra','Heart','Intra','NoF','Peno','TB']
LABEL = ['Is_CA','Is_Extra','Is_Heart','Is_Intra','Is_NoF','Is_Pneumonia','Is_TB']

for i in range(0,7):
    num = 0
    csv = pd.DataFrame(columns=['Image File',LABEL[i]])
    for f in sorted(os.listdir(PATH+SUB[i]+'train/')):
        name = f.split('_')[0]
        if name == FOLDER[i]:
            csv.loc[num] = [f,'1']
            print(num+1,'train/ Yes')
        else:
            csv.loc[num] = [f,'0']
            print(num+1,'train/ No')
        num+=1
    for f in sorted(os.listdir(PATH+SUB[i]+'test/')):
        name = f.split('_')[0]
        if name == FOLDER[i]:
            csv.loc[num] = [f,'1']
            print(num+1,'test/ Yes')
        else:
            csv.loc[num] = [f,'0']
            print(num+1,'test/ No')
        num+=1
    for f in sorted(os.listdir(PATH+SUB[i]+'valid/')):
        name = f.split('_')[0]
        if name == FOLDER[i]:
            csv.loc[num] = [f,'1']
            print(num+1,'valid/ Yes')
        else:
            csv.loc[num] = [f,'0']
            print(num+1,'valid/ No')
        num+=1
    csv.to_csv("balance_"+FOLDER[i]+"_class.csv")
