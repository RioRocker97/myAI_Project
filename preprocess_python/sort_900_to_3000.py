import pandas as pd
import shutil, os
from PIL import Image
import numpy as np
from skimage import exposure

new_name = ['Peno_'] #z
folder = ['peno/'] #y
csv = ['4000_peno.csv'] #x
dest_path = "D:/AI_Data/serious/"
path = "D:/AI_Data/ChestXray-NIHCC/Every Pic/images/"

def increase_image(img,fname):
    n=1
    for i in range(1,5):
        a = img.rotate(i)
        extend = fname+"_ext"+str(n)+".jpg"
        a.save(extend,'JPEG',quality=100)
        print("Extend",str(n))
        n+=1
    for j in range(357,360):
        a = img.rotate(j)
        extend = fname+"_ext"+str(n)+".jpg"
        a.save(extend,'JPEG',quality=100)
        print("Extend",str(n))
        n+=1
def preprocess_image(image,size):
    img = image.resize((size,size),Image.ANTIALIAS).convert('L')
    construct = np.full((size,size,3),0,dtype=np.uint8)

    np_img = np.array(img)
    np_img_2 = exposure.equalize_hist(np_img) 
    np_img_3 = exposure.equalize_adapthist(np_img)

    np_img = (255.0 / np_img.max() * (np_img - np_img.min())).astype(np.uint8)
    np_img_2 = (255.0 / np_img_2.max() * (np_img_2 - np_img_2.min())).astype(np.uint8)
    np_img_3 = (255.0 / np_img_3.max() * (np_img_3 - np_img_3.min())).astype(np.uint8)
    for i in range(0,size):
        for j in  range(0,size):
            construct[i][j][0] = np_img[i][j]
            construct[i][j][1] = np_img_2[i][j]
            construct[i][j][2] = np_img_3[i][j]
    construct = (255.0 / construct.max() * (construct - construct.min())).astype(np.uint8)
    new_img = Image.fromarray(construct)
    return new_img

def sort_image(x,y,z):
    csv_file = pd.read_csv(x)

    SIZE = 224
    train_limit = 500
    valid_limit = 250
    test_limit = 0
    size = 900
    num=0

    for f in os.listdir(path):
        if size > train_limit :
            dest_p= dest_path+y+'train/'
            if f == csv_file['Image File'][num] :
                full_f = path+ f
                shutil.copy(full_f,dest_p)
                old_img = Image.open(dest_p+f)
                new_img = preprocess_image(old_img,SIZE)
                EXT = dest_p+z+str(num+1)
                URL = dest_p+z+str(num+1)+'.jpg'
                new_img.save(URL,'JPEG',quality=100)
                os.remove(dest_p+f)
                print(y,"Ok train/",num+1,"pic")
                increase_image(new_img,EXT)
                size-=1
                num+=1
        elif size > valid_limit :
            dest_p= dest_path+y+'valid/'
            if f == csv_file['Image File'][num] :
                full_f = path+ f
                shutil.copy(full_f,dest_p)
                old_img = Image.open(dest_p+f)
                new_img = preprocess_image(old_img,SIZE)
                URL = dest_p+z+str(num+1)+'.jpg'
                new_img.save(URL,'JPEG',quality=100)
                os.remove(dest_p+f)
                print(y,"Ok valid/",num+1,"pic")
                size-=1
                num+=1
        elif size > test_limit :
            dest_p= dest_path+y+'test/'
            if f == csv_file['Image File'][num] :
                full_f = path+ f
                shutil.copy(full_f,dest_p)
                old_img = Image.open(dest_p+f)
                new_img = preprocess_image(old_img,SIZE)
                URL = dest_p+z+str(num+1)+'.jpg'
                new_img.save(URL,'JPEG',quality=100)
                os.remove(dest_p+f)
                print(y,"Ok test/",num+1,"pic")
                size-=1
                num+=1

for i in range(0,1):
    sort_image(csv[i],folder[i],new_name[i])