import pandas as pd
from stellaris_weapon_simulator.data_prep.create_weap_data.weapon_keys import key_list

# Load the original data with the correct delimiter
df = pd.read_csv(
    "C:/Python homedirectory/Stellaris/ship_designer/weapon_components_original.csv",
    delimiter=";",
    skiprows=5,
    comment="#",
)

# exclude weapon rows not used by the player
for i in range(87, 175):
    df = df.drop(i)
df = df.drop(186)
print(df)  # first 5 should be red laser and last 5 should be archaeo type

# REFORMAT index structure
df.key = df.key.str.lower()
df.insert(1, "size", "empty")
df.insert(2, "tier", 0)
df.insert(3, "tech", "empty")

# create columns for tier, size and technology
weapon_type_name = {
    "laser": "energy",
    "mass_driver": "kinetic",
    "plasma": "plasma",
    "autocannon": "kinetic",
    "kinetic": "kinetic",
    "missile": "missile",
    "torpedo": "missile",
    "disruptor": "energy",
    "lance": "energy",
    "emitter": "energy",
    "archaeo": "archaeo",
    "flak": "point defence",
    "defence": "point defence",
    "strike": "strike craft",
}

weapon_size_list = {
    "small": "S",
    "medium": "M",
    "large": "L",
    "missile": "S",
    "swarmer": "M",
    "torpedo": "G",
    "titan": "XL",
    "lance": "XL",
    "accelerator": "XL",
    "emitter": "XL",
    "artillery": "L",
}
weapon_tier_list = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5}


def create_tech_column(dataframe, key1, key2, string, string2):
    """Create tech column based on name of weapon.
    define dataframe; name of column to search for string;
    name of tech column; name of string search; and name of string output
    """
    for index, row in df.iterrows():
        if string in row[key1].lower():
            df.at[index, key2] = string2

# in één for loop??
for label, i in weapon_type_name.items():
    create_tech_column(df, "key", "tech", label, i)
for label, i in weapon_size_list.items():
    create_tech_column(df, "key", "size", label, i)
for label, i in weapon_tier_list.items():
    create_tech_column(df, "key", "tier", label, i)
# laser tier met de hand.

# Replace the strings in the 'key' column with the replacement_list values
df["key"] = df["key"].replace(key_list, value=None, inplace=True)
df.insert(1, "key2", key_list)
# check to see whether names correspond
df = df.drop("key", axis=1)

ws = df.iloc[0:, [0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13]]  # for normal stellaris_weapon_simulator
# ws = df.iloc[[87,163,164], [0,1,2,3,6,7,8,9,10,11,12,13]] ## for the alien stellaris_weapon_simulator
ws["avg_dmg"] = ((df["min_damage"] + df["max_damage"]) / 2) * df["accuracy"]
ws["cooldown"] = (df[["min_windup", "max_windup"]].mean(axis=1) + df.cooldown) / 10
ws["DPS"] = ws["avg_dmg"] / ws["cooldown"]
ws["hull_dps"] = (ws["avg_dmg"] * df["hull_damage"]) / ws["cooldown"]
ws["shield_dps"] = (ws["avg_dmg"] * df["shield_damage"]) / ws["cooldown"]
ws["armor_dps"] = (ws["avg_dmg"] * df["armor_damage"]) / ws["cooldown"]
ws["accuracy"] = df["accuracy"]
ws["tracking"] = df["tracking"]

ws.key2 = ws.key2.str.lower()
ws = ws.round(2)
ws = ws.dropna()
df.reset_index(drop=True, inplace=True)
ws.rename(columns={'key2': 'key'}, inplace=True)
print(ws.columns)
# ws.to_csv("weapon_subset_alien.csv", index=False)
ws.to_csv("weapon_set.csv", index=False)