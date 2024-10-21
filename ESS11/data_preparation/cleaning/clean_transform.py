import pandas as pd
from ESS11.utilities.functions import replace_missing_with_sentinels

df = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\interim\data_NL_political.csv', index_col=0)
print(df.shape)
print(df.info())

print(df.duplicated().sum())
desc = df.describe()

# recode the no answers; dont knows et cetera. See codebook
from ESS11.documentation.lists_dic_repository import list_sentinel_thou, list_sentinel_ten, list_sentinel_single

#What to do with non-voters?
print(df.value_counts(subset=['voted'])) # 2 refusal;
print(df.value_counts(subset=['which_p_close'])) # 2 refusal;
print(df.value_counts(subset=['close_party']))
print(df.value_counts(subset=['voted_party']))

var_list_mis_ten = ['activity_work','voted_party', 'placement_l_r', 'trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun']
var_list_mis_thou = ['age', 'education']
var_list_mis_single = ['gender', 'educational_level', 'voted']

# Important: first comes question close_party, if 1: which_p_close. if 2: which_p_close == Not applicable, thus != missing

# replace sentinel values with NaN for easy analysis
df = replace_missing_with_sentinels(df, list_sentinel_thou, var_list_mis_thou)
df = replace_missing_with_sentinels(df, list_sentinel_single, var_list_mis_single)
df = replace_missing_with_sentinels(df, list_sentinel_ten, var_list_mis_ten)
desc = df.describe()

print(df.isna().sum())

df.to_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf.csv')