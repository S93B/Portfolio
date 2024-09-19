import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\interim\data_selected_NL.csv', index_col=0)

# recode the no answers; dont knows et cetera. See codebook
list_sentinel_thou = [5555, 6666, 7777, 8888, 9999, 999]
list_sentinel_ten = [66, 77, 88, 99]
df.age = df.age.replace(list_sentinel_thou, np.nan)
df.activity_work = df.activity_work.replace(list_sentinel_ten)
print(df.describe())

#rename pvar columns and replace missing answers
ptrust_var = df.replace(list_sentinel_ten, np.nan)
pvote_var = df.replace(list_sentinel_ten, np.nan)
print(pvote_var.party.count())

df.to_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf.csv')