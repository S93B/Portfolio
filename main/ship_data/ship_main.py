import pandas as pd
import matplotlib.pyplot as plot
from main.ship_data.ships_OOP import Ship

df = pd.read_csv("C:\Python homedirectory\portfolio_stellaris\main\ship_data\ship_data_original.csv", delimiter=';', skiprows=[8, 9, 10])  #skiprows for defensive station
df = df.rename(str.lower, axis="columns")
df.columns

#creating groups
nanite_ships = df.iloc[-2:]
menacing_ships = df.iloc[7:11]
fe_ships = df.iloc[11:14]
std_ships = df.iloc[0:7]
# df = df.drop(6)  #drop juggernaut
# df = df.drop(10)  #drop star eater


#Reading the defensive ship modules
dd = pd.read_csv("C:\Python homedirectory\portfolio_stellaris\main/utility_components\def_high_tier.csv", delimiter=',')
dd.rename(str.lower, axis="columns", inplace=True)
dd = dd.dropna()

#Calculate shield points
df.loc[[0,1,2,7,14], "shield_average"] = (dd.loc[3, "shield"] * (round(df.utility / 2))) # voor S slot ships
df.loc[[0,1,2,7,14], "regen"] = (dd.loc[3, "regen"] * round(df.utility / 2)) # voor S slot ships
df.loc[[3, 8, 9, 11], "shield_average"] = (dd.loc[4, "shield"] * (df.utility / 2)) / 2 # voor M slot ships
df.loc[[3, 8, 9, 11], "regen"] = (dd.loc[4, "regen"] * (df.utility / 2)) / 2
df.loc[[4, 5,6, 10, 12,13], "shield_average"] = (dd.loc[5, "shield"] * (df.utility / 4)) / 2
df.loc[[4, 5,6, 10, 12,13], "regen"]  = (dd.loc[5, "regen"] * (df.utility / 4)) / 2

df.loc[[0, 7],"armor_average"] = dd.loc[0, "armor"] * 1 # voor S slot ships; speciaal plekje voor de corvette vanwege oneven number
df.loc[[1,2,14],"armor_average"] = dd.loc[0, "armor"] * (df.utility / 2) # voor S slot ships
df.loc[[3, 8, 9, 11], "armor_average"] = (dd.loc[1, "armor"] * (df.utility / 2)) / 2 # voor M slot ships
df.loc[[4, 5,6, 10, 12,13], "armor_average"] = (dd.loc[2, "armor"] * (df.utility / 4)) / 2

#special armor voor nanite class
df.loc[15, "armor_average"] =  dd.loc[2, "armor"] * 1 + 1500
df.loc[15, "shield_average"] =  (dd.loc[5, "shield"] * 2) # idem oneven getal, dus kies voor twee shield modules en één armor
df.loc[15, "regen"] =  dd.loc[5, "regen"] * 2
df.loc[15, "armor_regen"] = 15
df.loc[14, "armor_average"] =  df.loc[14, "armor_average"] + 100
df.loc[14, "armor_regen"] = 5

ship_col = df
ship_col = ship_col.drop('utility', axis=1)
ship_col = ship_col.drop("disengagement chance", axis=1)
ship_col = ship_col.drop('command points', axis=1)
ship_col = ship_col.round(0)
ship_col["type"] = ship_col.type.str.lower()
ship_col.to_csv("ship_col.csv", index= False)