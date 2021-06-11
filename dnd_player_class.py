#!/usr/bin/python3
import os, math, json, dnd_features, dnd_language, dnd_tools, dnd_dict, dnd_skills, dnd_race, dnd_class, dnd_pack, dnd_weapon, dnd_magic, random

#Player classes
def artificer():

# Set the HP here, add the HP from the race to the hit points determined above
    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],16)
    print(hp_mod)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d8"),1)
    dnd_dict.character_dict['d8']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per artificer level")

    armor_prof = ['Light Armor', 'Medium Armor', 'Shields']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)

# Setting the armor and weapon proficiencies

    weapon_prof = ['Simple Weapons']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)
# If you are already proficient in Thieve's Tools or Tinker's Tools, pass
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("Kits"),"Thieves' Tools")
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("Kits"),"Tinker's Tools")

    dnd_tools.artisan_tools()

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Artificer")


#Selecting the skills
#If the player is already proficient, loop back to the start and ask again.
#If they are not, then procede as normal
    i = 1
    while i < 3:
        while True:
            print(f'{i}/2')
            choice1 = input("Select the skill you want proficiency in:\n1) Arcana\n2) History\n3) Investigation\n4) Medicine\n5) Nature\n6) Perception\n7) Sleight of Hand\nEnter your Selection: ")
            if choice1=='1':
                if dnd_skills.skills_dict['arcana']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_arc = dnd_class.RaceStats.stat_bonus(arc_mod, dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['arcana'] = updated_arc
                    i+=1
                    break
                elif dnd_skills.skills_dict['arcana']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue
     
     
            elif choice1=='2':
                if dnd_skills.skills_dict['history']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_his = dnd_class.RaceStats.stat_bonus(his_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['history'] = updated_his
                    i+=1
                    break
                elif dnd_skills.skills_dict['history']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue
     
            elif choice1=='3':
                if dnd_skills.skills_dict['investigation']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_inv = dnd_class.RaceStats.stat_bonus(inv_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['investigation']=updated_inv
                    i+=1
                    break
                elif dnd_skills.skills_dict['investigation']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue
     
            elif choice1=='4':
                if dnd_skills.skills_dict['medicine']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    med_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_med = dnd_class.RaceStats.stat_bonus(med_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['medicine']=updated_med
                    i+=1
                    break
                elif dnd_skills.skills_dict['medicine']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue
     
     
            elif choice1=='5':
                if dnd_skills.skills_dict['nature']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_nat = dnd_class.RaceStats.stat_bonus(nat_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['nature']=updated_nat
                    i+=1
                    break
                elif dnd_skills.skills_dict['nature']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue
     
     
            elif choice1=='6':
                if dnd_skills.skills_dict['perception']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    prc_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_prc = dnd_class.RaceStats.stat_bonus(prc_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['perception']=updated_prc
                    i+=1
                    break
                elif dnd_skills.skills_dict['perception']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue
     
            elif choice1=='7':
                if dnd_skills.skills_dict['sleight_of_hand']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    soh_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                    updated_soh = dnd_class.RaceStats.stat_bonus(soh_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['sleight_of_hand']=updated_soh
                    i+=1
                    break
                elif dnd_skills.skills_dict['sleight_of_hand']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    print("Already proficient")
                    continue
     
            else:
                print("Invalid selection")
                continue


# Setting the saving throws.

    str_save = dnd_dict.character_dict['Stats']['strength']['mod']
    dex_save = dnd_dict.character_dict['Stats']['dexterity']['mod']
    con_save = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['constitution']['mod'],dnd_skills.prof_bonus)
    int_save = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],dnd_skills.prof_bonus)
    wis_save = dnd_dict.character_dict['Stats']['wisdom']['mod']
    cha_save = dnd_dict.character_dict['Stats']['charisma']['mod']

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
    
# Put into the dictionary

    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save

# Getting equipment
    dnd_weapon.double_simple()
    dnd_dict.character_dict.get("Equipment").append('Light Crossbow')
    dnd_dict.character_dict.get("Equipment").append('20 Bolts')
    dnd_dict.character_dict.get("Equipment").append('Thieves\' Tools')
    dnd_pack.dungeoneer_pack()


# Choose the type of armor you get
    while True:
        armor_choice = input("Choose which armor you will take:\n1) Studded Leather Armor\n2) Scale Mail\nEnter your selection: ")
        if armor_choice == '1':
            dnd_dict.character_dict.get("Equipment").append('Studded Leather Armor')
            armor_class = dnd_weapon.studded_leather_armor()
            print("Armor Class: ",armor_class)
            dnd_dict.character_dict.get("armor_class").append(armor_class)
            break

        elif armor_choice == '2':
            dnd_dict.character_dict.get("Equipment").append('Scale Mail')
            armor_class = dnd_class.RaceStats.stat_bonus(dnd_class.RaceStats.med_armor(dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")),14)
            print("Armor Class: ",armor_class)
            dnd_dict.character_dict.get("armor_class").append(armor_class)
            break
    
        else:
            print("Invalid Selection")
            continue

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = dnd_class.RaceStats.spell_attack((dnd_dict.character_dict.get("Stats").get("intelligence").get('mod')),dnd_skills.prof_bonus)
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict.get("spell_attack").append(spell_attack)

    spell_save = dnd_class.RaceStats.spell_save((dnd_dict.character_dict.get("Stats").get("intelligence").get('mod')),dnd_skills.prof_bonus)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict.get("spell_save").append(spell_save)


    dnd_magic.artificer_magic()
#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)

    dnd_features.artificer_features()
    return


def barbarian():

# Set the HP here, add the HP from the race to the hit points determined above
    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],24)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d12"),1)
    dnd_dict.character_dict['d12']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d12 per barbarian level")

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Barbarian")

# Setting the Armor Class
    print("""
Unarmored Defense

While you are not wearing any armor, your armor class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit. """)
#Armor Class = 10 + Dexterity Modifier + Constitution Modifier
    AC= (10 + dnd_dict.character_dict['Stats']['dexterity']['mod'] + (dnd_dict.character_dict['Stats']['constitution']['mod']))
    print("Armor Class: ",AC)
    dnd_dict.character_dict.get("armor_class").append(AC)

# Setting the armor and weapon proficiencies


    armor_prof = ['Light Armor','Medium Armor','Shields']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)

    weapon_prof = ['Simple Weapons', 'Martial Weapons']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)



#Selecting the skills
    i = 1
    while i < 3:
        while True:
           print(f'{i}/2')
           choice = input("Select the skill you want proficiency in:\n1) Animal Handling\n2) Athletics\n3) Intimidation\n4) Nature\n5) Perception\n6) Survival\nEnter your Selection: ")
           if choice=='1':
               if dnd_skills.skills_dict['animal_handling']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                   anm_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                   updated_anm = dnd_class.RaceStats.stat_bonus(anm_mod, dnd_skills.prof_bonus)
                   dnd_skills.skills_dict['animal_handling'] = updated_anm
                   i+=1
                   break
               elif dnd_skills.skills_dict['animal_handling']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                   print("Already proficient")
                   continue
    
    
           elif choice=='2':
               if dnd_skills.skills_dict['athletics']==dnd_dict.character_dict['Stats']['strength']['mod']:
                   ath_mod = dnd_dict.character_dict['Stats']['strength']['mod']
                   updated_ath = dnd_class.RaceStats.stat_bonus(ath_mod,dnd_skills.prof_bonus)
                   dnd_skills.skills_dict['athletics'] = updated_ath
                   i+=1
                   break
               elif dnd_skills.skills_dict['athletics']>dnd_dict.character_dict['Stats']['strength']['mod']:
                   print("Already proficient")
                   continue
    
           elif choice=='3':
               if dnd_skills.skills_dict['intimidation']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                   itd_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                   updated_itd = dnd_class.RaceStats.stat_bonus(itd_mod,dnd_skills.prof_bonus)
                   dnd_skills.skills_dict['intimidation']=updated_itd
                   i+=1
                   break
               elif dnd_skills.skills_dict['intimidation']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                   print("Already proficient")
                   continue
    
           elif choice=='4':
               if dnd_skills.skills_dict['nature']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                   nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                   updated_nat = dnd_class.RaceStats.stat_bonus(nat_mod,dnd_skills.prof_bonus)
                   dnd_skills.skills_dict['nature']=updated_nat
                   i+=1
                   break
               elif dnd_skills.skills_dict['nature']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                   print("Already proficient")
                   continue
    
    
           elif choice=='5':
               if dnd_skills.skills_dict['perception']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                   prc_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                   updated_prc = dnd_class.RaceStats.stat_bonus(prc_mod,dnd_skills.prof_bonus)
                   dnd_skills.skills_dict['perception']=updated_prc
                   i+=1
                   break
               elif dnd_skills.skills_dict['perception']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                   print("Already proficient")
                   continue
    
    
           elif choice=='6':
               if dnd_skills.skills_dict['survival']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                   sur_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                   updated_sur = dnd_class.RaceStats.stat_bonus(sur_mod,dnd_skills.prof_bonus)
                   dnd_skills.skills_dict['survival']=updated_sur
                   i+=1
                   break
               elif dnd_skills.skills_dict['survival']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                   print("Already proficient")
                   continue
    
    
           else:
               print("Invalid selection")
               continue

# Setting the saving throws.

    str_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['strength']['mod']),dnd_skills.prof_bonus)
    dex_save = dnd_dict.character_dict['Stats']['dexterity']['mod']
    con_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['constitution']['mod']),dnd_skills.prof_bonus)
    int_save = dnd_dict.character_dict['Stats']['intelligence']['mod']
    wis_save = dnd_dict.character_dict['Stats']['wisdom']['mod']
    cha_save = dnd_dict.character_dict['Stats']['charisma']['mod']

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
    
