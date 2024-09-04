import pandas as pd
ds = pd.read_csv('/stellaris_weapon_simulator/utility_components\defense_modules.csv', delimiter=',', skiprows=0)
ds = ds.rename(str.lower, axis="columns")
print(ds.columns)
def_high_tier = ds.loc[ds["tier"] == 5]
def_high_tier.to_csv("def_high_tier.csv", index=False)
