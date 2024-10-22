import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'/ESS11/archive/data_NL_transf.csv')

# TODO: sociodemo distributions with plots
sns.displot(data=df, x='age', kind='hist', kde=True)
df.age.describe() # m = 50 in sample. M = 42 in N.
sns.displot(data=df, x='educational_level', kind='hist')

plt.show()