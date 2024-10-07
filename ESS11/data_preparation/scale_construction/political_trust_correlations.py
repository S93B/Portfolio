import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

from ESS11.utilities.functions import calculate_pearson_correlation

df = pd.read_csv('C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf.csv', index_col=0)
df.dropna(inplace=True)
df.isna().sum()

# Correlation heatmap
f, ax = plt.subplots(figsize=(10,7))
corr = df.corr(numeric_only=True, method='pearson')
hm = sns.heatmap(round(corr,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f', vmin=-1, vmax=1, yticklabels=corr.columns, xticklabels=corr.columns)
f.subplots_adjust(top=0.83)
t= f.suptitle('Correlation Heatmap', fontsize=14)
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\correlation_heatmap.png')

# Trust correlations
pol_trust = df.loc[:, ['trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun',]].dropna()
print(pol_trust.isna().sum())
print(pol_trust.info())

# Compute Pearson correlation for all trust variables
pearson_result = calculate_pearson_correlation(pol_trust)
pearson_result.duplicated().sum()
pearson_result.drop_duplicates(inplace=True)
pearson_result.sort_values(by='Correlation', ascending=False, inplace=True)
print(pearson_result.head(10))
pearsonr(pol_trust['trstprl'], pol_trust['trstplt'])
pearson_result.to_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\political_trust_correlation_p.csv')

# TODO: check datapath and overal