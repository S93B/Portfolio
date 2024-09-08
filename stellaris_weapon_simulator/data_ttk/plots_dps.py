import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:\Python homedirectory\Portfolio_git\stellaris_weapon_simulator\data_prep\create_weap_data\weapon_set.csv')
df.drop(df.index[df['size'] == "empty"], inplace=True)  # remove empty size rodf

g = sns.FacetGrid(df, col='tech')
g.map(sns.scatterplot, 'DPS', 'key', alpha=.7)
plt.show()
