#!/usr/bin/python3

character_dict = {
      'Stats': {
          'strength':{
              'base':0,
              'mod':0,
              'save':0
          },
          'dexterity':{ 
              'base':0,
              'mod':0,
              'save':0
          },
          'constitution':{
              'base': 0,
              'mod':0,
              'save':0
          },
          'intelligence':{
              'base': 0,
              'mod':0,
              'save':0
          },
          'wisdom' :{
               'base': 0,
               'mod':0,
               'save':0
          },
          'charisma' :{
               'base': 0,
               'mod':0,
               'save':0
      },
   },
    "Languages":[
        'Common',
    ],
    "name":[
    ],
    "player_class":[
    ],
    "Tools":[
    ],
    "spell_attack":[
    ],
    "spell_save":[
    ],
    "speed":[
    ],
# In case a race is added that has a climbing, swimming, or flying speed
    "climb_speed":[
    ],
    "swim_speed":[
    ],
    "fly_speed":[
    ],
    "size":[
    ],
    "Kits":[
    ],
    "hp":[
    ],
    "hit_dice":[
    ],
# Hit Dice
    "d6":[
    ],
    "d8":[
    ],
    "d10":[
    ],
    "d12":[
    ],
    "Vehicles":[
    ],
    "race":[
    ],
    "background":[
    ],
    "Instruments":[
    ],
    "Gaming_Set":[
    ],
#Weapon Proficiencies
    "Weapon_Prof":[

    ],
#Armor Proficiencies
    "Armor_Prof":[
    ],
    "armor_class":[
    ],
    "passive_perception":[
    ],
#Cantrips for magic
    "cantrip":[
    ],
#1st level spells
    "first_level":[
    ],
    "gold":[
    ],
    "Equipment":[
    ],
#Misc items given in backgrounds
    "Misc":[
    ],
    "features":[
    ]
}

# Sets all of the hit dice to 0 so they can be added to in the player classes.
def set_hit_dice():
    character_dict['d6']=0
    character_dict['d8']=0
    character_dict['d10']=0
    character_dict['d12']=0
    
