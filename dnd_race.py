#!/usr/bin/python3
import os, math, dnd_features, dnd_class, dnd_dict, dnd_skills, dnd_language, dnd_magic

def dragonborn():

#Use RaceStats class and racial_bonus method to increase Strength by 2
    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("strength").get("base"), 2)
 
#Use RaceStats class and racial_bonus method to increase Charisma by 1
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("charisma").get("base"),1)
    dnd_dict.character_dict['Stats']['strength']['base'] = race1
    dnd_dict.character_dict['Stats']['charisma']['base'] = race2


#Define race, movement speed, size, and language known
    dnd_class.RaceStats.racial_choice("Dragonborn", 30, "Medium")
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Dragonborn")
    dnd_dict.character_dict.get("speed").append("30")
    dnd_dict.character_dict.get("size").append("Medium")

#Update Stats to Dictionary

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6


# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)

#Put a new language into the Language dictionary
    dnd_dict.character_dict.get("Languages").append("Draconic")

    dnd_features.dragonborn_features()

    dnd_skills.set_skill()

def dwarf_hill():

# Increase the base stats (constitution and wisdom) from the dictionary
    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("constitution").get("base"), 2)
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("wisdom").get("base"),1)

#Update Stats to Dictionary
    dnd_dict.character_dict['Stats']['constitution']['base'] = race1
    dnd_dict.character_dict['Stats']['wisdom']['base'] = race2


    dnd_class.RaceStats.racial_choice("Hill Dwarf", 25, "Small")
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Hill Dwarf")
    dnd_dict.character_dict.get("speed").append("25")
    dnd_dict.character_dict.get("size").append("Small")
    dnd_dict.character_dict.get("Languages").append("Dwarvish")


#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get('constitution').get('mod'),1)
    dnd_dict.character_dict.get('hp').append(hit_points)


    while True:
        choice = input("Select the artisan's tools you want proficiency in:\n1) Smith's Tools\n2) Brewer's Supplies\n3) Mason's Tools\nEnter your selection: ")
   
        if choice == '1':
            dnd_dict.character_dict.get("Tools").append('Smith\'s Tools')
            break

        elif choice == '2':
            dnd_dict.character_dict.get("Tools").append('Brewer\'s Tools')
            break

        elif choice == '3':
            dnd_dict.character_dict.get("Tools").append('Mason\'s Tools')
            break

        else:
            print("Invalid Selection")
            continue

    dnd_skills.set_skill()

    print("• Dwarven Combat Training. You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.")

    dwarf_weapon = ['Battleaxes','Handaxes','Light Hammers','Warhammers']
    dnd_dict.character_dict.get("Weapon_Prof").append(dwarf_weapon)


    dnd_features.dwarf_hill_features()

def dwarf_mountain():
# Increase the base stats (constitution and strength) from the dictionary
    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("constitution").get("base"), 2)
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("strength").get("base"),2)
#Update Stats to Dictionary
    dnd_dict.character_dict['Stats']['constitution']['base'] = race1
    dnd_dict.character_dict['Stats']['wisdom']['base'] = race2

    dnd_class.RaceStats.racial_choice("Mountain Dwarf", 25, "Small")
    dnd_dict.character_dict.get("Languages").append('Dwarvish')
    dnd_dict.character_dict.get("speed").append("25")
    dnd_dict.character_dict.get("size").append("Small")
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Mountain Dwarf")


#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)
    print(dnd_dict.character_dict.get('hp'))

    while True:
        choice = input("Select the artisan's tools you want proficiency in:\n1) Smith's Tools\n2) Brewer's Supplies\n3) Mason's Tools\nEnter your selection: ")
   
        if choice == '1':
            dnd_dict.character_dict.get("Tools").append('Smith\'s Tools')
            break

        elif choice == '2':
            dnd_dict.character_dict.get("Tools").append('Brewer\'s Tools')
            break

        elif choice == '3':
            dnd_dict.character_dict.get("Tools").append('Mason\'s Tools')
            break

        else:
            print("Invalid Selection")
            continue


    dnd_skills.set_skill()

    print("• Dwarven Combat Training. You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.")

    dwarf_weapon = ['Battleaxes','Handaxes','Light Hammers','Warhammers']
    dnd_dict.character_dict.get("Weapon_Prof").append(dwarf_weapon)


    dnd_features.dwarf_mountain_features()

