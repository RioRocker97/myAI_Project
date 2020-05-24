import pandas as pd
data1 = pd.read_csv('3000_nof.csv')
data2 = pd.read_csv('3000_tb.csv')
data3 = pd.read_csv('3000_heart.csv')
data4 = pd.read_csv('3000_ca_lung.csv')
data5 = pd.read_csv('3000_intra.csv')
data6 = pd.read_csv('123_extra.csv')
data7 = pd.read_csv('903_peno.csv')

combine = [data1,data2,data3,data4,data5,data6[:120],data7[:900]]
pattern = ['NoF_','TB_','Heart_','CA_','Intra_','Extra_','Peno_']
label = ['No Finding','TB','Heart','CA Lung','Intra','Extra','Peno']
rag = [3000,3000,3000,3000,3000,120,900]

def changefilename(data,name,label,r):
    for i in range(0,r):
        #data['Image File'][i] = name+str(i+1)+'.jpg'
        data['Finding Labels'] = label

for i in range(0,7):
    changefilename(combine[i],pattern[i],label[i],rag[i])

all_data=pd.concat(combine)
all_data.reset_index(inplace=True)
all_data = all_data.drop(columns="index")
all_data = all_data.drop(columns="Unnamed: 0")
print(all_data)
#all_data.to_csv("RAW_DATA_4500.csv")
all_data.to_csv("RAW_DATA_3000+900+120_7_class.csv")