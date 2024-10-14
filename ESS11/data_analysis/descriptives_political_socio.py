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

# Update dataframe with var name changes
df.to_csv('C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf_v2.csv')

#Selection to work with
df_pol = df.loc[:, ['age', 'gender', 'education', 'educational_level', 'activity_work', 'voted', 'political_trust']]

# sociodemo descriptivesoo
df_describe = df_pol.describe()

slice = df_pol.loc[:, ['political_trust', 'educational_level']]
slice2 = slice.groupby(by = ['educational_level'])
desc_slice2 = slice2.describe()



###############################################
#Exploration plots
sns.set(style='whitegrid')
plt.figure(figsize=(10, 6))
plot_categoricals = ['educational_level', 'activity_work', 'voted']

for feature in plot_categoricals:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_pol, x=feature,stat='percent')
    plt.savefig(fr'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\{feature}.png')
    plt.close()

#age
sns.displot(data=df_pol, x='age', kind='hist', kde=True)
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\age.png')
plt.close()
sns.displot(data=df_pol, x='political_trust', kind='hist', kde=True)
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\political_trust.png')
plt.close()
#gender
sns.catplot(data=df_pol, x='gender', kind='count',stat='percent')
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\gender.png')
plt.close()
sns.catplot(data=df_pol, x='educational_level', col='gender', kind='count')
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\gender_education.png')
plt.close()
#edu trust boxplot
sns.catplot(data=df_pol, x='educational_level', y='political_trust', kind='box')
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\education_political_trust.png')
plt.close()
#Lineplot relation education and trust
sns.lineplot(data=df_pol, x='educational_level', y='political_trust')
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\political_trust_line.png')
plt.close()
#trust edu for gender
sns.lineplot(data=df_pol, y='political_trust', x='educational_level', hue='gender')
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\political_trust_line_gender.png')
plt.close()
#Divide per voted political party and compare % to latest election