def elf_high():
    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("dexterity").get("base"), 2)
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("intelligence").get("base"),1)

    dnd_dict.character_dict['Stats']['dexterity']['base'] = race1
    dnd_dict.character_dict['Stats']['intelligence']['base'] = race2

    dnd_language.elf_lang()

    dnd_class.RaceStats.racial_choice("High Elf", 30, "Medium")
    dnd_dict.character_dict.get("speed").append("30")
    dnd_dict.character_dict.get("size").append("Medium")
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"High Elf")
    dnd_dict.character_dict.get("Languages").append('Elven')


#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)

    print("""Elf Weapon Training. You have proficiency with the longsword, shortsword, shortbow, and longbow.
• Keen Senses. You have proficiency in the Perception skill.""")

    elf_weapon_prof = ['Longswords', 'Shortswords', 'Shortbows', 'Longbows']
    dnd_dict.character_dict.get("Weapon_Prof").append(elf_weapon_prof)

    dnd_skills.set_skill()
    dnd_magic.wizard_cantrip()

#   Proficiency with Perception
    dnd_skills.perception_prof() 

    dnd_features.elf_features()

def elf_wood():

    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("dexterity").get("base"), 2)
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("wisdom").get("base"),1)

    dnd_dict.character_dict['Stats']['dexterity']['base'] = race1
    dnd_dict.character_dict['Stats']['wisdom']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

    dnd_class.RaceStats.racial_choice("Wood Elf", 35, "Medium")
    dnd_dict.character_dict.get("speed").append("30")
    dnd_dict.character_dict.get("size").append("Medium")
    dnd_dict.character_dict.get("Languages").append('Elven')
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Wood Elf")

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)

    dnd_skills.set_skill()
    dnd_skills.perception_prof() 
    

    print("""Elf Weapon Training. You have proficiency with the longsword, shortsword, shortbow, and longbow.
• Keen Senses. You have proficiency in the Perception skill.""")

    elf_weapon_prof = ['Longswords', 'Shortswords', 'Shortbows', 'Longbows']
    dnd_dict.character_dict.get("Weapon_Prof").append(elf_weapon_prof)
    dnd_skills.perception_prof() 

    dnd_features.elf_features()


def gnome_forest():

    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("intelligence").get("base"), 2)
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("dexterity").get("base"),1)

    dnd_dict.character_dict['Stats']['intelligence']['base'] = race1
    dnd_dict.character_dict['Stats']['dexterity']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Forest Gnome", 25, "Small")
    dnd_dict.character_dict.get("speed").append("25")
    dnd_dict.character_dict.get("size").append("Small")
    dnd_dict.character_dict.get("Languages").append('Gnomish')
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Forest Gnome")
    dnd_dict.character_dict.get("cantrip").append("Minor Illusion")

    dnd_features.gnome_forest_features()

def gnome_rock():

    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("intelligence").get("base"), 2)
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("constitution").get("base"),1)

    dnd_dict.character_dict['Stats']['intelligence']['base'] = race1
    dnd_dict.character_dict['Stats']['constitution']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Rock Gnome", 25, "Small")
    dnd_dict.character_dict.get("speed").append("25")
    dnd_dict.character_dict.get("size").append("Small")
    dnd_dict.character_dict.get("Languages").append('Gnomish')
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Rock Gnome")

    dnd_features.gnome_rock_features()

def half_elf():

# Increase Charisma score by 2
    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("charisma").get("base"), 2)
    dnd_dict.character_dict['Stats']['charisma']['base'] = race1

