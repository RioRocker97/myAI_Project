import pandas as pd

BASE = pd.read_csv("19200_CSV_7_Classes.csv")
LABEL = ['CA','Extra','Heart','Intra','No Finding','Pneumonia','TB']
COL = ['Is_CA','Is_Extra','Is_Heart','Is_Intra','Is_NoF','Is_Peno','Is_TB']
for i in range(0,7):
    add = pd.DataFrame(columns=['Image File',COL[i]])
    for j in range(0,19200):
        if BASE['Finding Label'][j] == LABEL[i]:
            add.loc[j] = [BASE['Image File'][j],'Yes']
            print(LABEL[i],'Yes',j)
        else :
            add.loc[j] = [BASE['Image File'][j],'No']
            print(LABEL[i],'No',j)
    add.to_csv('19200_'+LABEL[i]+'_class.csv')
    add = add.iloc[0:0]