# Put into the dictionary

    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Selecting Equipment
    while True:
        choice1 = input("Choose which primary weapon you will take\n1) A greataxe\n2) Any martial melee weapon\nChoose your selection: ")
        if choice1 == '1':
            dnd_dict.character_dict.get("Equipment").append('Greataxe')
            break
    
        elif choice1 == '2':
           dnd_weapon.martial_melee()
           break

        else:
            print("Invalid Selection")
            continue

    while True:
        choice2 = input("Choose which secondary weapon you will take\n1) Two Handaxes\n2) Any simple weapon\nEnter your selection: ")
    
        if choice2 == '1':
            dnd_dict.character_dict.get("Equipment").append('Handaxe')
            dnd_dict.character_dict.get("Equipment").append('Handaxe')
            break
 
        elif choice2 == '2':
            dnd_weapon.simple_weapon()
            break
    
        else:
            print("Invalid Selection")
            continue


    dnd_pack.explorer_pack()
    dnd_dict.character_dict.get("Equipment").append('Javelin (x4)')

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)

    dnd_features.barbarian_features()
    return


def bard():

    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],16)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d8"),1)
    dnd_dict.character_dict['d8']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per bard level")

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Bard")

# Setting the armor and weapon proficiencies


    weapon_prof = ['Simple Weapons', 'Hand Crossbows', 'Rapiers', 'Longswords','Shortswords'] 
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)

    armor_prof = ['Light Armor']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)

    dnd_tools.musical_instrument()
    dnd_tools.musical_instrument()
    dnd_tools.musical_instrument()



# Setting the skill proficiencies
    dnd_skills.bard_skills()

# Setting the saving throws.

    str_save = dnd_dict.character_dict['Stats']['strength']['mod']
    dex_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['dexterity']['mod']),dnd_skills.prof_bonus)
    con_save = dnd_dict.character_dict['Stats']['constitution']['mod']
    int_save = dnd_dict.character_dict['Stats']['intelligence']['mod']
    wis_save = dnd_dict.character_dict['Stats']['wisdom']['mod']
    cha_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['charisma']['mod']),dnd_skills.prof_bonus)

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
    
    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Getting equipment

    while True:
        choice1 = input("Choose which primary weapon you will take\n1) A rapier\n2) A longsword\n3) Any simple weapon\nChoose your selection: ")
        if choice1 == '1':
            dnd_dict.character_dict.get("Equipment").append('A Rapier')
            break

        elif choice1 == '2':
            dnd_dict.character_dict.get("Equipment").append('A Longsword')
            break

        elif choice1 == '3':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        choice2 = input("Choose which pack you will take\n1) A diplomat's pack\n2) An entertainer's pack\nEnter your selection: ")

        if choice2 == '1':
            dnd_pack.diplomat_pack()
            break

        elif choice2 == '2':
            dnd_pack.entertainer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        choice3 = input("Choose which instrument you will take\n1) A lute\n2) Any other musical instrument\nEnter your selection: ")

        if choice3 == '1':
            dnd_dict.character_dict.get("Equipment").append('A lute')
            break

        elif choice3 == '2':
            musical_equip = input("Which instrument do you want to take? ")
            dnd_dict.character_dict.get("Equipment").append(musical_equip)
            break

        else:
            print("Invalid Selection")
            continue

#Leather armor is 11 + Dex Mod
    dnd_dict.character_dict.get("Equipment").append('Leather Armor')
    dnd_dict.character_dict.get("Equipment").append('A Dagger')


    armor_class = dnd_weapon.leather_armor()
    print("Armor Class: ",armor_class)
    dnd_dict.character_dict.get("armor_class").append(armor_class)

    dnd_magic.bard_magic()

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = dnd_class.RaceStats.spell_attack((dnd_dict.character_dict.get("Stats").get("charisma").get('mod')),dnd_skills.prof_bonus)
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict.get("spell_attack").append(spell_attack)

    spell_save = dnd_class.RaceStats.spell_save((dnd_dict.character_dict.get("Stats").get("charisma").get('mod')),dnd_skills.prof_bonus)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict.get("spell_save").append(spell_save)

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)

    return

def cleric():

    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],16)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d8"),1)
    dnd_dict.character_dict['d8']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per cleric level")

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Cleric")

# Setting the armor and weapon proficiencies
    armor_prof = ['Light Armor', 'Medium Armor', 'Shields']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)
    weapon_prof = ['Simple Weapons']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)

#Selecting the skills
    i = 1
    while i < 3:
# If the player is proficient in all of the skills, break.
        if dnd_skills.skills_dict['history']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],dnd_skills.prof_bonus) and dnd_skills.skills_dict['insight']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],dnd_skills.prof_bonus) and dnd_skills.skills_dict['medicine']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],dnd_skills.prof_bonus) and dnd_skills.skills_dict['persuasion']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['charisma']['mod'],dnd_skills.prof_bonus) and dnd_skills.skills_dict['religion']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],dnd_skills.prof_bonus):
            i+=1
            break
        else: 
            while True:
                print(f'{i}/2')
                choice1 = input("Select the first skill you want proficiency in:\n1) History\n2) Insight\n3) Medicine\n4) Persuasion\n5) Religion\nEnter your Selection: ")
                if choice1=='1':
                    if dnd_skills.skills_dict['history']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                        updated_his = dnd_class.RaceStats.stat_bonus(his_mod, dnd_skills.prof_bonus)
                        dnd_skills.skills_dict['history'] = updated_his
                        i += 1
                        break
                    elif dnd_skills.skills_dict['history']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        print("Already proficient")
                        continue
 
                elif choice1=='2':
                    if dnd_skills.skills_dict['insight']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                        ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                        updated_ins = dnd_class.RaceStats.stat_bonus(ins_mod,dnd_skills.prof_bonus)
                        dnd_skills.skills_dict['insight'] = updated_ins
                        i += 1
                        break
                    elif dnd_skills.skills_dict['insight']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                        print("Already proficient")
                        continue
 
                elif choice1=='3':
                    if dnd_skills.skills_dict['medicine']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                        med_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                        updated_med = dnd_class.RaceStats.stat_bonus(med_mod,dnd_skills.prof_bonus)
                        dnd_skills.skills_dict['medicine']=updated_med
                        i += 1
                        break
                    elif dnd_skills.skills_dict['medicine']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                        print("Already proficient")
                        continue

                elif choice1=='4':
                    if dnd_skills.skills_dict['persuasion']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                        per_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                        updated_per = dnd_class.RaceStats.stat_bonus(per_mod,dnd_skills.prof_bonus)
                        dnd_skills.skills_dict['persuasion']=updated_per
                        i += 1
                        break
                    elif dnd_skills.skills_dict['persuasion']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                        print("Already proficient")
                        continue

                elif choice1=='5':
                    if dnd_skills.skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                        updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,dnd_skills.prof_bonus)
                        dnd_skills.skills_dict['religion']=updated_rel
                        i += 1
                        break
                    elif dnd_skills.skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                        print("Already proficient")
                        continue

                else:
                    print("Invalid selection")
                    continue

