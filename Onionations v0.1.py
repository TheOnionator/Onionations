import time
import math


class Nation:
    def __init__(self, name='', nation_id=0, current_research_id=0,
                 current_research_progress=0, if_at_war=False,

                 population_surplus=0, food_units=0, wood=0, stone=0, coal=0, metals=0, rare_earth_metals=0,
                 oil=0, bronze=0, iron=0, steel=0, concrete=0, gunpowder=0,
                 chemicals=0, electricity_production=0,

                 rock_thrower=0, spearman=0, basic_bronze_swordman=0,
                 bronze_cavalry=0, archer=0, basic_iron_swordman=0, iron_cavalry=0,
                 flame_archer=0, basic_pistoleer=0, basic_musketeer=0, cartridge_rifleman=0,
                 autorifleman=0, machine_gunner=0, rocket_specialist=0, basic_armored_personnel_carrier=0,
                 basic_tank=0, machine_gun_biplane=0, bomber_biplane=0, napalm_bomber_biplane=0,
                 mustard_gas_bomber_biplane=0, hwacha=0, hundred_kg_gunpowder_charge=0, tonne_gunpowder_charge=0,
                 ten_tonne_gunpowder_charge=0, basic_artillery_gun=0, basic_unguided_rocket_launcher=0, basic_bomb=0,
                 basic_napalm_bomb=0, basic_mustard_gas_bomb=0, mustard_gas_launcher=0):

        self.name = name
        self.nation_id = nation_id
        self.current_research_id = current_research_id
        self.current_research_progress = current_research_progress
        self.if_at_war = if_at_war
        self.population_surplus = population_surplus
        self.food_units = food_units
        self.wood = wood
        self.stone = stone
        self.coal = coal
        self.metals = metals
        self.rare_earth_metals = rare_earth_metals
        self.oil = oil
        self.bronze = bronze
        self.iron = iron
        self.steel = steel
        self.concrete = concrete
        self.gunpowder = gunpowder
        self.chemicals = chemicals
        self.electricity_production = electricity_production
        self.rock_thrower = rock_thrower
        self.spearman = spearman
        self.basic_bronze_swordman = basic_bronze_swordman
        self.bronze_cavalry = bronze_cavalry
        self.archer = archer
        self.basic_iron_swordman = basic_iron_swordman
        self.iron_cavalry = iron_cavalry
        self.flame_archer = flame_archer
        self.basic_pistoleer = basic_pistoleer
        self.basic_musketeer = basic_musketeer
        self.cartridge_rifleman = cartridge_rifleman
        self.autorifleman = autorifleman
        self.machine_gunner = machine_gunner
        self.rocket_specialist = rocket_specialist
        self.basic_armored_personnel_carrier = basic_armored_personnel_carrier
        self.basic_tank = basic_tank
        self.machine_gun_biplane = machine_gun_biplane
        self.bomber_biplane = bomber_biplane
        self.napalm_bomber_biplane = napalm_bomber_biplane
        self.mustard_gas_bomber_biplane = mustard_gas_bomber_biplane
        self.hwacha = hwacha
        self.hundred_kg_gunpowder_charge = hundred_kg_gunpowder_charge
        self.tonne_gunpowder_charge = tonne_gunpowder_charge
        self.ten_tonne_gunpowder_charge = ten_tonne_gunpowder_charge
        self.basic_artillery_gun = basic_artillery_gun
        self.basic_unguided_rocket_launcher = basic_unguided_rocket_launcher
        self.basic_bomb = basic_bomb
        self.basic_napalm_bomb = basic_napalm_bomb
        self.basic_mustard_gas_bomb = basic_mustard_gas_bomb
        self.mustard_gas_launcher = mustard_gas_launcher



