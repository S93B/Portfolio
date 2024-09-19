import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf.csv')

# TODO: sociodemo distributions with plots
sns.displot(data=df, x='age', kind='hist', kde=True)
df.age.describe() # m = 50 in sample. M = 42 in N.
sns.displot(data=df, x='educational_level', kind='hist')

plt.show()