# Setting the saving throws.

    str_save = dnd_dict.character_dict['Stats']['strength']['mod']
    dex_save = dnd_dict.character_dict['Stats']['dexterity']['mod']
    con_save = dnd_dict.character_dict['Stats']['constitution']['mod']
    int_save = dnd_dict.character_dict['Stats']['intelligence']['mod']
    wis_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['wisdom']['mod']),dnd_skills.prof_bonus)
    cha_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['charisma']['mod']),dnd_skills.prof_bonus)

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
    
# Put into the dictionary


    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Getting equipment

    while True:
        weapon_choice1 = input("What primary weapon do you want?\n1) A Mace\n2) A warhammer\nEnter your selection: ")
        if weapon_choice1 == '1':
            dnd_dict.character_dict.get("Equipment").append('Mace')
            break

        elif weapon_choice1 == '2':
            dnd_dict.character_dict.get("Equipment").append('Warhammer')
            break

        else:
            print("Invalid Selection")
            continue


# Choose the type of armor you get
    while True:
        armor_choice = input("Choose which armor you will take:\n1) Leather Armor\n2) Scale Mail\n3) Chain Mail\nEnter your selection: ")

#Leather Armor = 11 + Dex mod +2 from shield(given below)
        if armor_choice == '1':
            dnd_dict.character_dict.get("Equipment").append('Leather Armor')
            armor_class = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")),13)
            print("Armor Class: ",armor_class)
            dnd_dict.character_dict.get("armor_class").append(armor_class)
            break

#Scale Mail = 14 + Dex mod (maximum of +2) + 2 from the shield (given below)
        elif armor_choice == '2':
            dnd_dict.character_dict.get("Equipment").append('Scale Mail')
            armor_class = dnd_class.RaceStats.stat_bonus(dnd_class.RaceStats.med_armor(dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")),16)
            print("Armor Class: ",armor_class)
            dnd_dict.character_dict.get("armor_class").append(armor_class)
            break

#Chain Mail is a flat AC of 16+2 from shield (given below)
        elif armor_choice == '3':
            dnd_dict.character_dict.get("Equipment").append('Chain Mail')
            print("Armor Class: 18")
            dnd_dict.character_dict.get("armor_class").append("18")
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice2 = input("What secondary weapon do you want?\n1) A Light Crossbow with 20 bolts\n2) Any simple weapon\nEnter your selection: ")
        if weapon_choice2 == '1':
            dnd_dict.character_dict.get("Equipment").append('Light Crossbow')
            dnd_dict.character_dict.get("Equipment").append('20 Bolts')
            break

        elif weapon_choice2 == '2':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("What pack do you want?\n1) A priest's pack\n2) An explorer's pack\nEnter your selection: ")
        if pack_choice == '1':
            dnd_pack.priest_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_dict.character_dict.get("Equipment").append('Shield')
    dnd_dict.character_dict.get("Equipment").append('Holy Symbol')



    dnd_magic.cleric_magic()

# Choose the subclass
    while True:
        subclass_choice = input("Select your Domain:\n1) Knowledge Domain\n2) Life Domain\n3) Light Domain\n4) Nature Domain\n5) Tempest Domain\n6) Trickery Domain\n7) War Domain\nEnter your Selection: ")
        if subclass_choice=='1':
            dnd_features.knowledge_cleric_feature()
            break

        elif subclass_choice=='2':
            dnd_features.life_cleric_feature()
            break

        elif subclass_choice=='3':
            dnd_features.light_cleric_feature()
            break

        elif subclass_choice=='4':
            dnd_features.nature_cleric_feature()
            break

        elif subclass_choice=='5':
            dnd_features.tempest_cleric_feature()
            break

        elif subclass_choice=='6':
            dnd_features.trickery_cleric_feature()
            break

        elif subclass_choice=='7':
            dnd_features.war_cleric_feature()
            break

        else:
            print("Invalid Selection")
            continue
# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = dnd_class.RaceStats.spell_attack((dnd_dict.character_dict.get("Stats").get("wisdom").get('mod')),dnd_skills.prof_bonus)
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict.get("spell_attack").append(spell_attack)

    spell_save = dnd_class.RaceStats.spell_save((dnd_dict.character_dict.get("Stats").get("wisdom").get('mod')),dnd_skills.prof_bonus)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict.get("spell_save").append(spell_save)

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)

    return

def druid():

    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],16)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d8"),1)
    dnd_dict.character_dict['d8']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per druid level")

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Druid")

# Setting the armor and weapon proficiencies
# Druids also know the Druidic Language


    armor_prof=['Light Armor (Not made of metal)', 'Medium Armor (Not made of metal)', 'Shields (Not made of metal)']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)
    dnd_dict.character_dict.get("Languages").append('Druidic')
    weapon_prof=['Clubs', 'Daggers', 'Darts', 'Javelins', 'Maces', 'Quarterstaffs', 'Scimitars', 'Sickles', 'Slings', 'Spears']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)
    dnd_dict.character_dict.get("Kits").append('Herbalism Kit')



#Selecting the skills
    i = 1
    while i < 3:
        while True:
            print(f'{i}/2')
            choice1 = input("Select the skill you want proficiency in:\n1) Arcana\n2) Animal Handling\n3) Insight\n4) Medicine\n5) Nature\n6) Perception\n7) Religion\n8) Sleight of Hand\nEnter your Selection: ")
            if choice1=='1':
                if dnd_skills.skills_dict['arcana']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_arc = dnd_class.RaceStats.stat_bonus(arc_mod, dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['arcana'] = updated_arc
                    i+=1
                    break
                elif dnd_skills.skills_dict['arcana']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue

 
            elif choice1=='2':
                if dnd_skills.skills_dict['animal_handling']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    anm_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_anm = dnd_class.RaceStats.stat_bonus(anm_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['animal_handling'] = updated_anm
                    i+=1
                    break
                elif dnd_skills.skills_dict['animal_handling']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='3':
                if dnd_skills.skills_dict['insight']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_ins = dnd_class.RaceStats.stat_bonus(ins_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['insight']=updated_ins
                    i+=1
                    break
                elif dnd_skills.skills_dict['insight']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='4':
                if dnd_skills.skills_dict['medicine']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    med_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_med = dnd_class.RaceStats.stat_bonus(med_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['medicine']=updated_med
                    i+=1
                    break
                elif dnd_skills.skills_dict['medicine']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='5':
                if dnd_skills.skills_dict['nature']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_nat = dnd_class.RaceStats.stat_bonus(nat_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['nature']=updated_nat
                    i+=1
                    break
                elif dnd_skills.skills_dict['nature']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='6':
                if dnd_skills.skills_dict['perception']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    prc_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_prc = dnd_class.RaceStats.stat_bonus(prc_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['perception']=updated_prc
                    i+=1
                    break
                elif dnd_skills.skills_dict['perception']>dnd_dict.haracter_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='7':
                if dnd_skills.skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['religion']=updated_rel
                    i+=1
                    break
                elif dnd_skills.skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='8':
                if dnd_skills.skills_dict['sleight_of_hand']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    soh_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                    updated_soh = dnd_class.RaceStats.stat_bonus(soh_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['sleight_of_hand']=updated_soh
                    i+=1
                    break
                elif dnd_skills.skills_dict['sleight_of_hand']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    print("Already proficient")
                    continue

            else:
                print("Invalid selection")
                continue

# Setting the saving throws.

    str_save = dnd_dict.character_dict['Stats']['strength']['mod']
    dex_save = dnd_dict.character_dict['Stats']['dexterity']['mod']
    con_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['constitution']['mod']),dnd_skills.prof_bonus)
    int_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['intelligence']['mod']),dnd_skills.prof_bonus)
    wis_save = dnd_dict.character_dict['Stats']['wisdom']['mod']
    cha_save = dnd_dict.character_dict['Stats']['charisma']['mod']

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
# Put into the dictionary
    
    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Getting equipment


    dnd_weapon.double_simple()
    dnd_dict.character_dict.get("Equipment").append('Light Crossbow, 20 Bolts, Thieves\' Tools')
    dnd_pack.dungeoneer_pack()

    while True:
        weapon_choice1 = input("Choose what your primary weapon will be:\n1) A wooden shield\n2) Any simple weapon\nEnter your selection: ")
        if weapon_choice1 == '1':
            dnd_dict.character_dict.get("Equipment").append('Wooden Shield')
# Shields give an armor class of +2, and leather armor (given later) gives an AC of 11 + Dex mod
            armor_class = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")),13)
            print("Armor Class: ",armor_class)
            dnd_dict.character_dict.get("armor_class").append(armor_class)
            break

        elif weapon_choice1 == '2':
            dnd_weapon.simple_weapon()

# Leather armor (given later) gives an AC of 11 + Dex mod
            armor_class = dnd_weapon.leather_armor()
            print("Armor Class: ",armor_class)
            dnd_dict.character_dict.get("armor_class").append(armor_class)
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice2 = input("Choose what your secondary weapon will be:\n1) A scimitar\n2) Any simple melee weapon\nEnter your selection: ")
        if weapon_choice2 == '1':
            dnd_dict.character_dict.get("Equipment").append('Scimitar')
            break
 
        elif weapon_choice2 == '2':
            dnd_weapon.simple_melee()
            break

        else:
            print("Invalid Selection")
            continue


    dnd_dict.character_dict.get("Equipment").append('Leather Armor')
    dnd_dict.character_dict.get("Equipment").append('A Druidic Focus')

    dnd_pack.explorer_pack()

    dnd_magic.druid_magic()

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = dnd_class.RaceStats.spell_attack((dnd_dict.character_dict.get("Stats").get("wisdom").get('mod')),dnd_skills.prof_bonus)
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict.get("spell_attack").append(spell_attack)

    spell_save = dnd_class.RaceStats.spell_save((dnd_dict.character_dict.get("Stats").get("wisdom").get('mod')),dnd_skills.prof_bonus)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict.get("spell_save").append(spell_save)

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)

    dnd_features.druid_features()
    return


def fighter():

    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],20)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d10"),1)
    dnd_dict.character_dict['d10']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d10 per fighter level")

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Fighter")

