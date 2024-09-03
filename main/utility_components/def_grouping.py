import pandas as pd
ds = pd.read_csv('C:\Python homedirectory\portfolio_stellaris\main/utility_components\defense_modules.csv', delimiter=',', skiprows=0)
ds = ds.rename(str.lower, axis="columns")
print(ds.columns)
def_high_tier = ds.loc[ds["tier"] == 5]
def_high_tier.to_csv("def_high_tier.csv", index=False)
