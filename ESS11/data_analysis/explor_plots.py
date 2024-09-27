import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/ESS11/data/processed/data_NL_transf.csv', index_col=0)
#plots
sns.catplot(df, x='gender', kind='count')
sns.catplot(df, x='marital_status', kind='count')
sns.histplot(df, x='age')
plt.show()