# Setting the armor and weapon proficiencies
    armor_prof=['Light Armor', 'Medium Armor', 'Heavy Armor', 'Shields']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)
    weapon_prof=['Simple Weapons', 'Martial Weapons']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)


#Selecting the skills
    i = 1
    while i < 3:
        while True:
            print(f'{i}/2')
            choice1 = input("Select the skill you want proficiency in:\n1) Acrobatics\n2) Animal Handling\n3) Athletics\n4) History\n5) Insight\n6) Intimidation\n7) Perception\n8) Survival\nEnter your Selection: ")
            if choice1=='1':
                if dnd_skills.skills_dict['acrobatics']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    acr_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                    updated_acr = dnd_class.RaceStats.stat_bonus(acr_mod, dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['acrobatics'] = updated_acr
                    i+=1
                    break
                elif dnd_skills.skills_dict['acrobatics']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='2':
                if dnd_skills.skills_dict['animal_handling']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    anm_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_anm = dnd_class.RaceStats.stat_bonus(anm_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['animal_handling'] = updated_anm
                    i+=1
                    break
                elif dnd_skills.skills_dict['animal_handling']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='3':
                if dnd_skills.skills_dict['athletics']==dnd_dict.character_dict['Stats']['strength']['mod']:
                    ath_mod = dnd_dict.character_dict['Stats']['strength']['mod']
                    updated_ath = dnd_class.RaceStats.stat_bonus(ath_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['athletics']=updated_ath
                    i+=1
                    break
                elif dnd_skills.skills_dict['athletics']>dnd_dict.character_dict['Stats']['strength']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='4':
                if dnd_skills.skills_dict['history']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_his = dnd_class.RaceStats.stat_bonus(his_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['history']=updated_his
                    i+=1
                    break
                elif dnd_skills.skills_dict['history']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='5':
                if dnd_skills.skills_dict['insight']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_ins = dnd_class.RaceStats.stat_bonus(ins_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['insight']=updated_ins
                    i+=1
                    break
                elif dnd_skills.skills_dict['insight']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='6':
                if dnd_skills.skills_dict['intimidation']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                    itd_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                    updated_itd = dnd_class.RaceStats.stat_bonus(itd_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['intimidation']=updated_itd
                    i+=1
                    break
                elif dnd_skills.skills_dict['intimidation']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='7':
                if dnd_skills.skills_dict['perception']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    prc_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_prc = dnd_class.RaceStats.stat_bonus(prc_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['perception']=updated_prc
                    i+=1
                    break
                elif dnd_skills.skills_dict['perception']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='8':
                if dnd_skills.skills_dict['survival']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    sur_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_sur = dnd_class.RaceStats.stat_bonus(sur_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['survival']=updated_sur
                    i+=1
                    break
                elif dnd_skills.skills_dict['survival']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue

            else:
                print("Invalid selection")
                continue

# Setting the saving throws.

    str_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['strength']['mod']),dnd_skills.prof_bonus)
    dex_save = dnd_dict.character_dict['Stats']['dexterity']['mod']
    con_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['constitution']['mod']),dnd_skills.prof_bonus)
    int_save = dnd_dict.character_dict['Stats']['intelligence']['mod']
    wis_save = dnd_dict.character_dict['Stats']['wisdom']['mod']
    cha_save = dnd_dict.character_dict['Stats']['charisma']['mod']

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
    
# Put into the dictionary

    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Getting equipment

    while True:
        weapon_choice1 = input("Choose what your first set of equipment will be:\n1) Chain Mail\n2) Leather Armor, Longbow, and 20 arrows\nEnter your selection: ")
        if weapon_choice1 == '1':
            dnd_dict.character_dict.get("Equipment").append('Chain Mail')
#Chain mail gives an AC of 16
            armor_class = 16
            break

        elif weapon_choice1 == '2':
            dnd_dict.character_dict.get("Equipment").append('Leather Armor')
            dnd_dict.character_dict.get("Equipment").append('Longbow')
            dnd_dict.character_dict.get("Equipment").append('20 Arrows')

# Leather armor (given later) gives an AC of 11 + Dex mod
            armor_class = dnd_weapon.leather_armor()
# Do not print the AC here, since it might be boosted in the next choice with the shield
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice2 = input("Choose what your secondary weapon will be:\n1) A martial weapon and a shield\n2) Two martial weapons\nEnter your selection: ")
        if weapon_choice2 == '1':
            dnd_weapon.martial_weapon()
            dnd_dict.character_dict.get("Equipment").append('Shield')
# Shields give +2 to AC
            armor_class1 = dnd_class.RaceStats.stat_bonus(armor_class,2)
            print("Armor Class: ",armor_class1)
            dnd_dict.character_dict.get("armor_class").append(armor_class1)
            break
 
        elif weapon_choice2 == '2':
            dnd_weapon.double_martial()
# Since there is no bonus, put the regular armor class here
            print("Armor Class: ",armor_class)
            dnd_dict.character_dict.get("armor_class").append(armor_class)
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice3 = input("Choose what your ranged weapon will be:\n1) A light crossbow and 20 bolts\n2) Two handaxes\nEnter your selection: ")
        if weapon_choice3 == '1':
            dnd_dict.character_dict.get("Equipment").append('Light Crossbow, 20 Bolts')
            break

        elif weapon_choice3 == '2':
            dnd_dict.character_dict.get("Equipment").append('Handaxe')
            dnd_dict.character_dict.get("Equipment").append('Handaxe')
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("Choose what your pack will be:\n1) A dungeoneer\'s pack\n2) An explorer\'s pack\nEnter your selection: ")
        if pack_choice == '1':
            dnd_pack.dungeoneer_pack()
            break

        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)


    return


def monk():

    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],16)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d8"),1)
    dnd_dict.character_dict['d8']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per monk level")

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Monk")

    while True:
        tool_choice = input("Select which tool you will be proficient with:\n1) One type of artisan's tools\n2) One musical instrument\nEnter your selection: ")
        if tool_choice == '1':
            dnd_tools.artisan_tools()
            break
 
        elif tool_choice == '2':
            dnd_tools.musical_instrument()
            break

        else:
            print("Invalid Selection")
            continue

# Setting the armor and weapon proficiencies


    weapon_prof = ['Shortswords', 'Simple Weapons']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)

