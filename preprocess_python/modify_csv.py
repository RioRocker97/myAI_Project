import pandas as pd

old_csv = pd.read_csv('AI_Data_1/Raw_Data.csv')
old_csv = old_csv.drop(labels="full_path",axis=1)

print(old_csv)