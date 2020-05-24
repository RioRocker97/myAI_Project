import pandas as pd
import shutil, os
from PIL import Image

new_name = ['TB_','CA_','Heart_','Intra_','Extra_'] #z
folder = ['TB/','CA Lung/','Heart/','Intra/','Extra/'] #y
csv = ['4500_tb.csv','4500_ca_lung.csv','4500_heart.csv','4500_intra.csv','148_extra.csv'] #x

def sort_image(x,y,z,num):
    csv_file = pd.read_csv(x)
    dest_path = "D:/AI_Data/4500+148/data/"
    path = "D:/AI_Data/ChestXray-NIHCC/Every Pic/images/"
    dest_path= dest_path+y
    limit = 4500
    if num == 4:
        limit = 148
        
    for f in os.listdir(path):
        if num < limit :
            if f == csv_file['Image File'][num] :
                full_f = path+ f
                shutil.copy(full_f,dest_path)
                old_img = Image.open(dest_path+f)
                new_img = old_img.resize((224,224))
                new_img = new_img.convert('RGB')
                url = dest_path+z+str(num+1)+'.jpg'
                new_img.save(url,'JPEG',quality=100)
                os.remove(dest_path+f)
                print(y,"Ok",num+1,"pic")
                num+=1

for i in range(0,5):
    j=0
    sort_image(csv[i],folder[i],new_name[i],j)