#Selecting the skills
    i = 1
    while i < 3:
        while True:
            print(f'{i}/2')
            choice1 = input("Select the skill you want proficiency in:\n1) Acrobatics\n2) Athletics\n3) History\n4) Insight\n5) Religion\n6) Stealth\nEnter your Selection: ")
            if choice1=='1':
                if dnd_skills.skills_dict['acrobatics']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    acr_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                    updated_acr = dnd_class.RaceStats.stat_bonus(acr_mod, dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['acrobatics'] = updated_acr
                    i+=1
                    break
                elif dnd_skills.skills_dict['acrobatics']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='2':
                if dnd_skills.skills_dict['athletics']==dnd_dict.character_dict['Stats']['strength']['mod']:
                    ath_mod = dnd_dict.character_dict['Stats']['strength']['mod']
                    updated_ath = dnd_class.RaceStats.stat_bonus(ath_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['athletics'] = updated_ath
                    i+=1
                    break
                elif dnd_skills.skills_dict['athletics']>dnd_dict.character_dict['Stats']['strength']['mod']:
                    print("Already proficient")
                    continue
     
            elif choice1=='3':
                if dnd_skills.skills_dict['history']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_his = dnd_class.RaceStats.stat_bonus(his_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['history']=updated_his
                    i+=1
                    break
                elif dnd_skills.skills_dict['history']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='4':
                if dnd_skills.skills_dict['insight']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_ins = dnd_class.RaceStats.stat_bonus(ins_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['insight']=updated_ins
                    i+=1
                    break
                elif dnd_skills.skills_dict['insight']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='5':
                if dnd_skills.skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['religion']=updated_rel
                    i+=1
                    break
                elif dnd_skills.skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='6':
                if dnd_skills.skills_dict['stealth']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    stl_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                    updated_stl = dnd_class.RaceStats.stat_bonus(stl_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['stealth']=updated_stl
                    i+=1
                    break
                elif dnd_skills.skills_dict['stealth']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    print("Already proficient")
                    continue


            else:
                print("Invalid selection")
                continue


# Setting the saving throws.

    str_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['strength']['mod']),dnd_skills.prof_bonus)
    dex_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['dexterity']['mod']),dnd_skills.prof_bonus)
    con_save = dnd_dict.character_dict['Stats']['constitution']['mod']
    int_save = dnd_dict.character_dict['Stats']['intelligence']['mod']
    wis_save = dnd_dict.character_dict['Stats']['wisdom']['mod']
    cha_save = dnd_dict.character_dict['Stats']['charisma']['mod']

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
    
# Put into the dictionary

    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Getting equipment

    while True:
        weapon_choice = input("Choose your primary weapon:\n1) A Shortsword\n2) Any Simple Weapon\nEnter your selection: ")
        if weapon_choice == '1':
            dnd_dict.character_dict.get("Equipment").append('Shortsword')
            break

        elif weapon_choice == '2':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue



    while True:
        pack_choice = input("Choose what your pack will be:\n1) A dungeoneer's pack\n2) An explorer's pack\nEnter your selection: ")
        if pack_choice == '1':
            dnd_pack.dungeoneer_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_dict.character_dict.get("Equipment").append('10 Darts')

    dnd_features.monk_features()


#Armor Class = 10 + Dexterity Modifier + Wisdom Modifier
    armor_class = (10 + dnd_dict.character_dict['Stats']['dexterity']['mod'] + (dnd_dict.character_dict['Stats']['wisdom']['mod']))
    dnd_dict.character_dict.get("armor_class").append(armor_class)
    print("Armor Class: ",armor_class)

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)

    return


def paladin():

    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],20)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d10"),1)
    dnd_dict.character_dict['d10']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d10 per paladin level")

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Paladin")

# Setting the armor and weapon proficiencies
    armor_prof=['Light Armor', 'Medium Armor', 'Heavy Armor', 'Shields']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)
    weapon_prof=['Simple Weapons', 'Martial Weapons']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)

#Selecting the skills
    i = 1
    while i < 3:
        while True:
            print(f'{i}/2')
            choice1 = input("Select the skill you want proficiency in:\n1) Athletics\n2) Insight\n3) Intimidation\n4) Medicine\n5) Persuasion\n6) Religion\nEnter your Selection: ")
            if choice1=='1':
                if dnd_skills.skills_dict['athletics']==dnd_dict.character_dict['Stats']['strength']['mod']:
                    ath_mod = dnd_dict.character_dict['Stats']['strength']['mod']
                    updated_ath = dnd_class.RaceStats.stat_bonus(ath_mod, dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['athletics'] = updated_ath
                    i+=1
                    break
                elif dnd_skills.skills_dict['athletics']>dnd_dict.character_dict['Stats']['strength']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='2':
                if dnd_skills.skills_dict['insight']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_ins = dnd_class.RaceStats.stat_bonus(ins_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['insight'] = updated_ins
                    i+=1
                    break
                elif dnd_skills.skills_dict['insight']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='3':
                if dnd_skills.skills_dict['intimidation']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                    itd_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                    updated_itd = dnd_class.RaceStats.stat_bonus(itd_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['intimidation']=updated_itd
                    i+=1
                    break
                elif dnd_skills.skills_dict['intimidation']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='4':
                if dnd_skills.skills_dict['medicine']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    med_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_med = dnd_class.RaceStats.stat_bonus(med_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['medicine']=updated_med
                    i+=1
                    break
                elif dnd_skills.skills_dict['medicine']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='5':
                if dnd_skills.skills_dict['persuasion']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                    per_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                    updated_per = dnd_class.RaceStats.stat_bonus(per_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['persuasion']=updated_per
                    i+=1
                    break
                elif dnd_skills.skills_dict['persuasion']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='6':
                if dnd_skills.skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['religion']=updated_rel
                    i+=1
                    break
                elif dnd_skills.skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue


            else:
                print("Invalid selection")
                continue


# Setting the saving throws.

    str_save = dnd_dict.character_dict['Stats']['strength']['mod']
    dex_save = dnd_dict.character_dict['Stats']['dexterity']['mod']
    con_save = dnd_dict.character_dict['Stats']['constitution']['mod']
    int_save = dnd_dict.character_dict['Stats']['intelligence']['mod']
    wis_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['wisdom']['mod']),dnd_skills.prof_bonus)
    cha_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['charisma']['mod']),dnd_skills.prof_bonus)

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
    
# Put into the dictionary

    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Getting equipment
    print("Equipment given: chain mail, a holy symbol")

# Chain mail gives a base armor class of 16
    dnd_dict.character_dict.get("Equipment").append('Chain Mail')
    dnd_dict.character_dict.get("Equipment").append('A Holy Symbol')

    while True:
        weapon_choice1 = input("What primary weapon do you want?\n1) A martial weapon and a shield\n2) Two martial weapons\nEnter your selection: ")
        if weapon_choice1 == '1':
            dnd_weapon.martial_weapon()
# Shield gives +2 to armor class
            print("Armor Class: 18")
            dnd_dict.character_dict.get("armor_class").append("18")
            break

        elif weapon_choice1 == '2':
            dnd_weapon.double_martial()
            print("Armor Class: 16")
            dnd_dict.character_dict.get("armor_class").append("16")
            break
        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice2 = input("What secondary weapon do you want?\n1) Five Javelins\n2) Any simple weapon\nEnter your selection: ")
        if weapon_choice2 == '1':
            dnd_dict.character_dict.get("Equipment").append('Javelin (5)')
            break
 
        elif weapon_choice2 == '2':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("What pack do you want?\n1) A priest's pack\n2) An explorer's pack\nEnter your selection: ")
        if pack_choice == '1':
            dnd_pack.priest_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = dnd_class.RaceStats.spell_attack((dnd_dict.character_dict.get("Stats").get("charisma").get('mod')),dnd_skills.prof_bonus)
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict.get("spell_attack").append(spell_attack)

    spell_save = dnd_class.RaceStats.spell_save((dnd_dict.character_dict.get("Stats").get("charisma").get('mod')),dnd_skills.prof_bonus)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict.get("spell_save").append(spell_save)

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)

    dnd_features.paladin_features()
    return


def ranger():

    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],20)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d10"),1)
    dnd_dict.character_dict['d10']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d10 per ranger level")

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Ranger")

# Setting the armor and weapon proficiencies

    armor_prof=['Light Armor', 'Medium Armor', 'Shields']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)
    weapon_prof=['Simple Weapons', 'Martial Weapons']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)

