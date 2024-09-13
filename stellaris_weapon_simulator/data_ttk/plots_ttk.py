import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ws = pd.read_csv('C:\Python homedirectory\Portfolio_git\stellaris_weapon_simulator\data_ttk\data_ttk.csv')

XL_group = ws.loc[ws["size"] == "XL"]  # met index als column size
titan_group = XL_group.iloc[-3:, :]
small_slot = ws.loc[ws["size"] == "S"]
medium_slot = ws.loc[ws["size"] == "M"]
large_slot = ws.loc[ws["size"] == "L"]

for index, row in ws.iterrows():
    if row['seconds'] > 5000:
        ws.drop(index, inplace=True)

plt.figure(figsize=(10, 6))
plt.yticks(ha='right')
sns.scatterplot(data=ws, y='name', x='seconds', size='size', hue='size')
plt.tight_layout()
#plt.savefig('figure_all_ttk')
plt.show()
