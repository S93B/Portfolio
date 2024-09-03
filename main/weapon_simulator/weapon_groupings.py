import pandas as pd
import matplotlib.pyplot as plt

# Load the data with the correct delimiter and handle headers
df = pd.read_csv('C:/Python homedirectory/Stellaris/ship_designer//weapons/weapon_components.csv', delimiter=',', skiprows=0)
ws = pd.read_csv("C:/Python homedirectory/Stellaris/ship_designer/weapons/weapon_set.csv", delimiter=',', skiprows=0)
#sc = pd.read_csv("C:/Python homedirectory/Stellaris/ship_designer/main/g_craft.csv", delimiter=',', skiprows=0)

series_dmg = ws.avg_dmg #index als naam; series heeft daarbij index naam erbij staan

df.mean(numeric_only=True)


# ws.reindex(index="size")
XL_group = ws.loc[ws["size"] == "XL"] # met index als column size
titan_group = XL_group.iloc[-3:, :]
small_slot = ws.loc[ws["size"] == "S"]
medium_slot = ws.loc[ws["size"] == "M"]
large_slot = ws.loc[ws["size"] == "L"]
dmg_s_avg = round(small_slot.describe(), 0)
dmg_m_avg = round(medium_slot.describe(), 0)
dmg_l_avg = round(large_slot.describe(), 0)
#dmg_s_avg.to_csv("dmg_s_avg.csv", index=True)
dmg_m_avg.to_csv("dmg_m_avg.csv", index=True)
dmg_l_avg.to_csv("dmg_l_avg.csv", index=True)
##methoden werkt niet

plt.plot()
plt.show