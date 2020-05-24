import pandas as pd

mydata = pd.read_csv('ChestXray-NIHCC/Data_Entry_2017.csv')
unique_label = mydata['Finding Labels'].unique()
#print(len(unique_label))

def FindLabel(array,label) :
    split_array = []
    is_split_array =0
    for i in array:
        if i == '|':
            split_array = array.split('|')
            is_split_array =1
            break
        else:
            split_array = array
    if is_split_array:
        for i in split_array:
            if i == label:
                return True
    else:
        if split_array == label:
            return True
def GetLabel(array,label) :
    true_label = ""
    split_array = []
    is_split_array =0
    for i in array:
        if i == '|':
            true_label = array
            split_array = array.split('|')
            is_split_array =1
            break
        else:
            split_array = array
    if is_split_array:
        for i in split_array:
            if i == label:
                return true_label
    else:
        if split_array == label:
            return split_array
def SortLabel(data,array):
    get_data = data['Finding Labels'] == array[0]
    for i in range(1,len(array)):
        get_data |= data['Finding Labels'] == array[i]
    dataframe = pd.DataFrame({
        'Image File': data[get_data]['Image Index'][:4000],
        'Finding Labels': data[get_data]['Finding Labels'][:4000]
    })
    dataframe.reset_index(inplace=True)
    dataframe = dataframe.drop(columns='index')
    return dataframe

class_num = [0,0,0,0,0,0,0]
tb_class =[]
heart_class =[]
calung_class =[]
intra_class =[]
extra_class =[]
pneumonia_class = []

for i in unique_label:
    if FindLabel(i,'No Finding'):
        class_num[0]+=1
    elif FindLabel(i,'Mass') or FindLabel(i,'Module'):
        class_num[1]+=1
        tb_class.append(i)
    elif FindLabel(i,'Edema') or FindLabel(i,'Cardiomegaly'):
        class_num[2]+=1
        heart_class.append(i)
    elif ( FindLabel(i,'Atelectasis') or FindLabel(i,'Consolidation') or FindLabel(i,'Emphysema') 
    or FindLabel(i,'Fibrosis') or FindLabel(i,'Infiltration') ) and not FindLabel(i,'Pneumonia'):
        class_num[3]+=1
        calung_class.append(i)
    elif FindLabel(i,'Pleural_Thickening') or FindLabel(i,'Pneumothorax'):
        class_num[4]+=1
        intra_class.append(i)
    elif FindLabel(i,'Hernia'):
        class_num[5]+=1
        extra_class.append(i)
    elif FindLabel(i,'Pneumonia'):
        class_num[6]+=1
        pneumonia_class.append(i)

print("NoF--TB--HEART--CALUNG--INTRA--EXTRA--PENO")
print(class_num,'\n')

is_nof = SortLabel(mydata,['No Finding'])
is_tb = SortLabel(mydata,tb_class) #5700
is_heart = SortLabel(mydata,heart_class) #4731
is_ca_lung = SortLabel(mydata,calung_class) #10000
is_intra = SortLabel(mydata,intra_class) # 6316
is_extra = SortLabel(mydata,extra_class) #148
is_peno = SortLabel(mydata,pneumonia_class) #

print(is_tb.index)
print(is_heart.index)
print(is_ca_lung.index)
print(is_intra.index)
print(is_extra.index)
print(is_peno.index)

#print(is_extra)
#print(calung_class)
#print("=========================================================================")
#print(pneumonia_class)

is_nof.to_csv('4000_nof.csv')
is_tb.to_csv('4000_tb.csv')
is_heart.to_csv('4000_heart.csv')
is_ca_lung.to_csv('4000_ca_lung.csv')
is_intra.to_csv('4000_intra.csv')
is_extra.to_csv('4000_extra.csv')
is_peno.to_csv('4000_peno.csv')