class TileData:
    def __init__(self, cord_x, cord_y, hp=0, ownership=0, population=0, tile_type="empty",

                 rock_thrower=0, spearman=0, basic_bronze_swordman=0,
                 bronze_cavalry=0, archer=0, basic_iron_swordman=0, iron_cavalry=0,
                 flame_archer=0, basic_pistoleer=0, basic_musketeer=0, cartridge_rifleman=0,
                 autorifleman=0, machine_gunner=0, rocket_specialist=0, basic_armored_personnel_carrier=0,
                 basic_tank=0, machine_gun_biplane=0, bomber_biplane=0, napalm_bomber_biplane=0,
                 mustard_gas_bomber_biplane=0, hwacha=0, hundred_kg_gunpowder_charge=0, tonne_gunpowder_charge=0,
                 ten_tonne_gunpowder_charge=0, basic_artillery_gun=0, basic_unguided_rocket_launcher=0, basic_bomb=0,
                 basic_napalm_bomb=0, basic_mustard_gas_bomb=0, mustard_gas_launcher=0,

                 if_military_boolean=False, military_units_ownership=0, total_military_power=0,
                 if_battle_boolean=False, interaction_tile=0, attack_boolean=False, defense_boolean=False,
                 winning_boolean=False, losing_boolean=False, battle_duration_left=0,):

        self.cord_x = cord_x
        self.cord_y = cord_y
        self.hp = hp
        self.ownership = ownership
        self.population = population
        self.tile_type = tile_type
        self.rock_thrower = rock_thrower
        self.spearman = spearman
        self.basic_bronze_swordman = basic_bronze_swordman
        self.bronze_cavalry = bronze_cavalry
        self.archer = archer
        self.basic_iron_swordman = basic_iron_swordman
        self.iron_cavalry = iron_cavalry
        self.flame_archer = flame_archer
        self.basic_pistoleer = basic_pistoleer
        self.basic_musketeer = basic_musketeer
        self.cartridge_rifleman = cartridge_rifleman
        self.autorifleman = autorifleman
        self.machine_gunner = machine_gunner
        self.rocket_specialist = rocket_specialist
        self.basic_armored_personnel_carrier = basic_armored_personnel_carrier
        self.basic_tank = basic_tank
        self.machine_gun_biplane = machine_gun_biplane
        self.bomber_biplane = bomber_biplane
        self.napalm_bomber_biplane = napalm_bomber_biplane
        self.mustard_gas_bomber_biplane = mustard_gas_bomber_biplane
        self.hwacha = hwacha
        self.hundred_kg_gunpowder_charge = hundred_kg_gunpowder_charge
        self.tonne_gunpowder_charge = tonne_gunpowder_charge
        self.ten_tonne_gunpowder_charge = ten_tonne_gunpowder_charge
        self.basic_artillery_gun = basic_artillery_gun
        self.basic_unguided_rocket_launcher = basic_unguided_rocket_launcher
        self.basic_bomb = basic_bomb
        self.basic_napalm_bomb = basic_napalm_bomb
        self.basic_mustard_gas_bomb = basic_mustard_gas_bomb
        self.mustard_gas_launcher = mustard_gas_launcher
        self.if_military_boolean = if_military_boolean
        self.military_units_ownership = military_units_ownership
        self.total_military_power = total_military_power
        self.if_battle_boolean = if_battle_boolean
        self.interaction_tile = interaction_tile
        self.attack_boolean = attack_boolean
        self.defense_boolean = defense_boolean
        self.winning_boolean = winning_boolean
        self.losing_boolean = losing_boolean
        self.battle_duration_left = battle_duration_left



class TileType:
    def __init__(self, tile_type_name, tile_hp, tile_max_population, input_electricity=0, output_electricity=0,

                 input1='', input1n=0, input2='', input2n=0, input3='', input3n=0, input4='', input4n=0, input5='', input5n=0,
                 output='', output_n=0,
                 cost1='', cost1n=0, cost2='', cost2n=0, cost3='', cost3n=0):

        self.tile_type_name = tile_type_name
        self.tile_hp = tile_hp
        self.tile_max_population = tile_max_population
        self.input_electricity = input_electricity
        self.output_electricity = output_electricity
        self.input1 = input1
        self.input1n = input1n
        self.input2 = input2
        self.input2n = input2n
        self.input3 = input3
        self.input3n = input3n
        self.input4 = input4
        self.input4n = input4n
        self.input5 = input5
        self.input5n = input5n
        self.output = output
        self.output_n = output_n
        self.cost1 = cost1
        self.cost1n = cost1n
        self.cost2 = cost2
        self.cost2n = cost2n
        self.cost3 = cost3
        self.cost3n = cost3n



T1_Science_Lab = TileType("T1_Science_Lab", 1000, 1000, 0, 0, 'Wood', 20, 'Stone', 20, '', 0, '', 0, '', 0, 'T1_Science', 100,
                          'Wood', 2000, 'Stone', 2000)
T2_Science_Lab = TileType("T2_Science_Lab", 10000, 1000, 0, 0, 'Metals', 500, 'Coal', 500, 'Bronze', 100, '', 0, '', 0, 'T2_Science', 100,
                          'Metals', 50000, 'Coal', 50000, 'Bronze', 10000)