#Selecting the skills
    i = 1
    while i < 4:
        while True:
            print(f'{i}/3')
            choice1 = input("Select the skill you want proficiency in:\n1) Animal Handling\n2) Athletics\n3) Insight\n4) Investigation\n5) Nature\n6) Perception\n7) Stealth\n8) Survival\nEnter your Selection: ")
            if choice1=='1':
                if dnd_skills.skills_dict['animal_handling']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    anm_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_anm = dnd_class.RaceStats.stat_bonus(anm_mod, dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['animal_handling'] = updated_anm
                    i+=1
                    break
                elif dnd_skills.skills_dict['animal_handling']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='2':
                if dnd_skills.skills_dict['athletics']==dnd_dict.character_dict['Stats']['strength']['mod']:
                    ath_mod = dnd_dict.character_dict['Stats']['strength']['mod']
                    updated_ath = dnd_class.RaceStats.stat_bonus(ath_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['athletics'] = updated_ath
                    i+=1
                    break
                elif dnd_skills.skills_dict['athletics']>dnd_dict.character_dict['Stats']['athletics']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='3':
                if dnd_skills.skills_dict['insight']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_ins = dnd_class.RaceStats.stat_bonus(ins_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['insight']=updated_ins
                    i+=1
                    break
                elif dnd_skills.skills_dict['insight']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='4':
                if dnd_skills.skills_dict['investigation']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_inv = dnd_class.RaceStats.stat_bonus(inv_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['investigation']=updated_inv
                    i+=1
                    break
                elif dnd_skills.skills_dict['investigation']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='5':
                if dnd_skills.skills_dict['nature']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_nat = dnd_class.RaceStats.stat_bonus(nat_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['nature']=updated_nat
                    i+=1
                    break
                elif dnd_skills.skills_dict['nature']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='6':
                if dnd_skills.skills_dict['perception']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    prc_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_prc = dnd_class.RaceStats.stat_bonus(prc_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['perception']=updated_prc
                    i+=1
                    break
                elif dnd_skills.skills_dict['perception']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='7':
                if dnd_skills.skills_dict['stealth']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    stl_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                    updated_stl = dnd_class.RaceStats.stat_bonus(stl_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['stealth']=updated_stl
                    i+=1
                    break
                elif dnd_skills.skills_dict['stealth']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='8':
                if dnd_skills.skills_dict['survival']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    sur_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_sur = dnd_class.RaceStats.stat_bonus(sur_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['survival']=updated_sur
                    i+=1
                    break
                elif dnd_skills.skills_dict['survival']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue

            else:
                print("Invalid selection")
                continue

# Setting the saving throws.

    str_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['strength']['mod']),dnd_skills.prof_bonus)
    dex_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['dexterity']['mod']),dnd_skills.prof_bonus)
    con_save = dnd_dict.character_dict['Stats']['constitution']['mod']
    int_save = dnd_dict.character_dict['Stats']['intelligence']['mod']
    wis_save = dnd_dict.character_dict['Stats']['wisdom']['mod']
    cha_save = dnd_dict.character_dict['Stats']['charisma']['mod']

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
# Put into the dictionary
    
    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Getting equipment

# Choose your armor: Leather is 11 + Dex mod.
    while True:
        armor_choice = input("Choose which armor you will take:\n1) Leather Armor\n2) Scale Mail\nEnter your selection: ")
        if armor_choice == '1':
            dnd_dict.character_dict.get("Equipment").append('Leather Armor')
            armor_class = dnd_weapon.leather_armor()
            print("Armor Class: ",armor_class)
            dnd_dict.character_dict.get("armor_class").append(armor_class)
            break
 
        elif armor_choice == '2':
            dnd_dict.character_dict.get("Equipment").append('Scale Mail')
            armor_class = dnd_class.RaceStats.stat_bonus(dnd_class.RaceStats.med_armor(dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")),14)
            print("Armor Class: ",armor_class)
            dnd_dict.character_dict.get("armor_class").append(armor_class)
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice = input("Choose what your secondary weapon will be:\n1) Two shortswords\n2) Two simple melee weapons\nEnter your selection: ")
        if weapon_choice == '1':
            dnd_dict.character_dict.get("Equipment").append('Two Shortswords')
            break
 
        elif weapon_choice == '2':
            dnd_weapon.double_simple_melee()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("Choose what your pack will be:\n1) A dungeoneer\'s pack\n2) An explorer\'s pack\nEnter your selection: ")
        if pack_choice == '1':
            dnd_pack.dungeoneer_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_dict.character_dict.get("Equipment").append('Longbow, 20 Arrows')

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = dnd_class.RaceStats.spell_attack((dnd_dict.character_dict.get("Stats").get("wisdom").get('mod')),dnd_skills.prof_bonus)
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict.get("spell_attack").append(spell_attack)

    spell_save = dnd_class.RaceStats.spell_save((dnd_dict.character_dict.get("Stats").get("wisdom").get('mod')),dnd_skills.prof_bonus)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict.get("spell_save").append(spell_save)

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)



    dnd_language.language()

    dnd_features.ranger_features()
    return


def rogue():

    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],16)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d8"),1)
    dnd_dict.character_dict['d8']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per rogue level")

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Rogue")

# Setting the armor and weapon proficiencies

    weapon_prof = ['Simple Weapons', 'Hand Crossbows', 'Rapiers', 'Longswords','Shortswords']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)

    armor_prof = ['Light Armor']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("Kits"),"Thieves' Tools")
    dnd_dict.character_dict.get("Languages").append('Thieves Cant')

#Selecting the skills
    dnd_skills.rogue_skill_choice()

    dnd_skills.expertise_choice()

# Setting the saving throws.

    str_save = dnd_dict.character_dict['Stats']['strength']['mod']
    dex_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['dexterity']['mod']),dnd_skills.prof_bonus)
    con_save = dnd_dict.character_dict['Stats']['constitution']['mod']
    int_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['intelligence']['mod']),dnd_skills.prof_bonus)
    wis_save = dnd_dict.character_dict['Stats']['wisdom']['mod']
    cha_save = dnd_dict.character_dict['Stats']['charisma']['mod']

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
    
# Put into the dictionary

    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Getting equipment
    while True:
        weapon_choice1 = input("Choose what your primary weapon will be:\n1) A Rapier\n2) A Shortsword\nEnter your selection: ")
        if weapon_choice1 == '1':
            dnd_dict.character_dict.get("Equipment").append('Rapier')
            break
 
        elif weapon_choice1 == '2':
            dnd_dict.character_dict.get("Equipment").append('Shortsword')
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        weapon_choice2 = input("Choose what your secondary weapon will be:\n1) A Shortbow and a quiver of 20 arrows\n2) A Shortsword\nEnter your selection: ")
        if weapon_choice2 == '1':
            dnd_dict.character_dict.get("Equipment").append('Shortbow, 20 Arrows')
            break
 
        elif weapon_choice2 == '2':
            dnd_dict.character_dict.get("Equipment").append('Shortsword')
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("Choose what your pack will be:\n1) A burgler\'s pack\n2) An dungeoneer\'s pack\n3) An explorer\'s pack\nEnter your selection: ")
        if pack_choice == '1':
            dnd_pack.burgler_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.dungeoneer_pack()
            break

        elif pack_choice == '3':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_dict.character_dict.get("Equipment").append('Leather Armor')
    dnd_dict.character_dict.get("Equipment").append('Dagger')
    dnd_dict.character_dict.get("Equipment").append('Dagger')
    dnd_dict.character_dict.get("Equipment").append('Thieves\' Tools')

# Leather armor AC is 11 + Dex mod
    armor_class = dnd_weapon.leather_armor()
    print("Armor Class: ",armor_class)
    dnd_dict.character_dict.get("armor_class").append(armor_class)

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)


    dnd_features.rogue_features()
    return


def sorcerer():

    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],12)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d6"),1)
    dnd_dict.character_dict['d6']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d6 per sorcerer level")

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Sorcerer")

