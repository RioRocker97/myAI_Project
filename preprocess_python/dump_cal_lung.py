import pandas as pd
import shutil, os
from PIL import Image

PATH = "D:/AI_Data/zipthis/"
NEW_PATH = "D:/AI_Data/ca_lung_dump/"
NEW_NAME = "CA_new_"
n=0
j=0
for i in os.listdir(PATH+'train/Cardiomegaly/'):
    n+=1
    j+=1
    if j <= 550 :
        img = Image.open(PATH+i).resize((224,224),Image.ANTIALIAS).convert("RGB")
        name = NEW_PATH+NEW_NAME+str(n)+'.jpg'
        img.save(name,'JPEG',quality=100)
        print("Train OK",str(n))

for i in os.listdir(PATH+'test/Cardiomegaly/'):
    img = Image.open(PATH+i).resize((224,224),Image.ANTIALIAS).convert("RGB")
    name = NEW_PATH+NEW_NAME+str(n)+'.jpg'
    img.save(name,'JPEG',quality=100)
    print("Test OK",str(n))
    n+=1

for i in os.listdir(PATH+'valid/Cardiomegaly/'):
    img = Image.open(PATH+i).resize((224,224),Image.ANTIALIAS).convert("RGB")
    name = NEW_PATH+NEW_NAME+str(n)+'.jpg'
    img.save(name,'JPEG',quality=100)
    print("Valid OK",str(n))
    n+=1
PATH = "D:/AI_Data/chest_xray/train/PNEUMONIA/"
for i in os.listdir(PATH):
    img = Image.open(PATH+i).resize((224,224),Image.ANTIALIAS).convert("RGB")
    name = NEW_PATH+NEW_NAME+str(n)+'.jpg'
    img.save(name,'JPEG',quality=100)
    print("xray OK",str(n))
    n+=1