# Choose 2 stats (not counting charisma) to increase by 1
    while True:
        choice1 = input("Select the first stat you want to improve:\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\nEnter your Selection: ")
        if choice1=='1':                    
            race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("strength").get("base"), 1)
            dnd_dict.character_dict['Stats']['strength']['base'] = race2
            break
 
        elif choice1=='2':
            race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("dexterity").get("base"), 1)
            dnd_dict.character_dict['Stats']['dexterity']['base'] = race2
            break
 
        elif choice1=='3':
            race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("constitution").get("base"), 1)
            dnd_dict.character_dict['Stats']['constitution']['base'] = race2
            break
 
        elif choice1=='4':
            race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("intelligence").get("base"), 1)
            dnd_dict.character_dict['Stats']['intelligence']['base'] = race2
            break
 
        elif choice1=='5':
            race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("wisdom").get("base"), 1)
            dnd_dict.character_dict['Stats']['wisdom']['base'] = race2
            break


        else:
            print("Invalid Selection")
            continue

    while True:
        choice2 = input("Select the second stat you want to improve:\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\nEnter your Selection: ")
        if choice2=='1':
            if choice1=='1':
                print("Already Selected")
                continue
            else:
                race3 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("strength").get("base"), 1)
                dnd_dict.character_dict['Stats']['strength']['base'] = race3
                break
 
        elif choice2=='2':
            if choice1=='2':
                print("Already Selected")
                continue
            else:
                race3 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("dexterity").get("base"), 1)
                dnd_dict.character_dict['Stats']['dexterity']['base'] = race3
                break
 
        elif choice2=='3':
            if choice1=='3':
                print("Already Selected")
                continue
            else:
                race3 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("constitution").get("base"), 1)
                dnd_dict.character_dict['Stats']['constitution']['base'] = race3
                break
 
        elif choice2=='4':
            if choice1=='4':
                print("Already Selected")
                continue
            else:
                race3 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("intelligence").get("base"), 1)
                dnd_dict.character_dict['Stats']['intelligence']['base'] = race3
                break
 
        elif choice2=='5':
            if choice1=='5':
                print("Already Selected")
                continue
            else:
                race3 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("wisdom").get("base"), 1)
                dnd_dict.character_dict['Stats']['wisdom']['base'] = race3
                break

        else:
            print("Invalid Selection")
            continue

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)

    dnd_skills.set_skill()

# Select the languages known.
    dnd_dict.character_dict.get("Languages").append('Elven')
    dnd_language.elf_lang()

    dnd_class.RaceStats.racial_choice("Half-Elf", 30, "Medium")
    dnd_dict.character_dict.get("speed").append("30")
    dnd_dict.character_dict.get("size").append("Medium")
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Half-Elf")
    dnd_skills.half_elf_skills()

    dnd_features.half_elf_features()

def halfling_lightfoot():

    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("dexterity").get("base"), 2)
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("charisma").get("base"),1)

    dnd_dict.character_dict['Stats']['dexterity']['base'] = race1
    dnd_dict.character_dict['Stats']['charisma']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Lightfoot Halfling", 25, "Small")
    dnd_dict.character_dict.get("speed").append("25")
    dnd_dict.character_dict.get("size").append("Small")
    dnd_dict.character_dict.get("Languages").append('Halfling')
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Lightfoot Halfling")

    dnd_features.halfling_lightfoot_features()

def halfling_stout():

    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("dexterity").get("base"), 2)
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("constitution").get("base"),1)

    dnd_dict.character_dict['Stats']['dexterity']['base'] = race1
    dnd_dict.character_dict['Stats']['constitution']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Stout Halfling", 25, "Small")
    dnd_dict.character_dict.get("speed").append("25")
    dnd_dict.character_dict.get("size").append("Small")
    dnd_dict.character_dict.get("Languages").append("Halfling")
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Stout Halfling")

    dnd_features.halfling_stout_features()

def half_orc():

    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("strength").get("base"), 2)
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("constitution").get("base"),1)

    dnd_dict.character_dict['Stats']['strength']['base'] = race1
    dnd_dict.character_dict['Stats']['constitution']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Half-Orc", 30, "Medium")
    dnd_dict.character_dict.get("speed").append("30")
    dnd_dict.character_dict.get("size").append("Medium")
    dnd_dict.character_dict.get("Languages").append("Orc")
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Half-Orc")

#   Proficiency with Intimidation
    dnd_skills.intimidation_prof() 

    dnd_features.half_orc_features()


def human_regular():

    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("strength").get("base"), 1)
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("dexterity").get("base"),1)
    race3 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("constitution").get("base"), 1)
    race4 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("intelligence").get("base"), 1)
    race5 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("wisdom").get("base"), 1)
    race6 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("charisma").get("base"), 1)

    dnd_dict.character_dict['Stats']['strength']['base'] = race1
    dnd_dict.character_dict['Stats']['dexterity']['base'] = race2
    dnd_dict.character_dict['Stats']['constitution']['base'] = race3
    dnd_dict.character_dict['Stats']['intelligence']['base'] = race4
    dnd_dict.character_dict['Stats']['wisdom']['base'] = race5
    dnd_dict.character_dict['Stats']['charisma']['base'] = race6

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)

    dnd_skills.set_skill()

    dnd_language.language()
    dnd_class.RaceStats.racial_choice("Human", 30, "Medium")
    dnd_dict.character_dict.get("speed").append("30")
    dnd_dict.character_dict.get("size").append("Medium")
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Human")

def tiefling():

    race1 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("charisma").get("base"), 2)
    race2 = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("Stats").get("intelligence").get("base"),1)

    dnd_dict.character_dict['Stats']['charisma']['base'] = race1
    dnd_dict.character_dict['Stats']['intelligence']['base'] = race2

