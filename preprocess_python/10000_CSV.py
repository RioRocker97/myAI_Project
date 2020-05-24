import pandas as pd
import os,shutil
PATH = "D:/AI_Data/3000+123/"
SUB_PATH = ['CA Lung/','Heart/','Intra/','No Finding/','Pneumonia/','TB/','Extra/']
LABEL = ['CA','Heart','Intra','No Finding','Pneumonia','TB','Extra']
BASE = pd.DataFrame(columns=["Image File","Finding Label"])
num =0
for i in range(0,7):
    train = 1250
    test = 156
    valid = 156
    if(i==6):
        train = 500
        test = 62
        valid = 62
    elif(i==4 or i==5):
        test = 157
        valid = 157

    j=0
    for f in os.listdir(PATH+SUB_PATH[i]+"train/"):
        if(j<train):
            fname = PATH+SUB_PATH[i]+'train/'+f
            shutil.copy(fname,PATH+'Real/train/')
            BASE.loc[num] = [f,LABEL[i]]
            print(LABEL[i],"train",num)
            num+=1
            j+=1
    j=0
    for f in os.listdir(PATH+SUB_PATH[i]+"test/"):
        if(j<test):
            fname = PATH+SUB_PATH[i]+'test/'+f
            shutil.copy(fname,PATH+'Real/test/')
            BASE.loc[num] = [f,LABEL[i]]
            print(LABEL[i],"test",num)
            num+=1
            j+=1
    j=0
    for f in os.listdir(PATH+SUB_PATH[i]+"valid/"):
        if(j<valid):
            fname = PATH+SUB_PATH[i]+'valid/'+f
            shutil.copy(fname,PATH+'Real/valid/')
            BASE.loc[num] = [f,LABEL[i]]
            print(LABEL[i],"valid",num)
            num+=1
            j+=1


print(BASE)
BASE.to_csv('10000_CSV_7_Classes.csv')