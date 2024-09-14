import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from var_selection import socdemo_var

#plots
sns.catplot(socdemo_var, x='gender', kind='count')
sns.catplot(socdemo_var, x='marital_status', kind='count')
sns.histplot(socdemo_var, x='age')
plt.show()
