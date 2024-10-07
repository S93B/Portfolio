import pandas as pd
from ESS11.utilities.functions import replace_missing_with_sentinels

odf = pd.read_csv('C:\Python homedirectory\Portfolio_git\ESS11\data\interim\data_NL_political_soctrust.csv', index_col=0)
print(odf.shape)
print(odf.info())
df = odf.copy()

print(df.duplicated().sum())
desc = df.describe()

# recode the no answers; dont knows et cetera. See codebook
from ESS11.documentation.lists_dic_repository import list_sentinel_thou, list_sentinel_ten
describe_df = df.describe() # open in dataviewer

# replace sentinel values with NaN for easy analysis
columns_to_check = ['age', 'education']
df = replace_missing_with_sentinels(df, list_sentinel_thou, columns_to_check)
df = replace_missing_with_sentinels(df, list_sentinel_ten, df.iloc[:, 2:])
print(df.describe())

df.to_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf.csv')