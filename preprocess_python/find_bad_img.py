import pandas as pd
from PIL import Image
import shutil,os
import numpy as np 
import matplotlib.pyplot as plt
from skimage import exposure
PATH = "D:/AI_Data/ChestXray-NIHCC/Every Pic/images"

def getBadImgName():
    n=0
    for i in os.listdir(PATH):
        img = Image.open(PATH+'/'+i).resize((256,256)).convert('RGB')
        np_img = np.array(img)
        img.show()
        print(np_img)

img = Image.open(PATH+"/00000005_003.png").resize((256,256),Image.ANTIALIAS).convert('L')
construct = np.full((256,256,3),0,dtype=np.uint8)

np_img = np.array(img)
np_img_2 = exposure.equalize_hist(np_img) 
np_img_3 = exposure.equalize_adapthist(np_img)

np_img = (255.0 / np_img.max() * (np_img - np_img.min())).astype(np.uint8)
np_img_2 = (255.0 / np_img_2.max() * (np_img_2 - np_img_2.min())).astype(np.uint8)
np_img_3 = (255.0 / np_img_3.max() * (np_img_3 - np_img_3.min())).astype(np.uint8)
for i in range(0,256):
    for j in  range(0,256):
        construct[i][j][0] = np_img[i][j]
        construct[i][j][1] = np_img_2[i][j]
        construct[i][j][2] = np_img_3[i][j]

plt.figure(figsize=(15,15))
plt.subplot(1,4,1)
plt.title("B/W")
plt.imshow(np_img)
plt.subplot(1,4,2)
plt.title("Histrogram Eq.")
plt.imshow(np_img_2)
plt.subplot(1,4,3)
plt.title("CLAHE")
plt.imshow(np_img_3)
plt.subplot(1,4,4)
plt.title("All in one")
plt.imshow(construct)
plt.savefig('preprocess.jpg')
plt.show()

construct = (255.0 / construct.max() * (construct - construct.min())).astype(np.uint8)
new_img = Image.fromarray(construct)
#new_img.show()
#new_img.convert('RGB')
new_img.save('all in one2.jpg','JPEG',quality=100)