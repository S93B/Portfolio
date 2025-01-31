import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\Python homedirectory\Portfolio_git\Oefeningen\customer_satisfaction\E-commerce_NPA_Dataset.csv", index_col=0)

# Missings/type/length check
print(df.info())

f, ax = plt.subplots(figsize=(10,7))
corr = df.corr(numeric_only=True, method='pearson')
hm = sns.heatmap(round(corr,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f', vmin=-1, vmax=1, yticklabels=corr.columns, xticklabels=corr.columns)
f.subplots_adjust(top=0.83)
t= f.suptitle('Correlation Heatmap', fontsize=14)
# plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\correlation_heatmap.png')
plt.show()




df_describe = df.describe()
print(df.Gender.value_counts())
# Exploration demographic groups
group_gender = df.groupby('Gender')
print(group_gender.value_counts())


