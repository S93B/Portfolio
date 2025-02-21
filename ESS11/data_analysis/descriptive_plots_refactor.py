import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ESS11.utilities.functions import save_plot

path = "/ESS11/archive/data_NL_transf_kneighbor_v3.csv"
df = pd.read_csv(path, index_col=0)

print(df.columns)
print(df.info())

 #Selection to work with
df_pol = df.loc[:, ['age', 'gender', 'education', 'educational_level', 'activity_work', 'voted', 'political_trust']]


###############################################
# Gender piechart
gender_counts = df_pol['gender'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightblue', 'lightcoral']
)

plt.title('Gender Distribution', fontsize=14)
save_plot(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\gender.png')

#Exploration plots
# sns.set_theme(style='whitegrid')
# plt.figure(figsize=(10, 6))
# plot_categoricals = ['educational_level', 'voted']
# print(df.voted.value_counts())
#
# for feature in plot_categoricals:
#     sns.countplot(data=df_pol, x=feature,stat='percent')
#     plt.show()
#     plt.close()


plt.figure(figsize=(12, 8))
sns.histplot(data=df_pol, x='political_trust', stat='percent', kde=False, bins=10)
plt.title('Distribution of Political Trust', fontsize=14)
plt.xlabel('Political Trust', fontsize=12)
plt.ylabel('Percentage', fontsize=12)
plt.tight_layout()
save_plot(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\political_trust.png')

#edu trust boxplot
order_eduplot = ['lower_educated', 'mid_educated', 'highly_educated']
sns.catplot(data=df_pol, x='educational_level', y='political_trust', kind='box', order=order_eduplot,)
save_plot(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\education_political_trust.png')

#Lineplot relation education and trust
sns.lineplot(data=df_pol, x='educational_level', y='political_trust')
save_plot(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\political_trust_line.png')

#trust edu for gender
sns.lineplot(data=df_pol, y='political_trust', x='educational_level', hue='gender')
save_plot(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\political_trust_line_gender.png')