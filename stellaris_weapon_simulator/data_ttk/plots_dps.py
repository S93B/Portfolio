import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:\Python homedirectory\Portfolio_git\stellaris_weapon_simulator\data_prep\create_weap_data\weapon_set.csv')

# aantal types uitsluiten ivm leesbaarheid plot
mask1 = (df['size'] != 'XL') & (df.tech != 'point defence') & (df.tech != 'archaeo')
ws_f = df.loc[mask1 , ['key', 'DPS', 'tech', 'size']]
sns.set_style("whitegrid")
g = sns.FacetGrid(ws_f, col='tech', height=5, aspect=0.8, col_wrap=2, hue='size', sharex=False, sharey=False)
g.map(sns.scatterplot, 'DPS', 'key')
g.savefig('figure_w_dps')

# aparte plot voor XL
xl_s = df.loc[df['size'] == 'XL']
plt.figure(figsize=(7, 6))
sns.scatterplot(xl_s, x='DPS', y='key', hue='tech')
plt.tight_layout()
plt.savefig('figure_XL_dps')
#plt.show()

##TODO: formaat aanpassen zodat in readme goed staat


## TODO: originele onderzoeksvraag beantwoorden en laten zien
### WORK IN PROGRESS