T3_Science_Lab = TileType("T3_Science_Lab", 100000, 1000, 0, 0, 'Coal', 10000, 'Bronze', 5000, 'Iron', 1000, '', 0, '', 0, 'T3_Science', 100,
                          'Coal', 1000000, 'Bronze', 500000, 'Iron', 100000)
T4_Science_Lab = TileType("T4_Science_Lab", 1000000, 1000, 1000, 0, 'Concrete', 100000, 'Steel', 10000, '', 0, '', 0, '', 0, 'T4_Science', 100,
                          'Concrete', 10000000, 'Steel', 1000000)
T1_Residential_Tile = TileType("T1_Residential_Tile", 200, 1000, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, '', 0,
                               'Wood', 10000, 'Stone', 10000)
T2_Residential_Tile = TileType("T2_Residential_Tile", 500, 5000, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, '', 0,
                               'Stone', 100000, 'Wood', 25000, 'Bronze', 5000)
T3_Residential_Tile = TileType("T3_Residential_Tile", 1000, 25000, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, '', 0,
                               'Stone', 1000000, 'Wood', 50000, 'Iron', 25000)
T4_Residential_Tile = TileType("T4_Residential_Tile", 2000, 100000, 500, 0, '', 0, '', 0, '', 0, '', 0, '', 0, '', 0,
                               'Concrete', 5000000, 'Steel', 100000)
T1_Farm_Tile = TileType("T1_Farm_Tile", 2000, 50, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, 'Food_Units', 1000,
                        'Wood', 8000, 'Stone', 2000)
T2_Farm_Tile = TileType("T2_Farm_Tile", 5000, 400, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, 'Food_Units', 10000,
                        'Stone', 50000, 'Wood', 20000, 'Bronze', 4000)
T3_Farm_Tile = TileType("T3_Farm_Tile", 10000, 2000, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, 'Food Units', 50000,
                        'Stone', 200000, 'Iron', 25000)
T4_Farm_Tile = TileType("T4_Farm_Tile", 20000, 10000, 200, 0, '', 0, '', 0, '', 0, '', 0, '', 0, 'Food Units', 250000,
                        'Concrete', 2000000, 'Steel', 50000)
T1_Resource_Wood_Tile = TileType("T1_Resource_Wood_Tile", 2000, 50, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, 'Wood', 50,
                                 'Wood', 8000, 'Stone', 4000)
T1_Resource_Stone_Tile = TileType("T1_Resource_Stone_Tile", 2000, 50, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Stone", 50,
                                  'Wood', 16000, 'Stone', 5000)
T1_Resource_Coal_Tile = TileType("T1_Resource_Coal_Tile", 2000, 100, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Coal", 25,
                                 'Wood', 20000, 'Stone', 10000)
T1_Resource_Metals_Tile = TileType("T1_Resource_Metals_Tile", 2000, 100, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Metals", 10,
                                   'Stone', 20000, 'Wood', 10000)
T2_Resource_Wood_Tile = TileType("T2_Resource_Wood_Tile", 5000, 200, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Wood", 500,
                                 'Stone', 25000, 'Wood', 40000, 'Bronze', 5000)
T2_Resource_Stone_Tile = TileType("T2_Resource_Stone_Tile", 5000, 200, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Stone", 500,
                                  "Wood", 80000, 'Stone', 20000, 'Bronze', 10000)
T2_Resource_Coal_Tile = TileType("T2_Resource_Coal_Tile", 5000, 400, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Coal", 250,
                                 "Wood", 100000, "Stone", 50000, "Bronze", 15000)
T2_Resource_Metals_Tile = TileType("T2_Resource_Metals_Tile", 5000, 500, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Metal", 100,
                                   "Stone", 100000, "Wood", 50000, "Bronze", 20000)
T3_Resource_Wood_Tile = TileType("T3_Resource_Wood_Tile", 10000, 800, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Wood", 2500,
                                 "Stone", 50000, "Wood", 50000, "Iron", 25000)
T3_Resource_Stone_Tile = TileType("T3_Resource_Stone_Tile", 10000, 800, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Stone", 2500,
                                  "Stone", 80000, "Wood", 40000, "Iron", 40000)
T3_Resource_Coal_Tile = TileType("T3_Resource_Coal_Tile", 10000, 2000, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Coal", 2000,
                                 "Stone", 20000, "Wood", 50000, "Iron", 50000)
