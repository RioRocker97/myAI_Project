from PIL import Image
import os

path = "AI_Data_1/6_Extra/"
num=1
#for img in os.listdir(path):
#    old = Image.open(path+img)
#    new_img = old.resize((224,224))
#    new_img.save(path+'temp/'+img)
#    print("ok",num)
#    num+=1
for img in os.listdir(path):
    if img != 'jpg':
        old = Image.open(path+img)
        new_img = old.convert('RGB')
        img_url = img.split('.')[0]
        new_img_url = path+"jpg/"+img_url+".jpg"
        new_img.save(new_img_url,'JPEG',quality=100)
        print("Change Type OK",num)
        num+=1