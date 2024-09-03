import numpy as np
import pandas as pd
from main.weapon_simulator.weapon_object import *
from main.ship_data.ships_OOP import *
ws = pd.read_csv("C:\Python homedirectory\portfolio_stellaris\main\create_weap_data\weapon_set.csv", delimiter=',', skiprows=0)
scol = pd.read_csv("C:\Python homedirectory\portfolio_stellaris\main\ship_data\ship_col.csv", delimiter=',')

# SHIP CHOICE
ship = Ship(scol)
ss = Weapon(ws)
ship_multiplier = 9 #size multipliers zijn; 2x corvette; 3x destroyer; 5x cruiser; 9x battleship

# Simulation parameters; primarily used for single weapon testing
num_simulations = 1


# Function to calculate time to deplete defenses
def calculate_time(name, damage_range, cooldown, accuracy, tracking, num_simulations, shields, armor, hull):
    #Function to calculate how long it takes for a chosen weapon to destroy to specified ship.
    total_dmg = {
        "name": ss.n,
        "size": ss.size,
        "shield": 0,
        "armor": 0,
        "hull": 0,
        "total shots": 0,
        "hits": 0,
        "seconds": 0
    }
    total_times = []
    loop = 0
    for _ in range(num_simulations):
        shields = ship.shield
        armor = ship.armor
        hull = ship.hull
        evasion = ship.base_evasion
        armor_regen = ship.armor_regen
        loop = 0
        while hull > 0:
            loop +=1
            if loop == 10000:
                return print(f" {ss.n} size {ss.size} unable to destroy {ship.name} within 10k shots")
            hits = np.random.rand() < accuracy - (evasion - tracking)  # Determine if the shot hits
            if hits and ss.size == "G":
                dmg_per_shot = (np.random.uniform(*damage_range)) * ship_multiplier
                total_dmg["hits"] += 1
            elif hits:
                dmg_per_shot = (np.random.uniform(*damage_range))
                total_dmg["hits"] += 1
            else:
                dmg_per_shot = 0  # Missed shot
            total_dmg["total shots"] += 1
            dps = dmg_per_shot
            # Calculate damage to each defense type
            ##reset dmg values for loop
            shield_dmg = 0
            armor_dmg = 0
            hull_dmg = 0
            if shields < ship.shield:
                 shields += (ship.shield_regen * cooldown)
                 if shields > ship.shield:
                     shields = ship.shield
            if armor < ship.armor:
                armor += (armor_regen * cooldown)
                if armor > ship.armor:
                    armor = ship.armor
            if hull < ship.hull:
                hull += (ship.armor_regen * cooldown)
                if hull > ship.hull:
                    hull = ship.hull
            # Calculate damage to each defense type
            shield_dmg = dps * ss.shield_modifier
            armor_dmg = dps * ss.armor_modifier
            hull_dmg = dps * ss.hull_modifier
            if shields <= 0:
                shield_dmg = 0
            if shield_dmg > shields:
                armor_dmg = ((shield_dmg - shields) / ss.shield_modifier) * ss.armor_modifier
            if armor <= 0:
                armor_dmg = 0
            if ss.shield_penetration == False:
                shields = shields - shield_dmg
                total_dmg["shield"] += round(shield_dmg)
                #Time to deplete armor
            if ss.armor_penetration == False:
                if shields <= 0:
                    armor = armor - armor_dmg
                    total_dmg["armor"] += round(armor_dmg)
                    if armor <= 0:
                        # Time to deplete hull
                        hull = hull - hull_dmg
                        total_dmg["hull"] += round(hull_dmg)
                    if hull <= 0:
                        # Total time
                        total_time = round(total_dmg["total shots"] * cooldown)
                        total_times.append(total_time)
            if ss.shield_penetration and ss.armor_penetration: # if shield pen and armor pen are true
                hull = hull - hull_dmg
                total_dmg["hull"] += round(hull_dmg)
                if hull <= 0:
                    # Total time
                    total_time = round( total_dmg["total shots"] * cooldown)
                    total_times.append(total_time)
            elif ss.shield_penetration and ss.armor_penetration == False: #if shield pen is true but armor pen is not
                armor = armor - armor_dmg
                total_dmg["armor"] += round(armor_dmg)
                if armor <= 0:
                    # Time to deplete hull
                    hull = hull - hull_dmg
                    total_dmg["hull"] += round(hull_dmg)
                    if hull <= 0:
                        # Total time
                        total_time = round(total_dmg["total shots"] * cooldown)
                        total_times.append(total_time)
    total_times = sum(total_times) / num_simulations
    total_dmg["total shots"] = total_dmg["total shots"] / num_simulations
    total_dmg["hits"] = total_dmg["hits"] / num_simulations
    total_dmg["seconds"] = total_times
    total_dmg["name"] = ss.n
    #print(f"{total_times} seconds total by {ss.n} size {ss.size} to destroy {ship.name}\n")
    #print(total_dmg)
    total_dmg = pd.DataFrame(total_dmg, index=[0])
    return total_dmg

#bij specifieke selectie wapens
list_w_against_battleship = [14, 29, 38, 44, 53, 58, 60, 62, 64, 66, 67, 68, 81,84,86, 95]
list_best_w = [12,13,14,27,28,29,36,37,38,43,44,51,52,53,54,55,56,58,60,62,64,66,67,68,81,84,86,95]
list_w_against_all = range(0, 97)
weapon_S_sizes = ws[ws["size"] == "S"]
weapon_S_sizes = weapon_S_sizes.reset_index(drop=True)
weapon_M_sizes = ws[ws["size"] == "M"]
weapon_L_sizes = ws[ws["size"] == "L"]

end_list = pd.DataFrame()

#Kies een schip om op te schieten TODO: maak het een input vraag met uitleg
ship_list = [4]
for i in ship_list:
    ship.select_row_by_key(i)
    #selecteer wapenlijst
    for num in list_w_against_all:
        ss.select_rows_by_index(num)
        kinetic_times = calculate_time(ss.n, ss.avg_dmg_range, ss.cooldown, ss.accuracy, ss.tracking, num_simulations,
                                           ship.shield, ship.armor, ship.hull)
        end_list = pd.concat([end_list, kinetic_times], ignore_index=True)
end_list.set_index("name", inplace=True)
#print(end_list)
end_list.to_csv("C:\Python homedirectory\portfolio_stellaris\main\data_ttk\data_ttk.csv")