T3_Resource_Metals_Tile = TileType("T3_Resource_Metals_Tile", 10000, 3000, 0, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Metals", 500,
                                   "Stone", 40000, "Iron", 80000)
T4_Resource_Wood_Tile = TileType("T4_Resource_Wood_Tile", 20000, 4000, 250, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Wood", 25000,
                                 "Concrete", 2500000, "Steel", 80000)
T4_Resource_Stone_Tile = TileType("T4_Resource_Stone_Tile", 20000, 4000, 250, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Stone", 25000,
                                  "Concrete", 2500000, "Steel", 80000)
T4_Resource_Coal_Tile = TileType("T4_Resource_Coal_Tile", 20000, 6000, 500, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Coal", 20000,
                                 "Concrete", 4000000, "Steel", 150000)
T4_Resource_Metals_Tile = TileType("T4_Resource_Metals_Tile", 20000, 10000, 800, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Metals", 10000,
                                   "Concrete", 5000000, "Steel", 250000)
T4_Resource_Rare_Earth_Metals_Tile = TileType("T4_Resource_Rare_Earth_Metals_Tile", 20000, 10000, 1000, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Rare_Earth_Metals", 1000,
                                              "Concrete", 5000000, "Steel", 250000)
T4_Resource_Oil_Tile = TileType("T4_Resource_Oil_Tile", 20000, 15000, 1000, 0, '', 0, '', 0, '', 0, '', 0, '', 0, "Oil", 8000,
                                "Concrete", 8000000, "Steel", 400000)
T2_Bronze_Factory = TileType("T2_Bronze_Factory", 5000, 500, 0, 0, 'Metals', 10, 'Coal', 25, '', 0, '', 0, '', 0, "Bronze", 10,
                             "Stone", 50000, "Wood", 25000, "Metals", 5000)
T3_Iron_Factory = TileType("T3_Iron_Factory", 10000, 2000, 0, 0, 'Metals', 100, 'Coal', 200, '', 0, '', 0, '', 0, "Iron", 20,
                           "Stone", 250000, "Wood", 50000, "Bronze", 20000)
T4_Coal_Power_Plant = TileType("T4_Coal_Power_Plant", 20000, 1000, 0, 10000, 'Coal', 10000, '', 0, '', 0, '', 0, '', 0, "", 0,
                               "Iron", 500000, "Stone", 500000)
T4_Large_Coal_Power_Plant = TileType("T4_Large_Coal_Power_Plant", 20000, 10000, 0, 2000000, 'Coal', 1000000, '', 0, '', 0, '', 0, '', 0, "", 0,
                                     "Concrete", 250000000, "Steel", 50000000)
T4_Concrete_Factory = TileType("T4_Concrete_Factory", 20000, 2000, 400, 0, 'Stone', 25000, 'Metals', 1000, '', 0, '', 0, '', 0, "Concrete", 25000,
                               "Stone", 1000000, "Iron", 100000)
T4_Steel_Factory = TileType("T4_Steel_Factory", 20000, 2000, 1000, 0, 'Metals', 20000, 'Coal', 5000, '', 0, '', 0, '', 0, "Steel", 5000,
                            "Concrete", 5000000, "Iron", 500000)
T4_Chemicals_Factory = TileType("T4_Chemicals_Factory", 20000, 4000, 800, 0, 'Oil', 8000, '', 0, '', 0, '', 0, '', 0, "Chemicals", 4000,
                                "Concrete", 10000000, "Steel", 1000000)
T4_Gunpowder_Factory = TileType("T4_Gunpowder_Factory", 20000, 5000, 800, 0, 'Coal', 5000, 'Chemicals', 2000, '', 0, '', 0, '', 0, 'Gunpowder', 4000,
                                "Concrete", 10000000, "Steel", 1000000)
T1_Rock_Military_Factory = TileType("T1_Rock_Military_Factory", 2000, 100, 0, 0, 'Stone', 100, '', 0, '', 0, '', 0, '', 0, "Rock", 10,
                                    "Stone", 10000, "Wood", 16000)
T1_Spear_Military_Factory = TileType("T1_Spear_Military_Factory", 2000, 200, 0, 0, 'Rock', 10, 'Wood', 10, '', 0, '', 0, '', 0, "Spear", 10,
                                     "Stone", 10000, "Wood", 16000)
