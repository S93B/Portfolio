import pandas as pd
from ESS11.utilities.functions import calculate_pearson_correlation
df = pd.read_csv(r'/ESS11/data/processed/data_NL_transf.csv', index_col=0)
corr_df = df.corr(numeric_only=True)

#trust variables
pol_trust = df.loc[:, ['trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun',]].dropna()
print(pol_trust.isna().sum())
print(pol_trust.info())
# Compute Pearson correlation for all trust variables
pearson_result = calculate_pearson_correlation(pol_trust)
pearson_result.duplicated().sum()
pearson_result.drop_duplicates(inplace=True)
pearson_result.sort_values(by='Correlation', ascending=False, inplace=True)
pearson_result.to_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\political_trust_correlation_p.csv')

# TODO: check datapath and overal