import pandas as pd
import pingouin as pg
import numpy as np
from sklearn.impute import KNNImputer
df = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf_satis.csv', index_col=0)
#df.set_index(keys=['respondent'], inplace=True)
print(df.isna().sum())
print(df.shape)
print(df.info())

#How many non-voters?
print(df.voted.value_counts())

#Replace missings on voted with party closeness choice
print(df.voted_party.unique())
df['voted_party'] = df['voted_party'].fillna(value=99)
df['voted_party'] = df.apply(lambda row: row['which_p_close'] if row['close_party'] == 1 else row['voted_party'], axis=1)
df['voted_party'] = df.apply(lambda row: np.nan if row['voted_party'] == 99 else row['voted_party'], axis=1)

## K-Nearest neighbor
original_index = df.index
df_encoded = pd.get_dummies(df, columns=['gender'], dummy_na=True)
#columns_impute = ['age', 'education', 'activity_work', 'educational_level','trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun']
df_encoded = df_encoded.drop(axis=1, columns=['educational_level'])
imputer = KNNImputer(n_neighbors=5, weights='uniform')
imputed_df = pd.DataFrame(imputer.fit_transform(df_encoded), columns=df_encoded.columns)
imputed_df.index = original_index

# Round k-neighbor imputed values
columns_to_round =['trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun', 'stfeco', 'stfdem', 'stfgov', 'stfhlth', 'stfedu']
imputed_df[columns_to_round] = imputed_df[columns_to_round].apply(np.round, decimals=0)
# Slicing for trust variables, cronbach alpha, creating mean scale

factor_1 = imputed_df.loc[: , ['trstprl', 'trstplt', 'trstprt', 'trstep']]
#factor_1 = factor_1.loc[: , ['trstprl','trstplt', 'trstprt', 'trstep']].apply(np.round, decimals=1)
print(pg.cronbach_alpha(data=factor_1))  # alfa == 0.9
factor_1['political_trust'] = factor_1.mean(axis=1)
print(factor_1.political_trust.mean())
desc_factor1 = factor_1.describe()

# Slicing for trust variables, cronbach alpha, creating mean scale
# factor_2 = imputed_df.loc[: , ['trstprl', 'trstplt', 'trstprt', 'trstep']] # FIXME selectie variabel klopt niet
# print(pg.cronbach_alpha(data=factor_2))  # alfa == 0.9
# factor_2['political_trust'] = factor_2.mean(axis=1)
# print(factor_2.political_trust.mean())
# desc_factor2 = factor_2.describe()
# desc_combined = pd.concat([desc_factor1, desc_factor2], axis=1) # compare

#dropping dummys
imputed_df.drop(columns=['gender_nan', 'gender_Male', 'gender_Female'], inplace=True)
#inserting dropped columns back
imputed_df['gender'] = df['gender']
imputed_df['educational_level'] = df['educational_level']
#insert pol trust scale
imputed_df['political_trust'] = factor_1['political_trust']
imputed_df.rename(columns={'Unnamed: 0': 'respondent'}, inplace=True)
imputed_df.to_csv('C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf_kneighbor_v2.csv')


# TODO K-NEIGHBORS moet afronden