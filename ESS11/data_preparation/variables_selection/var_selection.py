import pandas as pd
from ESS11.documentation.lists_dic_repository import dic_political_parties, dic_political_parties_closeness

df = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\raw\ESS11.csv')

# data shape
print(df.info())
print(df.head())

# selection country NL
dd = df.loc[df['cntry'] == 'NL']

# var selection socio-demographics
socdemo_var = dd[['gndr', 'agea', 'edlvenl', 'mnactic']].copy()
socdemo_var = socdemo_var.rename(columns = {'gndr': 'gender', 'agea': 'age', 'edlvenl': 'education', 'mnactic': 'activity_work'})
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
pvote_var = dd[['vote', 'prtvtinl','clsprty', 'prtclhnl', 'prtdgcl', 'lrscale']].copy()
pvote_var = pvote_var.rename(columns={'vote': 'voted', 'prtvtinl': 'voted_party', 'clsprty': 'close_party', 'prtclhnl': 'which_p_close', 'prtdgcl': 'how_close', 'lrscale': 'placement_l_r'})
# pvote_var['v_l_election'] = pvote_var['v_l_election'].map(dic_political_parties) ##to other module!
# pvote_var['closeness_v_l_election'] = pvote_var['closeness_v_l_election'].map(dic_political_parties_closeness)

#check for matching index
print(socdemo_var.index.equals(pvote_var.index))

from ESS11.utilities.functions import check_matching_indices
if check_matching_indices(socdemo_var, pvote_var, ptrust_var):
     df = pd.concat([socdemo_var, pvote_var, ptrust_var], axis=1)
else:
    print("DataFrames do not have matching indices.")

#data_concat_b = pd.concat([socdemo_var, health_var, bmi], axis=1) for later

df.to_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\interim\data_NL_political.csv')
#print(df.info())