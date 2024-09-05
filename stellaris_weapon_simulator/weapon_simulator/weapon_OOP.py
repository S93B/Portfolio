
class Weapon:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.weapon = 0
        self.min_damage = 0
        self.max_damage = 0
        self.accuracy = 0
        self.tracking = 0
        self.n = ""
        self.cooldown = 0
        self.range = 0
        self.avg_dmg_range = 0
        self.hull_modifier = 0
        self.armor_modifier = 0
        self.shield_modifier = 0
        self.size = ""
        self.shield_penetration = False
        self.armor_penetration = False
        self.size_multiplier = False

    def select_row_by_key(self, key):
        self.weapon = self.dataframe.loc[key]
        self.cooldown = self.weapon["cooldown"]
        if self.weapon["size"] == "G":
            self.size_multiplier = True
        self.n = self.weapon.name
        self.min_damage = self.weapon["min_damage"]
        self.max_damage = self.weapon["max_damage"]
        self.accuracy = self.weapon["accuracy"]
        self.avg_dmg_range = (self.weapon["min_damage"], self.weapon["max_damage"])
        self.hull_modifier = self.weapon["hull_damage"]
        self.armor_modifier = self.weapon["armor_damage"]
        self.shield_modifier = self.weapon["shield_damage"]
        self.tracking = self.weapon["tracking"]
        if self.weapon["shield_penetration"] == 1.0:
            self.shield_penetration = True
        if self.weapon["armor_penetration"] == 1.0:
            self.armor_penetration = True

    def select_columns(self, columns):
        return self.dataframe.loc[columns]

    def select_rows_by_index(self, index):
        self.weapon = self.dataframe.loc[index]
        self.n = self.weapon.key
        self.size = self.weapon["size"]
        # if self.weapon["size"] == "G":
        #     self.size_multiplier = True
        self.cooldown = self.weapon["cooldown"]
        self.min_damage = self.weapon["min_damage"]
        self.max_damage = self.weapon["max_damage"]
        self.accuracy = self.weapon["accuracy"]
        self.avg_dmg_range = (self.weapon["min_damage"], self.weapon["max_damage"])
        self.hull_modifier = self.weapon["hull_damage"]
        self.armor_modifier = self.weapon["armor_damage"]
        self.shield_modifier = self.weapon["shield_damage"]
        self.tracking = self.weapon["tracking"]
        if self.weapon["shield_penetration"] == 1.0:
            self.shield_penetration = True
        else:
            self.shield_penetration = False
        if self.weapon["armor_penetration"] == 1.0:
            self.armor_penetration = True
        else:
            self.armor_penetration = False

    def select_rows_by_condition(self, condition):
        return self.dataframe[condition]
