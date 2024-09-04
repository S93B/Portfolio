class Ship:
    def __init__(self, dataframe):
        self.ship = None
        self.dataframe = dataframe
        self.name = ""
        self.shield = 0
        self.armor = 0
        self.hull = 0
        self.base_speed = 0
        self.base_evasion = 0
        self.armor_regen = 0

    def select_row_by_key(self, key):
        self.ship = self.dataframe.loc[key]
        self.name = self.ship["type"]
        self.hull = self.ship["base hull"]
        self.shield = self.ship["shield_average"]
        self.armor = self.ship["armor_average"]
        self.shield_regen = self.ship["regen"]
        if self.ship["armor_regen"] >= 1:
            self.armor_regen = self.ship["armor_regen"]
        self.base_speed = self.ship["base speed"]
        self.base_evasion = self.ship["base evasion"]
