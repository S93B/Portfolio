import pandas as pd
from ESS11.documentation.lists_dic_repository import dic_political_parties
df = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\raw\ESS11.csv')

# data shape
print(df.info())
print(df.head())

# selection country NL
dd = df.loc[df['cntry'] == 'NL']
# print(dd.shape)

# var selection socio-demographics
socdemo_var = dd.loc[:, ['gndr', 'agea', 'edlvenl', 'mnactic']]
socdemo_labels = {'gndr': 'gender', 'agea': 'age', 'edlvenl': 'education', 'mnactic': 'activity_work'}
socdemo_var = socdemo_var.rename(columns=socdemo_labels)
print(socdemo_var.info())

#recode educational level into three categories
## 1 - 5 = low.
##  6 - 11 = mid
## 12 - 18 = high
educational_bins = [0, 5, 11, 18]
educational_levels = ['lower_educated', 'mid_educated', 'highly_educated']
socdemo_var['educational_level'] = pd.cut(socdemo_var['education'], bins=educational_bins, labels=educational_levels)
print(socdemo_var.educational_level.value_counts()) #relatively high nr of highly edu
print(socdemo_var.query('education == 12').head(5)) # should be high
print(socdemo_var.query('education == 6').head(5)) # should be mid

# gender
gender_labels = {1: 'Male', 2: 'Female', 9: 'No answer'}
socdemo_var['gender'] = socdemo_var['gender'].map(gender_labels)
print(socdemo_var.gender.value_counts())

# var selection politics
ptrust_var = dd.loc[:, ['trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun',]]
pvote_var = dd.loc[:, ['vote', 'prtvtinl']]
pvote_labels = {'vote': 'voted', 'prtvtinl': 'party'}
pvote_var = pvote_var.rename(columns=pvote_labels)
pvote_var['party'] = pvote_var['party'].map(dic_political_parties)

#check for matching index, just incase
print(socdemo_var.index)
print(pvote_var.index)

df = pd.merge(socdemo_var, pvote_var, left_index=True, right_index=True)
#df.to_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\interim\data_selected_NL.csv')
print(df.info())