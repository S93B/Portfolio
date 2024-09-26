import numpy as np
import pandas as pd
from ESS11.utilities.functions import replace_missing_with_sentinels

odf = pd.read_csv(r'ESS11/data/interim/data_NL_political_soctrust.csv', index_col=0)
print(odf.shape)
print(odf.info())
df = odf.copy()

list_sentinel_thou = [5555, 6666, 7777, 8888, 9999, 999]
list_sentinel_ten = [66, 77, 88, 99]

# recode the no answers; dont knows et cetera. See codebook
##from ESS11.documentation.lists_dic_repository import list_sentinel_thou NOT WORKING?!
describe_df = df.describe() # open in dataviewer

# replace sentinel values with NaN for easy analysis

columns_to_check = ['ptrust_var', 'pvote_var']
df = replace_missing_with_sentinels(df, list_sentinel_ten, columns_to_check)

df.age = df.age.replace(list_sentinel_thou, np.nan)

df.activity_work = df.activity_work.replace(list_sentinel_ten)
print(df.describe())

#rename pvar columns and replace missing answers
ptrust_var = df.replace(list_sentinel_ten, np.nan)
pvote_var = df.replace(list_sentinel_ten, np.nan)
print(pvote_var.party.count())

df.to_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf.csv')
