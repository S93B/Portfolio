import numpy as np
import pandas as pd
from ESS11.documentation.lists_dic_repository import *
df = pd.read_csv('C:/Python homedirectory/ESS/ESS11/data/raw/ESS11.csv')

# data shape
print(df.info())
print(df.head)

# selection country NL
dd = df.loc[df['cntry'] == 'NL']
# print(dd.shape)

# var selection socio-demographics
socdemo_var = dd.loc[:, ['gndr', 'agea', 'edlvenl', 'mnactic']]
socdemo_labels = {'gndr': 'gender', 'agea': 'age', 'edlvenl': 'education', 'mnactic': 'activity_work'}
socdemo_var = socdemo_var.rename(columns=socdemo_labels)
print(socdemo_var.info())

#recode educational level into three categories
## range 1 - 5 = low.
## range 6 - 11 = mid
## range 12 - 18 = high
educational_bins = [0, 6, 11, 18]
educational_levels = ['lower_educated', 'mid_educated', 'highly_educated']
socdemo_var['educational_level'] = pd.cut(socdemo_var['education'], bins=educational_bins, labels=educational_levels)
print(socdemo_var.educational_level.value_counts())

# gender
gender_labels = {1: 'Male', 2: 'Female', 9: 'No answer'}
socdemo_var['gender'] = socdemo_var['gender'].map(gender_labels)
print(socdemo_var.gender.value_counts())

# recode the no answers; dont knows et cetera. See codebook
list_missing = [5555,6666, 7777, 8888, 9999, 999]
list_missing2 = [66, 77, 88, 99]
socdemo_var = socdemo_var.replace(list_missing, np.nan)
socdemo_var.activity_work = socdemo_var.activity_work.replace(list_missing2)
print(socdemo_var.describe())


# var selection politics
ptrust_var = dd.loc[:, ['trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun',]]
pvote_var = dd.loc[:, ['vote', 'prtvtinl']]
pvote_labels = {'vote': 'voted', 'prtvtinl': 'party'}

#rename pvar columns and replace missing answers
pvote_var = pvote_var.rename(columns=pvote_labels)
ptrust_var = ptrust_var.replace(list_missing2, np.nan)
pvote_var = pvote_var.replace(list_missing2, np.nan)
pvote_var['party'] = pvote_var['party'].map(dic_political_parties)
print(pvote_var.party.count())

#check whether high nr are replaced
print(ptrust_var.describe())
print(pvote_var.describe())