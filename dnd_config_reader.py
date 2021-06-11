#import dnd_config_reader
import dnd_dict
from configparser import ConfigParser
#from argparse import ConfigParser

config = ConfigParser()
config.read("dnd_config.ini")

# check keys
key_check = config['Player_Values'].keys()
for k in key_check:
    if k not in dnd_dict.character_dict.keys():
        print(f'The following key is borked: {k}')
        exit()

Race, Background, Player_Class = config['Player_Values'].values()

accept_list_race = ['Dragonborn', 'Hill Dwarf', 'Mountain Dwarf', 'High Elf', 'Wood Elf', 'Forest Gnome', 'Rock Gnome', 'Half-Elf', 'Lightfoot Halfling', 'Stout Halfling', 'Half-Orc', 'Human', 'Tiefling', 'None']
accept_list_background =['Acolyte', 'Anthropologist', 'Archeologist', 'Charlatan', 'City Watch', 'Cloistered Scholar', 'Criminal', 'Entertainer', 'Far Traveler', 'Folk Hero', 'Gladiator', 'Guild Artisan', 'Guild Merchant', 'Haunted One', 'Hermit', 'Inquisitor', 'Investigator', 'Knight', 'Marine', 'Mercenary', 'Noble', 'Outlander', 'Pirate', 'Sage', 'Sailor', 'Soldier', 'Spy', 'Urban Bounty Hunter', 'Urchin', 'None']
accept_list_class = ['Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', 'None']

if Race not in accept_list_race:
    print("Error in Race key")
    exit()

if Background not in accept_list_background:
    print("Error in Background key")
    exit()

if Player_Class not in accept_list_class:
    print("Error in Player Class key")
    exit()


def config_race(**kwargs):
    for key, value in kwargs.items():
# Put the items in a list so it is easier to append with certain classes
        new_list = [value]
        dnd_dict.character_dict[key] = new_list


# Lower Case is the dictionary in dnd_dict, Upper Case is the value from the
# user input
config_race(race=Race,background=Background,player_class=Player_Class)