T1_Rock_Thrower_Military_Factory = TileType("T1_Rock_Thrower_Military_Factory", 2000, 200, 0, 0, 'Rock', 10, 'Population', 2, '', 0, '', 0, '', 0, "Rock_Thrower", 2,
                                            "Wood", 30000, "Stone", 20000)
T1_Spear_Thrower_Military_Factory = TileType("T1_Spear_Thrower_Military_Factory", 2000, 300, 0, 0, 'Spear', 10, 'Population', 2, '', 0, '', 0, '', 0, "Spear_Thrower", 2,
                                             "Wood", 30000, "Stone", 20000)
T2_Bronze_Armor_Military_Factory = TileType("T2_Bronze_Armor_Military_Factory", 5000, 500, 0, 0, 'Bronze', 4, '', 0, '', 0, '', 0, '', 0, "Bronze_Armor", 1,
                                            "Stone", 40000, "Wood", 10000, "Bronze", 4000)
T2_Bronze_Sword_Military_Factory = TileType("T2_Bronze_Sword_Military_Factory", 5000, 500, 0, 0, 'Bronze', 4, '', 0, '', 0, '', 0, '', 0, "Bronze_Sword", 2,
                                            "Stone", 20000, "Wood", 5000, "Bronze", 2000)
T2_Bow_Military_Factory = TileType("T2_Bow_Military_Factory", 5000, 800, 0, 0, 'Wood', 200, 'Bronze', 20, '', 0, '', 0, '', 0, "Bow", 10,
                                   "Stone", 25000, "Wood", 20000, "Bronze", 2500)
T2_Bronze_Arrow_Military_Factory = TileType("T2_Bronze_Arrow_Military_Factory", 5000, 800, 0, 0, 'Wood', 100, 'Bronze', 50, '', 0, '', 0, '', 0, "Bronze_Arrow", 50,
                                            "Stone", 20000, "Wood", 5000, "Bronze", 2000)
T2_Basic_Bronze_Swordman_Military_Factory = TileType("T2_Basic_Bronze_Swordman_Military_Factory", 5000, 1000, 0, 0, 'Bronze_Armor', 1, 'Bronze_Sword', 2,
                                                     'Population', 1, '', 0, '', 0, "Bronze_Swordman", 1,
                                                     "Stone", 50000, "Wood", 10000, "Bronze", 5000)
T2_Bronze_Cavalry_Military_Factory = TileType("T2_Bronze_Cavalry_Military_Factory", 5000, 1000, 0, 0, 'Bronze_Armor', 4, 'Bronze_Sword', 4, 'Population', 4, '', 0, '', 0,
                                              "Bronze_Cavalry", 1,
                                              "Stone", 100000, "Wood", 20000, "Bronze", 10000)
T2_Bronze_Archer_Military_Factory = TileType("T2_Bronze_Archer_Military_Factory", 5000, 1000, 0, 0, 'Bow', 2, 'Bronze_Arrow', 10, 'Population', 2, '', 0, '', 0,
                                             "Bronze_Archer", 2,
                                             "Stone", 80000, "Wood", 10000, "Bronze", 10000)
T3_Iron_Armor_Military_Factory = TileType("T3_Iron_Armor_Military_Factory", 10000, 2000, 0, 0, 'Iron', 10, '', 0, '', 0, '', 0, '', 0, "Iron_Armor", 1,
                                          "Stone", 200000, "Iron", 20000)
T3_Iron_Sword_Military_Factory = TileType("T3_Iron_Sword_Military_Factor", 10000, 2000, 0, 0, 'Iron', 10, '', 0, '', 0, '', 0, '', 0, "Iron_Sword", 2,
                                          "Stone", 200000, "Iron", 20000)
T3_Torch_Arrow_Military_Factory = TileType("T3_Torch_Arrow_Military_Factory", 10000, 4000, 0, 0, 'Wood', 500, 'Coal', 200, '', 0, '', 0, '', 0, "Torch_Arrow", 100,
                                           "Stone", 400000, "Wood", 50000, "Iron", 40000)
T3_Iron_Swordman_Military_Factory = TileType("T3_Iron_Swordman_Military_Factory", 10000, 4000, 0, 0, 'Iron_Armor', 1, 'Iron_Sword', 2, 'Population', 1, '', 0, '', 0,
                                             "Iron_Swordman", 1,
                                             "Stone", 500000, "Iron", 50000)
