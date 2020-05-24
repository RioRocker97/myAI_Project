import pandas as pd
import os,shutil
name = 'TB'
BASE = pd.read_csv('10000_CSV_7_Classes.csv')
csv = pd.DataFrame(columns=['Image File','Is_'+name])

for i in range(0,10000):
    if BASE['Finding Label'][i] == name:
        csv.loc[i] = [BASE['Image File'][i],'Yes']
        print("Yes",i)
    else:
        csv.loc[i] = [BASE['Image File'][i],'No']
        print("No",i)

print(csv)
csv.to_csv("10000_"+name+"_Class.csv")