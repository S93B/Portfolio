import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('/ESS11/data/processed/data_NL_transf.csv', index_col=0)

#trust variables
pol_trust = df.loc[:, ['trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun',]].dropna()
print(pol_trust.isna().sum())
print(pol_trust.info())

# TODO: first figure out factor analysis
scaler = StandardScaler()
scaled_data = scaler.fit_transform(pol_trust)

pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)

pricipal_df = pd.DataFrame(data=principal_components, columns=['principal component 1', 'principal component 2'])
print(pricipal_df.head(5))
factor_loadings = pca.components_
print(factor_loadings)
print(pca.explained_variance_ratio_)