T3_Iron_Cavalry_Military_Factory = TileType("T3_Iron_Cavalry_Military_Factory", 10000, 5000, 0, 0, 'Iron_Armor', 4, 'Iron_Sword', 4, 'Population', 4, '', 0, '', 0,
                                            "Iron Cavalry", 1,
                                            "Stone", 1000000, "Iron", 80000)
T3_Flame_Archer_Military_Factory = TileType("T3_Flame_Archer_Military_Factory", 10000, 4000, 0, 0, 'Bow', 2, 'Torch_Arrow', 10, 'Population', 2, '', 0, '', 0,
                                            "Flame_Archer", 2,
                                            "Stone", 800000, "Iron", 100000)
T3_Hwacha_Military_Factory = TileType("T3_Hwacha_Military_Factory", 10000, 4000, 0, 0, 'Torch_Arrow', 100, 'Iron', 80, '', 0, '', 0, '', 0, "Hwacha", 1,
                                      "Stone", 2000000, "Iron", 200000)
T4_Basic_Gunpowder_Pistol_Military_Factory = TileType("T4_Basic_Gunpowder_Pistol_Military_Factory", 20000, 8000, 500, 0, 'Gunpowder', 500, 'Steel', 200, '', 0, '', 0, '', 0,
                                                      "Basic_Gunpowder_Pistol", 2,
                                                      "Concrete", 2000000, "Steel", 100000)
T4_Basic_Gunpowder_Musket_Military_Factory = TileType("T4_Basic_Gunpowder_Musket_Military_Factory", 20000, 10000, 500, 0, 'Gunpowder', 1000, 'Steel', 400, '', 0, '', 0, '', 0,
                                                      "Basic_Gunpowder_Musket", 2,
                                                      "Concrete", 2000000, "Steel", 100000)
T4_Cartridge_Rifle_Military_Factory = TileType("T4_Cartridge_Rifle_Military_Factory", 20000, 10000, 1000, 0, 'Gunpowder', 1000, 'Steel', 500, '', 0, '', 0, '', 0,
                                               "Cartridge_Rifle", 1,
                                               "Concrete", 2000000, "Steel", 100000)
T4_Automatic_Rifle_Military_Factory = TileType("T4_Automatic_Rifle_Military_Factory", 20000, 20000, 2000, 0, 'Gunpowder', 2000, 'Steel', 1000, '', 0, '', 0, '', 0,
                                               "Automatic_Rifle", 2,
                                               "Concrete", 4000000, "Steel", 250000)
T4_Machine_Gun_Military_Factory = TileType("T4_Machine_Gun_Military_Factory", 20000, 30000, 4000, 0, 'Gunpowder', 4000, 'Steel', 2000, '', 0, '', 0, '', 0,
                                           "Machine_Gun", 1,
                                           "Concrete", 5000000, "Steel", 250000)
T4_Rocket_Launcher_Military_Factory = TileType("T4_Rocket_Launcher_Military_Factory", 20000, 40000, 8000, 0, 'Gunpowder', 8000, 'Steel', 4000, '', 0, '', 0, '', 0,
                                               "Rocket_Launcher", 1,
                                               "Concrete", 10000000, "Steel", 500000)
T4_Basic_Pistoleer_Military_Factory = TileType("T4_Basic_Pistoleer_Military_Factory", 20000, 10000, 1000, 0, 'Basic_Gunpowder_Pistol', 2, 'Population', 2, '', 0, '', 0, '', 0,
                                               "Basic_Pistoleer", 2,
                                               "Concrete", 4000000, "Steel", 250000)
T4_Basic_Musketeer_Military_Factory = TileType("T4_Basic_Musketeer_Military_Factory", 20000, 10000, 1000, 0, 'Basic_Gunpowder_Musket', 2, 'Population', 2, '', 0, '', 0, '', 0,
                                               "Basic_Musketeer", 2,
                                               "Concrete", 4000000, "Steel", 250000)
T4_Cartridge_Rifleman_Military_Factory = TileType("T4_Cartridge_Rifleman_Military_Factory", 20000, 20000, 2000, 0, 'Cartridge_Rifle', 1, 'Population', 1, '', 0, '', 0, '', 0,
                                                  "Cartridge_Rifleman", 1,
                                                  "Concrete", 4000000, "Steel", 250000)
T4_Autorifleman_Military_Factory = TileType("T4_Cartridge_Rifleman_Military_Factory", 20000, 30000, 4000, 0, 'Automatic_Rifle', 2, 'Population', 2, '', 0, '', 0, '', 0,
                                            "Autorifleman", 2,
                                            "Concrete", 10000000, "Steel", 500000)
