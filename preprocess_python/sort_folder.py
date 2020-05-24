import os,shutil
import pandas as pd

MODE = 0
PATH = "D:/AI_Data/3000+123/10000_Real/"
c = '10000_NoF_Class.csv'
CLASS = pd.read_csv(c)
LABEL = "Is No_Finding"
folder = "NoF/"
start = 0
num = 0
train_limit = 500
test_limit = 62
valid_limit = 62
for i in range(0,10000):
    if CLASS[LABEL][i] == 'Yes':
        if num==0:
            start = i
        num+=1
        
stop = start+num
num = 0
print(start)
print(stop)

#for i in range(start,start+train_limit):
    #for f in sorted(os.listdir(PATH+'train/')):
    #    if f == CLASS['Image File'][i] :
    #        num+=1
    #        print(i,"train/ found yes",num)
    #        shutil.copy(PATH+'train/'+f,PATH+folder+'train/Yes')
    #        break
for i in range(start+train_limit,stop-valid_limit):
    for f in sorted(os.listdir(PATH+'test/')):
        if f == CLASS['Image File'][i] :
            num+=1
            print(i,"test/ found yes",num)
            shutil.copy(PATH+'test/'+f,PATH+folder+'test/Yes')
            break
#for i in range(stop-valid_limit,stop):
    #for f in sorted(os.listdir(PATH+'valid/')):
    #    if f == CLASS['Image File'][i] :
    #        num+=1
    #        print(i,"valid/ found yes",num)
    #        shutil.copy(PATH+'valid/'+f,PATH+folder+'valid/Yes')
    #        break
num=0
for i in range(0,start):
    #for f in sorted(os.listdir(PATH+'train/')):
    #    if f == CLASS['Image File'][i]:
    #        num+=1
    #        print(i,"train/ found no",num)
    #        shutil.copy(PATH+'train/'+f,PATH+folder+'train/No')
    #        break
    for f in sorted(os.listdir(PATH+'test/')):
        if f == CLASS['Image File'][i]:
            num+=1
            print(i,"test/ found no",num)
            shutil.copy(PATH+'test/'+f,PATH+folder+'test/No')
            break
    #for f in sorted(os.listdir(PATH+'valid/')):
    #   if f == CLASS['Image File'][i]:
    #        num+=1
    #        print(i,"valid/ found no",num)
    #        shutil.copy(PATH+'valid/'+f,PATH+folder+'valid/No')
    #        break
            
if stop == 10000:
    stop = 9999
    
for i in range(stop,10000):
    #for f in sorted(os.listdir(PATH+'train/')):
    #    if f == CLASS['Image File'][i]:
    #        num+=1
    #        print(i,"train/ found no",num)
    #        shutil.copy(PATH+'train/'+f,PATH+folder+'train/No')
    #        break
    for f in sorted(os.listdir(PATH+'test/')):
        if f == CLASS['Image File'][i]:
            num+=1
            print(i,"test/ found no",num)
            shutil.copy(PATH+'test/'+f,PATH+folder+'test/No')
            break
    #for f in sorted(os.listdir(PATH+'valid/')):
    #    if f == CLASS['Image File'][i]:
    #        num+=1
    #        print(i,"valid/ found no",num)
    #        shutil.copy(PATH+'valid/'+f,PATH+folder+'valid/No')
    #        break
