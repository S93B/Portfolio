import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path = 'C:\Python homedirectory\Portfolio_git\ESS11\data\interim\data_selected_NL.csv'
df = pd.read_csv(path, index_col=0)

print(df.columns)

# sociodemo descriptives
slice = df.iloc[:, [0,1,2]]
slice1 = slice.groupby('gender')
desr_slice1 = slice1.describe()

sns.displot(data=slice1, x='age', kind='hist')
plt.show()