T4_Machine_Gunner_Military_Factory = TileType("T4_Machine_Gunner_Military_Factory", 20000, 40000, 8000, 0, 'Machine_Gun', 1, 'Population', 1, '', 0, '', 0, '', 0,
                                              "Machine_Gunner", 1,
                                              "Concrete", 1000000, "Steel", 500000)
T4_Rocket_Specialist_Military_Factory = TileType("T4_Rocket_Specialist_Military_Factory", 20000, 50000, 16000, 0, 'Rocket_Launcher', 1, 'Population', 1, '', 0, '', 0, '', 0,
                                                 "Rocket_Specialist", 1,
                                                 "Concrete", 10000000, "Steel", 500000)
T4_Basic_Armored_Personnel_Carrier_Military_Factory = TileType("T4_Basic_Armored_Personnel_Carrier_Military_Factory", 20000, 100000, 50000, 0,
                                                               'Oil', 4000, 'Steel', 10000, '', 0, '', 0, '', 0,
                                                               "Basic_Armored_Personnel_Carrier", 1,
                                                               "Concrete", 15000000, "Steel", 800000)
T4_Basic_Tank_Military_Factory = TileType("T4_Basic_Tank_Military_Factory", 20000, 100000, 100000, 0, 'Oil', 10000, 'Steel', 40000, '', 0, '', 0, '', 0,
                                          "Basic_Tank", 1,
                                          "Concrete", 20000000, "Steel", 1000000)
T4_Machine_Gun_Biplane_Military_Factory = TileType("T4_Machine_Gun_Biplane_Military_Factory", 20000, 200000, 250000, 0,
                                                   'Oil', 16000, 'Steel', 20000, '', 0, '', 0, '', 0,
                                                   "Machine_Gun_Biplane", 1,
                                                   "Concrete", 30000000, "Steel", 1000000)
T4_Bomber_Biplane_Military_Factory = TileType("T4_Bomber_Biplane_Military_Factory", 20000, 200000, 250000, 0,
                                              'Basic_Bomb', 10, 'Oil', 16000, 'Steel', 20000, '', 0, '', 0,
                                              "Bomber_Biplane", 1,
                                              "Concrete", 30000000, "Steel", 1000000)
T4_Napalm_Bomber_Biplane_Military_Factory = TileType("T4_Napalm_Bomber_Biplane_Military_Factory", 20000, 200000, 250000, 0,
                                                     'Napalm_Bomb', 10, 'Oil', 16000, 'Steel', 20000, '', 0, '', 0,
                                                     "Napalm_Bomber_Biplane", 1,
                                                     "Concrete", 30000000, "Steel", 1000000)
T4_Mustard_Gas_Bomber_Biplane_Military_Factory = TileType("T4_Mustard_Gas_Bomber_Biplane_Military_Factory", 20000, 200000, 250000, 0,
                                                          'Mustard_Gas_Bomb', 10, 'Oil', 16000, 'Steel', 20000, '', 0, '', 0,
                                                          "Mustard_Gas_Bomber_Biplane", 1,
                                                          "Concrete", 30000000, "Steel", 1000000)
T4_100kg_Gunpowder_Charge_Military_Factory = TileType("T4_100kg_Gunpowder_Charge_Military_Factory", 20000, 100000, 10000, 0,
                                                      'Gunpowder', 5000, 'Steel', 1000, '', 0, '', 0, '', 0,
                                                      "100kg_Gunpowder_Charge", 1,
                                                      "Concrete", 5000000, "Steel", 100000)
T4_1000kg_Gunpowder_Charge_Military_Factory = TileType("T4_1000kg_Gunpowder_Charge_Military_Factory", 20000, 1000000, 100000, 0,
                                                       'Gunpowder', 50000, 'Steel', 10000, '', 0, '', 0, '', 0,
                                                       "1000kg_Gunpowder_Charge_Military_Factory", 1,
                                                       "Concrete", 50000000, "Steel", 1000000)
T4_10000kg_Gunpowder_Charge_Military_Factory = TileType("T4_10000kg_Gunpowder_Charge_Military_Factory", 20000, 10000000, 1000000, 0,
                                                        'Gunpowder', 500000, 'Steel', 100000, '', 0, '', 0, '', 0,
                                                        "10000kg_Gunpowder_Charge", 1,
                                                        "Concrete", 500000000, "Steel", 10000000)
