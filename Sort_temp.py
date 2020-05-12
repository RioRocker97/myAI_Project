import os,shutil
import pandas as pd

MODE = 0
PATH = "/home/changsmarter/Desktop/myAI_Project/7classes_data/"
c = ['10000_NoF_Class.csv',]
CLASS = pd.read_csv("7classes_data/10000_NoF_Class.csv")
LABEL = "Is No_Finding"
start = 0
num = 0
train_limit = 1250
test_limit = 156
valid_limit = 156
for i in range(0,10000):
    if CLASS[LABEL][i] == 'Yes':
        if num==0:
            start = i
        num+=1
        
stop = start+num
num = 0

for i in range(start,start+train_limit):
    for f in sorted(os.listdir(PATH+'train/')):
        if f == CLASS['Image File'][i] :
            num+=1
            print(i,"train/ found yes",num)
            shutil.copy(PATH+'train/'+f,PATH+'temp/train/Yes')
            break
for i in range(start+train_limit,stop-valid_limit):
    for f in sorted(os.listdir(PATH+'test/')):
        if f == CLASS['Image File'][i] :
            num+=1
            print(i,"test/ found yes",num)
            shutil.copy(PATH+'test/'+f,PATH+'temp/test/Yes')
            break
for i in range(stop-valid_limit,stop):
    for f in sorted(os.listdir(PATH+'valid/')):
        if f == CLASS['Image File'][i] :
            num+=1
            print(i,"valid/ found yes",num)
            shutil.copy(PATH+'valid/'+f,PATH+'temp/valid/Yes')
            break
num=0
for i in range(0,start):
    for f in sorted(os.listdir(PATH+'train/')):
        if f == CLASS['Image File'][i]:
            num+=1
            print(i,"train/ found no",num)
            shutil.copy(PATH+'train/'+f,PATH+'temp/train/No')
            break
    for f in sorted(os.listdir(PATH+'test/')):
        if f == CLASS['Image File'][i]:
            num+=1
            print(i,"test/ found no",num)
            shutil.copy(PATH+'test/'+f,PATH+'temp/test/No')
            break
    for f in sorted(os.listdir(PATH+'valid/')):
        if f == CLASS['Image File'][i]:
            num+=1
            print(i,"valid/ found no",num)
            shutil.copy(PATH+'valid/'+f,PATH+'temp/valid/No')
            break
            
if stop == 10000:
    stop = 9999
    
for i in range(stop,10000):
    for f in sorted(os.listdir(PATH+'train/')):
        if f == CLASS['Image File'][i]:
            num+=1
            print(i,"train/ found no",num)
            shutil.copy(PATH+'train/'+f,PATH+'temp/train/No')
            break
    for f in sorted(os.listdir(PATH+'test/')):
        if f == CLASS['Image File'][i]:
            num+=1
            print(i,"test/ found no",num)
            shutil.copy(PATH+'test/'+f,PATH+'temp/test/No')
            break
    for f in sorted(os.listdir(PATH+'valid/')):
        if f == CLASS['Image File'][i]:
            num+=1
            print(i,"valid/ found no",num)
            shutil.copy(PATH+'valid/'+f,PATH+'temp/valid/No')
            break