import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

df = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\raw\ESS11.csv')

dd = df.loc[df['cntry'] == 'NL']

satisfaction_society = dd.loc[:, ['stflife', 'stfeco', 'stfgov', 'stfdem', 'stfedu', 'stfhlth']]

# Correlation heatmap
f, ax = plt.subplots(figsize=(10,7))
corr = satisfaction_society.corr(numeric_only=True, method='pearson')
hm = sns.heatmap(round(corr,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f', vmin=-1, vmax=1, yticklabels=corr.columns, xticklabels=corr.columns)
f.subplots_adjust(top=0.83)
t= f.suptitle('Correlation Heatmap', fontsize=14)
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\correlation_heatmap_satisf.png')

print(satisfaction_society.stfeco.value_counts())



#Import transf dataset and merge satisfaction variables
de = pd.read_csv('C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf.csv', index_col=0)

from ESS11.utilities.functions import check_matching_indices, replace_missing_with_sentinels

check_matching_indices(de, satisfaction_society)
de = pd.concat([de, satisfaction_society], axis=1)

#cleaning quick
from ESS11.documentation.lists_dic_repository import list_sentinel_thou, list_sentinel_ten, list_sentinel_single
from ESS11.utilities.functions import replace_missing_with_sentinels

print(de.info())

_columns = de.columns[-6:]

for column in _columns:
    print(de[column].value_counts())

columns_fill_list = ['stflife', 'stfeco', 'stfgov', 'stfdem', 'stfedu', 'stfhlth']
de = replace_missing_with_sentinels(de, list_sentinel_ten, columns_fill_list)
de.to_csv('C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf_satis.csv')



# Wat hiermee doen?
nat_id_var = dd.loc[:, ['atchctr', 'atcherp']]