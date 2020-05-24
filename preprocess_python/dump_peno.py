import pandas as pd
import shutil, os
from PIL import Image

PATH = "D:/AI_Data/chest_xray/train/PNEUMONIA/"
NEW_PATH = "D:/AI_Data/peno_dump/"
NEW_NAME = "Peno_new_"
n=1
my_json = pd.read_json("pneumonia-challenge-annotations-original_2018.json")
print(my_json.describe())
#for i in os.listdir(PATH):
#    if n <= 1098 :
#        img = Image.open(PATH+i).resize((224,224),Image.ANTIALIAS)
#        name = NEW_PATH+NEW_NAME+str(n)+'.jpg'
#        img.save(name,'JPEG',quality=100)
#        print("Peno OK",str(n))
#        n+=1

