#!/usr/bin/python3
import os, stat_roller, dnd_features, dnd_language, dnd_tools, dnd_dict, dnd_skills, dnd_race, dnd_player_class, dnd_class, dnd_background, dnd_magic


# Display all of the information
def char_display():
    print("Name: {}".format(dnd_dict.character_dict.get("name")[0]))
#Printing the stat scores with their modifiers underneath
    print("Strength: ",dnd_dict.character_dict.get("Stats").get("strength").get("base"))
    print("Strength mod: ({})".format(dnd_dict.character_dict.get("Stats").get("strength").get("mod")))

    print("Dexterity: ",dnd_dict.character_dict.get("Stats").get("dexterity").get("base"))
    print("Dexterity mod: ({})".format(dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")))

    print("Constitution: ",dnd_dict.character_dict.get("Stats").get("constitution").get("base"))
    print("Constitution mod: ({})".format(dnd_dict.character_dict.get("Stats").get("constitution").get("mod")))

    print("Intelligence: ",dnd_dict.character_dict.get("Stats").get("intelligence").get("base"))
    print("Intelligence mod: ({})".format(dnd_dict.character_dict.get("Stats").get("intelligence").get("mod")))

    print("Wisdom: ",dnd_dict.character_dict.get("Stats").get("wisdom").get("base"))
    print("Wisdom mod: ({})".format(dnd_dict.character_dict.get("Stats").get("wisdom").get("mod")))

    print("Charisma: ",dnd_dict.character_dict.get("Stats").get("charisma").get("base"))
    print("Charisma mod: ({})".format(dnd_dict.character_dict.get("Stats").get("charisma").get("mod")))

#Print Saving Throws
    print("Strength Saving Throw: {}".format(dnd_dict.character_dict.get("Stats").get("strength").get("save")))
    print("Dexterity Saving Throw: {}".format(dnd_dict.character_dict.get("Stats").get("dexterity").get("save")))
    print("Constitution Saving Throw: {}".format(dnd_dict.character_dict.get("Stats").get("constitution").get("save")))
    print("Intelligence Saving Throw: {}".format(dnd_dict.character_dict.get("Stats").get("intelligence").get("save")))
    print("Wisdom Saving Throw: {}".format(dnd_dict.character_dict.get("Stats").get("wisdom").get("save")))
    print("Charisma Saving Throw: {}".format(dnd_dict.character_dict.get("Stats").get("charisma").get("save")))

    print("Player Class: {}".format(', '.join(dnd_dict.character_dict.get("player_class"))))
    print("Background: {}".format(dnd_dict.character_dict.get("background")[0]))
    print("Race: {}".format(dnd_dict.character_dict.get("race")[0]))
# Initiative bonus is the Dex mod.
    print("Initiative Bonus: {}".format(dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")))
    print("Armor Class: {}".format(dnd_dict.character_dict.get("armor_class")[0]))
    print("Passive Perception: {}".format(dnd_dict.character_dict.get("passive_perception")[0]))
    print("Hit Points: {}".format(dnd_dict.character_dict.get("hp")))
# Hit Dice List
    dnd_class.RaceStats.hit_dice_display(dnd_dict.character_dict.get("d6"),"d6")
    dnd_class.RaceStats.hit_dice_display(dnd_dict.character_dict.get("d8"),"d8")
    dnd_class.RaceStats.hit_dice_display(dnd_dict.character_dict.get("d10"),"d10")
    dnd_class.RaceStats.hit_dice_display(dnd_dict.character_dict.get("d12"),"d12")
    print("Walking Speed: {}".format(dnd_dict.character_dict.get("speed")[0]))
    print("Size: {}".format(dnd_dict.character_dict.get("size")[0]))
    print("Languages known: {}".format(', '.join(dnd_dict.character_dict.get("Languages"))))
    if dnd_dict.character_dict.get("Tools"):
        print("Tool Proficiencies: {}".format(', '.join(dnd_dict.character_dict.get("Tools"))))
    else:
        print("Tool Proficiencies: N/A")
    if dnd_dict.character_dict.get("Kits"):
        print("Kit Proficiencies: {}".format(', '.join(dnd_dict.character_dict.get("Kits"))))
    else:
        print("Kit Proficiencies: N/A")
    if dnd_dict.character_dict.get("Vehicle"):
        print("Vehicle Proficiencies: {}".format(', '.join(dnd_dict.character_dict.get("Vehicles"))))
    else:
        print("Vehicle Proficiencies: N/A")
    if dnd_dict.character_dict.get("Gaming_Set"):
        print("Gaming Set Proficiencies: {}".format(', '.join(dnd_dict.character_dict.get("Gaming_Set"))))
    else:
        print("Gaming Set Proficiencies: N/A")
    if dnd_dict.character_dict.get("Instruments"):
        print("Instruments Proficiencies: {}".format(', '.join(dnd_dict.character_dict.get("Instruments"))))
    else:
        print("Instrument Proficiencies: N/A")

# Joins any weapons in the lists and removes duplicates
    weapon_prof = dnd_dict.character_dict.get('Weapon_Prof')
    if len(weapon_prof) == 3:
        weapon_prof = weapon_prof[0] + weapon_prof[1] + weapon_prof[2]
# removes duplicates
        weapon_prof = list(set(weapon_prof))
    elif len(weapon_prof) == 2:
        weapon_prof = weapon_prof[0] + weapon_prof[1]
        weapon_prof = list(set(weapon_prof))
    elif len(weapon_prof) ==1:
        weapon_prof = weapon_prof[0]
        weapon_prof = list(set(weapon_prof))

# Joins any armor in the lists and removes duplicates
    armor_prof = dnd_dict.character_dict.get('Armor_Prof')
    if len(armor_prof) == 3:
        armor_prof = armor_prof[0] + armor_prof[1] + armor_prof[2]
# removes duplicates
        armor_prof = list(set(armor_prof))
    elif len(armor_prof) == 2:
        armor_prof = armor_prof[0] + armor_prof[1]
# removes duplicates
        armor_prof = list(set(armor_prof))
    elif len(armor_prof) ==1:
        armor_prof = armor_prof[0]
        armor_prof = list(set(armor_prof))

    misc_items = dnd_dict.character_dict.get('Misc')
    misc_items = misc_items[0]
    misc_tems = list(set(misc_items))

    magic_spells = dnd_dict.character_dict.get("first_level")

# Necessary since the first level spells for these classes are put into a single list
    if "Artificer" in dnd_dict.character_dict.get("player_class") or "Cleric" in dnd_dict.character_dict.get("player_class") or "Druid" in dnd_dict.character_dict.get("player_class"):
        magic_spells = dnd_dict.character_dict.get("first_level")

# Certain subclasses add spells to the existing list
        if len(magic_spells) == 2:
            magic_spells = magic_spells[0]+magic_spells[1]
            magic_spells = list(set(magic_spells))
        else:
            magic_spells = magic_spells[0]
            magic_spells = list(set(magic_spells))

    print("Weapon Proficiencies: {}".format(', '.join([str(i) for i in weapon_prof])))
    if armor_prof:
        print("Armor Proficiencies: {}".format(', '.join([str(i) for i in armor_prof])))
    else:
        print("Armor Proficiencies: N/A")
    if dnd_dict.character_dict.get("gold"):
        print("Gold: {}".format(dnd_dict.character_dict.get("gold")[0]))
    else:
        print("Gold: 0")
    print("Equipment: {}".format(', '.join(dnd_dict.character_dict.get("Equipment"))))
#Spell Attack Modifier, if there is none, then print N/A
    if dnd_dict.character_dict.get("spell_attack"):
        print("Spell Attack Modifier: {}".format(dnd_dict.character_dict.get("spell_attack")[0]))
    else:
        print("Spell Save DC: N/A")
#Spell Save DC
    if dnd_dict.character_dict.get("spell_save"):
        print("Spell Save DC: {}".format(dnd_dict.character_dict.get("spell_save")[0]))
    else:
        print("Spell Save DC: N/A")
    if dnd_dict.character_dict.get("cantrip"):
        print("Cantrips known: {}".format(', '.join(dnd_dict.character_dict.get("cantrip"))))
    else:
        print("Cantrips Known: N/A")
    if dnd_dict.character_dict.get("first_level"):
        print("First Level Spells Known: {}".format(', '.join([str(i) for i in magic_spells])))
    else:
        print("First Level Spells Known: N/A")
    print("Misc. Items: {}".format(', '.join(map(str,misc_items))))
    features = dnd_dict.character_dict.get("features")
    features= ' '.join(features)
    print("Features:\n{}".format(features))


    print("Proficiency Bonus: {}".format(dnd_skills.prof_bonus))
#Displays the skills. If the character has proficieny or expertise,
# it puts a (*) or (*)(E) before the number

    print("Acrobatics: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("acrobatics"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("dexterity").get("mod"))))

    print("Animal Handling: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("animal_handling"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("wisdom").get("mod"))))

    print("Arcana: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("arcana"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("intelligence").get("mod"))))

    print("Athletics: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("athletics"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("strength").get("mod"))))

    print("Deception: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("deception"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("charisma").get("mod"))))

    print("History: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("history"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("intelligence").get("mod"))))

    print("Insight: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("insight"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("wisdom").get("mod"))))

    print("Intimidation: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("intimidation"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("charisma").get("mod"))))

    print("Investigation: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("investigation"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("intelligence").get("mod"))))

    print("Medicine: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("medicine"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("wisdom").get("mod"))))

    print("Nature: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("nature"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("intelligence").get("mod"))))

    print("Perception: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("perception"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("wisdom").get("mod"))))

    print("Performance: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("performance"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("charisma").get("mod"))))

    print("Persuasion: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("persuasion"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("charisma").get("mod"))))

    print("Religion: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("religion"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("intelligence").get("mod"))))

    print("Sleight of Hand: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("sleight_of_hand"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("dexterity").get("mod"))))

    print("Stealth: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("stealth"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("dexterity").get("mod"))))

    print("Survival: {}".format(dnd_class.Character.show_prof(dnd_skills.skills_dict.get("survival"),dnd_skills.prof_bonus,dnd_dict.character_dict.get("Stats").get("wisdom").get("mod"))))
    return
