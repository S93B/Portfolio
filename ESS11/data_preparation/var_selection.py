import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

df = pd.read_csv('C:/Python homedirectory/ESS/ESS11/data/raw/ESS11.csv')

# data shape
# print(df.info())
# print(df.head)

# selection country NL
dd = df.loc[df['cntry'] == 'NL']
# print(dd.shape)

# var selection socio-demographics
socdemo_var = dd.loc[:, ['gndr', 'agea', 'marsts', 'edlvenl', 'mainact', 'edlvpenl', 'pdwrkp' ]]
socdemo_labels = {'gndr': 'gender', 'agea': 'age', 'edlvenl': 'education_level', 'mainact': 'activity_work', 'edlvpenl': 'partner_education',  'pdwrkp': 'partner_activity' }
socdemo_var = socdemo_var.rename(columns=socdemo_labels)
# print(socdemo_var.columns)

# gender
gender_labels = {1: 'Male', 2: 'Female', 9: 'No answer'}
socdemo_var['gender'] = socdemo_var['gender'].map(gender_labels)
# print(socdemo_var.gender)

# recode the no answers; dont knows et cetera. See codebook
list_missing = [5555,6666, 7777, 8888, 9999, 999]
socdemo_var = socdemo_var.replace(list_missing, np.nan)
socdemo_describe = socdemo_var.describe()

# var selection politics
ptrust_var = dd.loc[:, ['trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun',]]
pvote_var = dd.loc[:, ['vote', 'prtvtinl']]
pvote_labels = {'vote': 'voted', 'prtvtinl': 'party'}
pvote_var = pvote_var.rename(columns=pvote_labels)
list_missing2 = [77, 88, 99]
ptrust_var = ptrust_var.replace(list_missing2, np.nan)
print(ptrust_var.describe())
print(pvote_var.describe())