T4_Basic_Artillery_Gun_Military_Factory = TileType("T4_Basic_Artillery_Gun_Military_Factory", 20000, 1000000, 250000, 0,
                                                   'Gunpowder', 250000, 'Steel', 100000, '', 0, '', 0, '', 0,
                                                   "Basic_Artillery_Gun", 1,
                                                   "Concrete", 40000000, "Steel", 2000000)
T4_Basic_Unguided_Rocket_Launcher_Military_Factory = TileType("T4_Basic_Unguided_Rocket_Launcher_Military_Factory", 20000, 1000000, 2000000, 0,
                                                              'Gunpowder', 1000000, 'Steel', 500000, '', 0, '', 0, '', 0,
                                                              "Basic_Unguided_Rocket_Launcher", 1,
                                                              "Concrete", 100000000, "Steel", 5000000)
T4_Basic_Bomb_Military_Factory = TileType("T4_Basic_Bomb_Military_Factory", 20000, 100000, 50000, 0, 'Gunpowder', 1000, 'Steel', 1000, '', 0, '', 0, '', 0,
                                          "Basic_Bomb", 1,
                                          "Concrete", 50000000, "Steel", 1000000)
T4_Basic_Napalm_Bomb_Military_Factory = TileType("T4_Basic_Napalm_Bomb_Military_Factory", 20000, 100000, 50000, 0, 'Oil', 4000, 'Gunpowder', 1000, 'Steel', 1000, '', 0, '', 0,
                                                 "Basic_Napalm_Bomb", 1,
                                                 "Concrete", 50000000, "Steel", 1000000)
T4_Basic_Mustard_Gas_Bomb_Military_Factory = TileType("T4_Basic_Mustard_Gas_Bomb_Military_Factory", 20000, 100000, 50000, 0,
                                                      'Chemicals', 8000, 'Gunpowder', 1000, 'Steel', 1000, '', 0, '', 0,
                                                      "Basic_Mustard_Gas_Bomb", 1,
                                                      "Concrete", 50000000, "Steel", 1000000)
T4_Mustard_Gas_Launcher_Military_Factory = TileType("T4_Mustard_Gas_Launcher_Military_Factory", 20000, 2000000, 1000000, 0,
                                                    'Chemicals', 1000000, 'Gunpowder', 100000, 'Steel', 50000, '', 0, '', 0,
                                                    "Concrete", 5000000, "Steel", 1000000)





Loading_Screen = True
Dimensions = 4000
Year = -10000
Day = 1
Map = {}
Nations_Tile_List = [[], []]
Nations_War_List = []

Onionation = Nation("Onionation")
Onionation.nation_id = 1


def generate_map(dim, map_dict):
    n = 1
    start_time = time.time()
    time_list = [time.time() - start_time]
    avg_list = []
    Sum = 0
    for x in range(dim):
        for y in range(dim):
            if n % math.floor(dim**2/1000) == 0:
                time_list.append(round((time.time() - start_time), 6))
                if Loading_Screen:
                    print((n/10)/(dim**2/1000), "%")
                    print(round((time.time() - start_time), 9), " Time Elapsed")
                    print(round((time_list[-1] - time_list[-2]), 9), " 0.1% Time")
                avg_list.append(round((time_list[-1] - time_list[-2]), 6))
                for a in avg_list:
                    Sum += a
                avg = Sum/len(avg_list)
                if Loading_Screen:
                    print(f'{avg:.9f}', " Avg 0.1% Time")
                    print("Estimated Total Time ", round((avg*1000), 2), "s")
                    print("Estimated Time Left ", round((avg*1000 - Sum), 3), "s")


                Sum = 0
            tile_name = ("tile_x{}".format(x)+"_y{}".format(y))
            map_dict[tile_name] = map_dict.get(tile_name, TileData(cord_x=x, cord_y=y))
            n += 1

    gen_speed = math.floor((dim**2) / round((time.time() - start_time), 9))
    max_60s_dim = math.floor(math.sqrt(gen_speed*60))

    print("")
    print(f"{gen_speed:,d}", "Tiles/s")
    print("60s Max Suggested Dimensions -", max_60s_dim, "x", max_60s_dim, " ", (round((max_60s_dim**2 / 10000**2), 6) * 100), "% of Full Size Map")
    print("Map Generation Finished  ", f"{dim**2:,d}", "Tiles Generated  ", dim, "x", dim)








generate_map(Dimensions, Map)


