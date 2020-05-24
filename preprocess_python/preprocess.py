from PIL import Image
import shutil,os
import numpy as np 
from skimage import exposure
from tensorflow.keras.applications.densenet import preprocess_input
def preprocess(image):

    size = 224
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

def predictImage(image):
    x = preprocess_input(image)