import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Python homedirectory/ESS/ESS11/data/raw/ESS11.csv')
df.agea.describe()
sns.catplot(data=df, y='agea', kind='box')

plt.show()