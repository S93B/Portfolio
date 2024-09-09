import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:\Python homedirectory\Portfolio_git\stellaris_weapon_simulator\data_prep\create_weap_data\weapon_set.csv')

ws = df.loc[df['size'] != 'XL'] # XL slots uitsluiten ivm leesbaarheid plot
sns.set_style("whitegrid")
g = sns.FacetGrid(ws, col='tech', height=5, aspect=0.8, col_wrap=2, hue='size', sharex=False, sharey=False)
g.map(sns.scatterplot, 'DPS', 'key')
g.savefig('figure_w_dps')
# plt.show()

ws = df.loc[df['size'] == 'XL'] # aparte plot voor XL
plt.figure(figsize=(10, 6))
sns.scatterplot(ws, x='DPS', y='key', hue='tech')
plt.savefig('figure_XL_dps')
# plt.show()


## TODO: originele onderzoeksvraag beantwoorden en laten zien
### WORK IN PROGRESS