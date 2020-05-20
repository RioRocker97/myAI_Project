from PIL import Image
import numpy as np 
from skimage import exposure
from tensorflow.keras.applications.densenet import preprocess_input
from tensorflow.keras.models import load_model

model1 = load_model('FinalModel/CA_final_Den169.h5')
model2 = load_model('FinalModel/EXT_final_Den169.h5')
model3 = load_model('FinalModel/HEART_final_Den169.h5')
model4 = load_model('FinalModel/INT_final_Den169.h5')
model5 = load_model('FinalModel/NOF_final_Den169.h5')
model6 = load_model('FinalModel/PENO_final_Den169.h5')
model7 = load_model('FinalModel/TB_final_Den169.h5')

def predictImage(image):
    size = 224
    img = image.resize((size,size),Image.ANTIALIAS).convert('L')
    construct = np.full((size,size,3),0,dtype=np.uint8)
    
    np_img = np.array(img)
    np_img_2 = exposure.equalize_hist(np_img) 
    np_img_3 = exposure.equalize_adapthist(np_img)
   
    for i in range(0,size):
        for j in range(0,size):
            construct[i][j][0] = np_img[i][j]
            construct[i][j][1] = np_img_2[i][j]
            construct[i][j][2] = np_img_3[i][j]

    x_pred = preprocess_input(construct)
    x_pred = np.expand_dims(x_pred, axis=0)
    print(x_pred.shape)
    y_pred = np.array([
        np.max(model1.predict(x_pred)),
        np.max(model2.predict(x_pred)),
        np.max(model3.predict(x_pred)),
        np.max(model4.predict(x_pred)),
        np.max(model5.predict(x_pred)),
        np.max(model6.predict(x_pred)),
        np.max(model7.predict(x_pred)),        
    ])
    y_label = np.array([
        bool(np.argmax(model1.predict(x_pred),axis=1)),
        bool(np.argmax(model2.predict(x_pred),axis=1)),
        bool(np.argmax(model3.predict(x_pred),axis=1)),
        bool(np.argmax(model4.predict(x_pred),axis=1)),
        bool(np.argmax(model5.predict(x_pred),axis=1)),
        bool(np.argmax(model6.predict(x_pred),axis=1)),
        bool(np.argmax(model7.predict(x_pred),axis=1)),
    ])
    return y_pred,y_label

