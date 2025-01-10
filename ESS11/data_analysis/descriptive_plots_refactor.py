import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = 'ESS11/data/processed/data_NL_transf_kneighbor_v2.csv'
df = pd.read_csv(path, index_col=0)

print(df.columns)
print(df.info())

 #Selection to work with
df_pol = df.loc[:, ['age', 'gender', 'education', 'educational_level', 'activity_work', 'voted', 'political_trust']]


###############################################
#Exploration plots
sns.set_theme(style='whitegrid')
plt.figure(figsize=(10, 6))
plot_categoricals = ['educational_level', 'voted']
print(df.voted.value_counts())
sns.countplot(df, x=df.activity_work, stat='percent')
plt.show()

for feature in plot_categoricals:
    sns.countplot(data=df_pol, x=feature,stat='percent')
    plt.show()
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
