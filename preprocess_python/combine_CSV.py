import pandas as pd

a = pd.read_csv('new_ca_list.csv')
b = pd.read_csv('new_heart_list.csv')
c = pd.read_csv('new_hernia_list.csv')
d = pd.read_csv('new_intra_list.csv')
e = pd.read_csv('new_no_finding_list.csv')
f = pd.read_csv('new_tb_list.csv')
All_File=[]
All_Symptom=[]
All_path=[]
print(a['Image File'].size + b['Image File'].size + c['Image File'].size + d['Image File'].size + e['Image File'].size + f['Image File'].size )
half = 1000
qua = 500
tri = 250
hud = 100
for i in range(0,hud):
    All_File.append(e['Image File'][i])
    All_Symptom.append("No Finding")
    #path = "../input/1_No_Finding/"+e['Image File'][i]
    #All_path.append(path)
for i in range(0,hud):
    All_File.append(f['Image File'][i])
    All_Symptom.append("TB")
    #path = "../input/2_TB/"+f['Image File'][i]
    #All_path.append(path)
for i in range(0,hud):
    All_File.append(b['Image File'][i])
    All_Symptom.append("Heart")
    #path = "../input/3_Heart/"+b['Image File'][i]
    #All_path.append(path)
for i in range(0,hud):
    All_File.append(a['Image File'][i])
    All_Symptom.append("CA lung")
    #path = "../input/4_CA_lung/"+a['Image File'][i]
    #All_path.append(path)
for i in range(0,hud):
    All_File.append(d['Image File'][i])
    All_Symptom.append("Intra")
    #path = "../input/5_Intra/"+d['Image File'][i]
    #All_path.append(path)
for i in range(0,hud):
    All_File.append(c['Image File'][i])
    All_Symptom.append("Extra")
    #path = "../input/6_Extra/"+c['Image File'][i]
    #All_path.append(path)

combine_CSV = pd.DataFrame({
    'Image File' : All_File,
    'Diagnosis' : All_Symptom,
    #'full_path' : All_path
})
print(len(All_File))
print(len(All_Symptom))
combine_CSV.to_csv("Raw_Data_100.csv")
print(combine_CSV)