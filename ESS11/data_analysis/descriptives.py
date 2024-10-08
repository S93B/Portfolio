import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = 'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf_v2.csv'
df = pd.read_csv(path, index_col=0)

print(df.columns)

#rename pol vars for easy readability
df.rename(columns={'trstprl': 't_parlement', 'trstlgl': 't_legalsystem', 'trstplc': 't_police', 'trstplt': 't_politicians', 'trstprt': 't_political_parties', 'trstep': 't_EU_parlement', 'trstun': 't_united_nations'}, inplace=True)

#Create dataframe for analysis political trust
educational_bins = [0,5,11,18]
educational_levels = ['lower_educated', 'mid_educated', 'highly_educated']
df['educational_level'] = pd.cut(df['education'], bins=educational_bins, labels=educational_levels)
df_pol = df.loc[:, ['age', 'gender', 'education', 'educational_level', 'activity_work', 'voted', 'political_trust']]

# sociodemo descriptivesoo
df_describe = df_pol.describe()

slice = df_pol.loc[:, ['political_trust', 'educational_level']]
slice2 = slice.groupby(by = ['educational_level'])
desc_slice2 = slice2.describe()

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_pol, x='educational_level', y='political_trust')
plt.savefig(fr'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\political_trust_line.png')

#Exploration plots
plot_categoricals = ['gender', 'educational_level', 'activity_work', 'voted']
plot_continous = ['age', 'political_trust']

for feature in plot_categoricals:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_pol, x=feature,stat='percent')
    plt.savefig(fr'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\{feature}.png')
    plt.close()

for feature in plot_continous:
    plt.figure(figsize=(10, 6))
    sns.displot(data=df_pol, x=feature, stat='frequency')
    plt.savefig(fr'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\{feature}.png')
    plt.close()

#Divide per voted political party and compare % to latest election