import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path = 'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf_v2.csv'
df = pd.read_csv(path, index_col=0)

print(df.columns)

#rename pol vars for easy readability
df.rename(columns={'trstprl': 't_parlement', 'trstlgl': 't_legalsystem', 'trstplc': 't_police', 'trstplt': 't_politicians', 'trstprt': 't_political_parties', 'trstep': 't_EU_parlement', 'trstun': 't_united_nations'}, inplace=True)
#rename social trust vars

#rename national id vars


# sociodemo descriptives
slice = df.iloc[:, [0,1,2]]
slice1 = slice.groupby('gender')
desr_slice1 = slice1.describe()

slice2 = df.groupby(by = ['gender', 'educational_level'])
desc_slice2 = slice2.describe()
sns.displot(data=slice1, x='age', kind='hist')
plt.show()


#Divide per voted political party and compare % to latest election