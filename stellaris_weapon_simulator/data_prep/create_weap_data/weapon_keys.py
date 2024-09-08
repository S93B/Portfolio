key_data = """
Red Laser
Red Laser
Red Laser
Blue Laser
Blue Laser
Blue Laser
Uv Laser
Uv Laser
Uv Laser
Xray Laser
Xray Laser
Xray Laser
Gamma Laser
Gamma Laser
Gamma Laser
Mass Driver
Mass Driver
Mass Driver
Coilgun
Coilgun
Coilgun
Railgun
Railgun
Railgun
Advanced Railgun
Advanced Railgun
Advanced Railgun
Gauss Cannon
Gauss Cannon
Gauss Cannon
Plasma Thrower
Plasma Thrower
Plasma Thrower
Plasma Accelerator
Plasma Accelerator
Plasma Accelerator
Plasma Cannon
Plasma Cannon
Plasma Cannon
Disruptor
Disruptor
Ion Disruptor
Ion Disruptor
Phase Disruptor
Phase Disruptor
Autocannon
Autocannon
Autocannon
Ripper Autocannon'
Ripper Autocannon'
Ripper Autocannon'
Stormfire Autocannon
Stormfire Autocannon
Stormfire Autocannon
Nanite Autocannon
Nanite Autocannon
Nanite Autocannon
Kinetic Artillery 1
Kinetic Artillery 2
Proton Launcher
Neutron Launcher
Mega Cannon
Giga Cannon
Particle Lance
Tachyon Lance
Arc Emitter
Focused Arc Emitter
Titan Laser
Perdition Beam Titan
Flak Battery
Flak Cannons
Flak Artillery
Nanite Flak Battery
Sentinel Point-Defense
Barrier Point-Defense
Guardian Point-Defense
Nuclear Missiles
Fusion Missiles
Antimatter Missiles
Quantum Missiles
Marauder Missiles
Space Torpedoes
Armored Torpedoes
Devastator Torpedoes
Swarmer Missiles
Whirlwind Missiles
Ancient Cavitation Collapser
Ancient Cavitation Collapser
Ancient Cavitation Collapser
Ancient Macro Batteries
Ancient Macro Batteries
Ancient Macro Batteries
Ancient Defensive Web Slinger
Nano-Missile Cloud Launcher
Ancient Ruination Glare
Ancient Ruination Glare
Ancient Saturator Artillery
"""

list_craft = (
    """'Scout Wing
Basic Strike Craft
Improve Strike Craft
Advanced Strike Craft
"""
    ""
)

# Convert the  string to a list
key_list = key_data.strip().split("\n")


# create columns for tier, size and technology
weapon_type_name = {
    "laser": "energy",
    "mass_driver": "kinetic",
    "accelerator": "kinetic",
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
    "perdition": "energy",
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
    "flak": "P",
    "point": "P",
    "ARCHAEO_X": "XL",
}
weapon_tier_list = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
