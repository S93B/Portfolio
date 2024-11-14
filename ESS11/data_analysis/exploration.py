import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = '/ESS11/data/processed/data_NL_transf.csv'
df = pd.read_csv(path, index_col=0)

from ESS11.documentation.lists_dic_repository import dic_political_parties, dic_political_parties_closeness
df['voted_party_s'] = df['voted_party'].map(dic_political_parties) ##to other module!

slice1 = df.groupby('voted_party_s')
sorted_trust = slice1.political_trust.sort_values(ascending=False)
des_slice = slice1.describe()
print(slice1.political_trust.mean().head(5))