# Setting the armor and weapon proficiencies
    weapon_prof=['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)

#Selecting the skills
    i = 1
    while i < 3:
        while True:
            print(f'{i}/2')
            choice1 = input("Select the skill you want proficiency in:\n1) Arcana\n2) Deception\n3) Insight\n4) Intimidation\n5) Persuasion\n6) Religion\nEnter your Selection: ")
            if choice1=='1':
                if dnd_skills.skills_dict['arcana']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_arc = dnd_class.RaceStats.stat_bonus(arc_mod, dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['arcana'] = updated_arc
                    i+=1
                    break
                elif dnd_skills.skills_dict['arcana']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='2':
                if dnd_skills.skills_dict['deception']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                    dec_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                    updated_dec = dnd_class.RaceStats.stat_bonus(dec_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['deception'] = updated_dec
                    i+=1
                    break
                elif dnd_skills.skills_dict['deception']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='3':
                if dnd_skills.skills_dict['insight']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_ins = dnd_class.RaceStats.stat_bonus(ins_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['insight']=updated_ins
                    i+=1
                    break
                elif dnd_skills.skills_dict['insight']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='4':
                if dnd_skills.skills_dict['intimidation']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                    itd_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                    updated_itd = dnd_class.RaceStats.stat_bonus(itd_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['intimidation']=updated_itd
                    i+=1
                    break
                elif dnd_skills.skills_dict['intimidation']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='5':
                if dnd_skills.skills_dict['persuasion']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                    per_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                    updated_per = dnd_class.RaceStats.stat_bonus(per_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['persuasion']=updated_per
                    i+=1
                    break
                elif dnd_skills.skills_dict['persuasion']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='6':
                if dnd_skills.skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['religion']=updated_rel
                    i+=1
                    break
                elif dnd_skills.skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue


            else:
                print("Invalid selection")
                continue


# Setting the saving throws.

    str_save = dnd_dict.character_dict['Stats']['strength']['mod']
    dex_save = dnd_dict.character_dict['Stats']['dexterity']['mod']
    con_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['constitution']['mod']),dnd_skills.prof_bonus)
    int_save = dnd_dict.character_dict['Stats']['intelligence']['mod']
    wis_save = dnd_dict.character_dict['Stats']['wisdom']['mod']
    cha_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['charisma']['mod']),dnd_skills.prof_bonus)

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
    
# Put into the dictionary

    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Getting equipment
    while True:
        weapon_choice = input("What primary weapon do you want?\n1) A light crossbow with 20 bolts\n2) Any simple weapon\nEnter your selection: ")
        if weapon_choice == '1':
            dnd_dict.character_dict.get("Equipment").append('Light Crossbow')
            dnd_dict.character_dict.get("Equipment").append('20 Bolts')
            break
 
        elif weapon_choice == '2':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        focus_choice = input("What tool will you use to cast your spells?\n1) A component pouch\n2) An arcana focus\nEnter your selection: ")
        if focus_choice == '1':
            dnd_dict.character_dict.get("Equipment").append('Component Pouch')
            break
 
        elif focus_choice == '2':
            dnd_dict.character_dict.get("Equipment").append('An Arcane Focus')
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("What pack do you want?\n1) A dungeoneer's pack\n2) An explorer's pack\nEnter your selection: ")
        if pack_choice == '1':
            dnd_pack.dungeoneer_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_dict.character_dict.get("Equipment").append('Dagger')
    dnd_dict.character_dict.get("Equipment").append('Dagger')



    dnd_magic.sorcerer_magic()

# Choose the subclass
    while True:
        subclass_choice = input("Select your Sorcerous Origin:\n1) Draconic Bloodline\n2) Wild Magic\nEnter your Selection: ")
        if subclass_choice=='1':
            dnd_features.draconic_sorcerer_feature()
#Armor Class = 13 + Dex mod because of DB feature
            armor_class = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")),13)
            dnd_dict.character_dict.get("armor_class").append(armor_class)
            break

        elif subclass_choice=='2':
            dnd_features.wild_magic_sorcerer_feature()
#Armor Class = 10 + Dex mod
            armor_class = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")),10)
            dnd_dict.character_dict.get("armor_class").append(armor_class)
            break

        else:
            print("Invalid Selection")
            continue

    print("Armor Class: ",armor_class)
# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = dnd_class.RaceStats.spell_attack((dnd_dict.character_dict.get("Stats").get("charisma").get('mod')),dnd_skills.prof_bonus)
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict.get("spell_attack").append(spell_attack)

    spell_save = dnd_class.RaceStats.spell_save((dnd_dict.character_dict.get("Stats").get("charisma").get('mod')),dnd_skills.prof_bonus)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict.get("spell_save").append(spell_save)

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)

    return


def warlock():

    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],16)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d8"),1)
    dnd_dict.character_dict['d8']=new_hit_dice

    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d8 per warlock level")

    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Warlock")

# Setting the armor and weapon proficiencies

    armor_prof = ['Light Armor']
    dnd_dict.character_dict.get("Armor_Prof").append(armor_prof)

    weapon_prof = ['Simple Weapons']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)

#Selecting the skills
    i = 1
    while i < 3:
        while True:
            print(f'{i}/2')
            choice1 = input("Select the skill you want proficiency in:\n1) Arcana\n2) Deception\n3) History\n4) Intimidation\n5) Investigation\n6) Nature\n7) Religion\nEnter your Selection: ")
            if choice1=='1':
                if dnd_skills.skills_dict['arcana']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_arc = dnd_class.RaceStats.stat_bonus(arc_mod, dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['arcana'] = updated_arc
                    i+=1
                    break
                elif dnd_skills.skills_dict['arcana']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='2':
                if dnd_skills.skills_dict['deception']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                    dec_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                    updated_dec = dnd_class.RaceStats.stat_bonus(dec_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['deception'] = updated_dec
                    i+=1
                    break
                elif dnd_skills.skills_dict['deception']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='3':
                if dnd_skills.skills_dict['history']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_his = dnd_class.RaceStats.stat_bonus(his_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['history']=updated_his
                    i+=1
                    break
                elif dnd_skills.skills_dict['history']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='4':
                if dnd_skills.skills_dict['intimidation']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                    itd_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                    updated_itd = dnd_class.RaceStats.stat_bonus(itd_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['intimidation']=updated_itd
                    i+=1
                    break
                elif dnd_skills.skills_dict['intimidation']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='5':
                if dnd_skills.skills_dict['investigation']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_inv = dnd_class.RaceStats.stat_bonus(inv_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['investigation']=updated_inv
                    i+=1
                    break
                elif dnd_skills.skills_dict['investigation']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='6':
                if dnd_skills.skills_dict['nature']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_nat = dnd_class.RaceStats.stat_bonus(nat_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['nature']=updated_nat
                    i+=1
                    break
                elif dnd_skills.skills_dict['nature']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='7':
                if dnd_skills.skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['religion']=updated_rel
                    i+=1
                    break
                elif dnd_skills.skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue

            else:
                print("Invalid selection")
                continue

# Setting the saving throws.

    str_save = dnd_dict.character_dict['Stats']['strength']['mod']
    dex_save = dnd_dict.character_dict['Stats']['dexterity']['mod']
    con_save = dnd_dict.character_dict['Stats']['constitution']['mod']
    int_save = dnd_dict.character_dict['Stats']['intelligence']['mod']
    wis_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['wisdom']['mod']),dnd_skills.prof_bonus)
    cha_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['charisma']['mod']),dnd_skills.prof_bonus)

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
    
# Put into the dictionary

    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Getting equipment
    while True:
        weapon_choice = input("What primary weapon do you want?\n1) A light crossbow with 20 bolts\n2) Any simple weapon\nEnter your selection: ")
        if weapon_choice == '1':
            dnd_dict.character_dict.get("Equipment").append('Light Crossbow')
            dnd_dict.character_dict.get("Equipment").append('20 Bolts')
            break

        elif weapon_choice == '2':
            dnd_weapon.simple_weapon()
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        focus_choice = input("What tool will you use to cast your spells?\n1) A component pouch\n2) An arcana focus\nEnter your selection: ")
        if focus_choice == '1':
            dnd_dict.character_dict.get("Equipment").append('Component Pouch')
            break
 
        elif focus_choice == '2':
            dnd_dict.character_dict.get("Equipment").append('Arcane Focus')
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("What pack do you want?\n1) A scholar's pack\n2) A dungeoneer's pack\nEnter your selection: ")
        if pack_choice == '1':
            dnd_pack.scholar_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.dungeoneer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_dict.character_dict.get("Equipment").append('Leather Armor')
    dnd_dict.character_dict.get("Equipment").append('Dagger')
    dnd_dict.character_dict.get("Equipment").append('Dagger')
    dnd_weapon.simple_weapon()
# Leather armor is 11 + Dex mod


    armor_class = dnd_weapon.leather_armor()
    print("Armor Class: ",armor_class)
    dnd_dict.character_dict.get("armor_class").append(armor_class)


# Choose the subclass
    while True:
        subclass_choice = input("Select your patron:\n1) Archfey\n2) Fiend\n3) Great Old One\nEnter your Selection: ")
        if subclass_choice=='1':
            dnd_features.archfey_warlock_feature()
            break

        elif subclass_choice=='2':
            dnd_features.fiend_warlock_feature()
            break

        elif subclass_choice=='3':
            dnd_features.goo_warlock_feature()
            break

        else:
            print("Invalid Selection")
            continue

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = dnd_class.RaceStats.spell_attack((dnd_dict.character_dict.get("Stats").get("charisma").get('mod')),dnd_skills.prof_bonus)
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict.get("spell_attack").append(spell_attack)

    spell_save = dnd_class.RaceStats.spell_save((dnd_dict.character_dict.get("Stats").get("charisma").get('mod')),dnd_skills.prof_bonus)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict.get("spell_save").append(spell_save)

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)


    return


def wizard():

    hp_mod = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("hp")[0],12)
    dnd_dict.character_dict['hp'] = hp_mod