#Update all modifiers
    mod1 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('strength').get('base'))
    mod2 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('dexterity').get('base'))
    mod3 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('constitution').get('base'))
    mod4 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('intelligence').get('base'))
    mod5 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('wisdom').get('base'))
    mod6 = dnd_class.Character.mod(dnd_dict.character_dict.get("Stats").get('charisma').get('base'))


    dnd_dict.character_dict['Stats']['strength']['mod'] = mod1
    dnd_dict.character_dict['Stats']['dexterity']['mod'] = mod2
    dnd_dict.character_dict['Stats']['constitution']['mod'] = mod3
    dnd_dict.character_dict['Stats']['intelligence']['mod'] = mod4
    dnd_dict.character_dict['Stats']['wisdom']['mod'] = mod5
    dnd_dict.character_dict['Stats']['charisma']['mod'] = mod6

# Hit points: Constitution mod (except Hill Dwarves who get an additional +1)
    hit_points = dnd_dict.character_dict.get("Stats").get('constitution').get('mod')
    dnd_dict.character_dict.get('hp').append(hit_points)

    dnd_skills.set_skill()

    dnd_class.RaceStats.racial_choice("Tiefling", 30, "Medium")
    dnd_dict.character_dict.get("speed").append("30")
    dnd_dict.character_dict.get("size").append("Medium")
    dnd_dict.character_dict.get("Languages").append("Infernal")
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("race"),"Tiefling")

    dnd_features.tiefling_features()

def player_race():

# If the race has already been chosen in the config file, don't bother choosing.
    if "Dragonborn" in dnd_dict.character_dict.get("race"):
        dragonborn()
    elif "Hill Dwarf" in dnd_dict.character_dict.get("race"):
        dwarf_hill()
    elif "Mountain Dwarf" in dnd_dict.character_dict.get("race"):
        dwarf_mountain()
    elif "High Elf" in dnd_dict.character_dict.get("race"):
        elf_high()
    elif "Wood Elf" in dnd_dict.character_dict.get("race"):
        elf_wood()
    elif "Forest Gnome" in dnd_dict.character_dict.get("race"):
        gnome_forest()
    elif "Rock Gnome" in dnd_dict.character_dict.get("race"):
        gnome_rock()
    elif "Half-Elf" in dnd_dict.character_dict.get("race"):
        half_elf()
    elif "Lightfoot Halfling" in dnd_dict.character_dict.get("race"):
        halfling_lightfoot()
    elif "Stout Halfling" in dnd_dict.character_dict.get("race"):
        halfling_stout()
    elif "Half-Orc" in dnd_dict.character_dict.get("race"):
        half_orc()
    elif "Human" in dnd_dict.character_dict.get("race"):
        human_regular()
    elif "Tiefling" in dnd_dict.character_dict.get("race"):
        tiefling()
    else:
# If the config.ini has no race selected, delete that from the dictionary.
        del dnd_dict.character_dict.get("race")[0]
        while True:
            choose_race = input("Choose your race:\n1) Dragonborn\n2) Dwarf (Hill)\n3) Dwarf (Mountain)\n4) Elf (High)\n5) Elf (Wood)\n6) Gnome (Forest)\n7) Gnome (Rock)\n8) Half-Elf\n9) Halfling (Lightfoot)\n10) Halfling (Stout)\n11) Half-Orc\n12) Human (Regular)\n13) Tiefling\n0) Exit\nEnter your selection: ")
    
            if choose_race =='1':
                dragonborn() 
                break
     
            elif choose_race =='2':
                dwarf_hill()
                break
    
            elif choose_race =='3':
                dwarf_mountain()
                break
    
            elif choose_race =='4':
                elf_high()
                break
     
            elif choose_race =='5':
                elf_wood()
                break
    
            elif choose_race =='6':
                gnome_forest()
                break
    
            elif choose_race =='7':
                gnome_rock()
                break
    
            elif choose_race =='8':
                half_elf()
                break
    
            elif choose_race =='9':
                halfling_lightfoot()
                break
    
            elif choose_race =='10':
                halfling_stout()
                break
    
            elif choose_race =='11':
                half_orc()
                break
    
            elif choose_race =='12':
                human_regular()
                break
    
            elif choose_race =='13':
                tiefling()
                break
    
            elif choose_race == '0':
                print("Exiting program")
                exit()
    
            else:
                print("Invalid Selection")
                continue