# Set Hit Dice
    dnd_dict.set_hit_dice()
    new_hit_dice = dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict.get("d6"),1)
    dnd_dict.character_dict['d6']=new_hit_dice


    print("Hit Points: ",hp_mod)
    print("Hit Dice: 1d6 per wizard level")


    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("player_class"),"Wizard")

# Setting the armor and weapon proficiencies

    weapon_prof=['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows']
    dnd_dict.character_dict.get("Weapon_Prof").append(weapon_prof)

#Selecting the skills
    i = 1
    while i < 3:
        while True:
            print(f'{i}/2')
            choice1 = input("Select the skill you want proficiency in:\n1) Arcana\n2) History\n3) Insight\n4) Investigation\n5) Medicine\n6) Religion\nEnter your Selection: ")
            if choice1=='1':
                if dnd_skills.skills_dict['arcana']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_arc = dnd_class.RaceStats.stat_bonus(arc_mod, dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['arcana'] = updated_arc
                    i+=1
                    break
                elif dnd_skills.skills_dict['arcana']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='2':
                if dnd_skills.skills_dict['history']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_his = dnd_class.RaceStats.stat_bonus(his_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['history'] = updated_his
                    i+=1
                    break
                elif dnd_skills.skills_dict['history']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='3':
                if dnd_skills.skills_dict['insight']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_ins = dnd_class.RaceStats.stat_bonus(ins_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['insight']=updated_ins
                    i+=1
                    break
                elif dnd_skills.skills_dict['insight']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue

            elif choice1=='4':
                if dnd_skills.skills_dict['investigation']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_inv = dnd_class.RaceStats.stat_bonus(inv_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['investigation']=updated_inv
                    i+=1
                    break
                elif dnd_skills.skills_dict['investigation']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='5':
                if dnd_skills.skills_dict['medicine']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    med_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                    updated_med = dnd_class.RaceStats.stat_bonus(med_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['medicine']=updated_med
                    i+=1
                    break
                elif dnd_skills.skills_dict['medicine']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                    print("Already proficient")
                    continue


            elif choice1=='6':
                if dnd_skills.skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                    updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,dnd_skills.prof_bonus)
                    dnd_skills.skills_dict['religion']=updated_rel
                    i+=1
                    break
                elif dnd_skills.skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                    print("Already proficient")
                    continue

            else:
                print("Invalid selection")
                continue

# Setting the saving throws.

    str_save = dnd_dict.character_dict['Stats']['strength']['mod']
    dex_save = dnd_dict.character_dict['Stats']['dexterity']['mod']
    con_save = dnd_dict.character_dict['Stats']['constitution']['mod']
    int_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['intelligence']['mod']),dnd_skills.prof_bonus)
    wis_save = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict['Stats']['wisdom']['mod']),dnd_skills.prof_bonus)
    cha_save = dnd_dict.character_dict['Stats']['charisma']['mod']

    print("Strength Saving Throw: ",str_save)
    print("Dexterity Saving Throw: ",dex_save)
    print("Constitution Saving Throw: ",con_save)
    print("Intelligence Saving Throw: ",int_save)
    print("Wisdom Saving Throw: ",wis_save)
    print("Charisma Saving Throw: ",cha_save)
# Put into the dictionary
    
    dnd_dict.character_dict['Stats']['strength']['save'] = str_save
    dnd_dict.character_dict['Stats']['dexterity']['save'] = dex_save
    dnd_dict.character_dict['Stats']['constitution']['save'] = con_save
    dnd_dict.character_dict['Stats']['intelligence']['save'] = int_save
    dnd_dict.character_dict['Stats']['wisdom']['save'] = wis_save
    dnd_dict.character_dict['Stats']['charisma']['save'] = cha_save
# Getting equipment
    while True:
        weapon_choice = input("What primary weapon do you want?\n1) A quarterstaff\n2) A dagger\nEnter your selection: ")
        if weapon_choice == '1':
            dnd_dict.character_dict.get("Equipment").append('Quarterstaff')
            break
 
        elif weapon_choice == '2':
            dnd_dict.character_dict.get("Equipment").append('Dagger')
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        focus_choice = input("What tool will you use to cast your spells?\n1) A component pouch\n2) An arcana focus\nEnter your selection: ")
        if focus_choice == '1':
            dnd_dict.character_dict.get("Equipment").append('Component Pouch')
            break
 
        elif focus_choice == '2':
            dnd_dict.character_dict.get("Equipment").append('Arcane Focus')
            break

        else:
            print("Invalid Selection")
            continue

    while True:
        pack_choice = input("What pack do you want?\n1) A scholar's pack\n2) An explorer's pack\nEnter your selection: ")
        if pack_choice == '1':
            dnd_pack.scholar_pack()
            break
 
        elif pack_choice == '2':
            dnd_pack.explorer_pack()
            break

        else:
            print("Invalid Selection")
            continue

    dnd_dict.character_dict.get("Equipment").append('Spellbook')

#Armor Class = 10 + Dex mod
    armor_class = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")),10)

    print("Armor Class: ",armor_class)
    dnd_dict.character_dict.get("armor_class").append(armor_class)

    dnd_magic.wizard_magic()

# Setting the Spell Save DC and Spell Attack Modifiers
    spell_attack = dnd_class.RaceStats.spell_attack((dnd_dict.character_dict.get("Stats").get("intelligence").get('mod')),dnd_skills.prof_bonus)
    print("Spell Attack Modifier: {}".format(spell_attack))
    dnd_dict.character_dict.get("spell_attack").append(spell_attack)

    spell_save = dnd_class.RaceStats.spell_save((dnd_dict.character_dict.get("Stats").get("intelligence").get('mod')),dnd_skills.prof_bonus)
    print("Spell DC: {}".format(spell_save))
    dnd_dict.character_dict.get("spell_save").append(spell_save)

#     Passive perception = 10 + Perception score
    passive_perception = dnd_class.RaceStats.stat_bonus(dnd_skills.skills_dict.get("perception"), 10)
    print("Passive Perception: ",passive_perception)
    dnd_dict.character_dict.get("passive_perception").append(passive_perception)
    return

def player_class():
    if "Artificer" in dnd_dict.character_dict.get("player_class"):
        artificer()

    elif "Barbarian" in dnd_dict.character_dict.get("player_class"):
        barbarian()

    elif "Bard" in dnd_dict.character_dict.get("player_class"):
        bard()

    elif "Cleric" in dnd_dict.character_dict.get("player_class"):
        cleric()

    elif "Druid" in dnd_dict.character_dict.get("player_class"):
        druid()

    elif "Fighter" in dnd_dict.character_dict.get("player_class"):
        fighter()

    elif "Monk" in dnd_dict.character_dict.get("player_class"):
        monk()

    elif "Paladin" in dnd_dict.character_dict.get("player_class"):
        paladin()

    elif "Ranger" in dnd_dict.character_dict.get("player_class"):
        ranger()

    elif "Rogue" in dnd_dict.character_dict.get("player_class"):
        rogue()

    elif "Sorcerer" in dnd_dict.character_dict.get("player_class"):
        sorcerer()

    elif "Warlock" in dnd_dict.character_dict.get("player_class"):
        warlock()

    elif "Wizard" in dnd_dict.character_dict.get("player_class"):
        wizard()

    else:
# If the config.ini has no class selected, delete that from the dictionary.
        del dnd_dict.character_dict.get("player_class")[0]
        while True:
            character_class = input("Choose your class:\n1) Artificer\n2) Barbarian\n3) Bard\n4) Cleric\n5) Druid\n6) Fighter\n7) Monk\n8) Paladin\n9) Ranger\n10) Rogue\n11) Sorcerer\n12) Warlock\n13) Wizard\nEnter your selection: ")
    
            if character_class=='1':
                artificer()
                break

            elif character_class=='2':
                barbarian()
                break

            elif character_class=='3':
                bard()
                break

            elif character_class=='4':
                cleric()
                break

            elif character_class=='5':
                druid()
                break

            elif character_class=='6':
                fighter()
                break

            elif character_class=='7':
                monk()
                break

            elif character_class=='8':
                paladin()
                break

            elif character_class=='9':
                ranger()
                break

            elif character_class=='10':
                rogue()
                break

            elif character_class=='11':
                sorcerer()
                break

            elif character_class=='12':
                warlock()
                break

            elif character_class=='13':
                wizard()
                break

            else:
                print("Invalid input")
                continue
