#!/usr/bin/python3
import random, os, math, json, dnd_features, dnd_tools, dnd_dict, dnd_skills, dnd_race, dnd_class,dnd_language,dnd_pack


def acolyte():
    print("Skill Proficiencies: Insight, Religion")
    dnd_language.double_language()
    dnd_class.RaceStats.pass_function(dnd_dict.character_dict.get("background"),"Acolyte")

    print("Equipment: A holy symbol (a gift to you when you entered the priesthood), a prayer book or prayer wheel, 5 sticks of incense, vestments, a set of common clothes, and a belt pouch containing 15 gp")

# Update skill proficiencies
    dnd_skills.insight_prof()
    dnd_skills.religion_prof()

    dnd_dict.character_dict.get("gold").append("15")

    misc_items = ['A holy symbol (a gift to you when you entered the priesthood)','A prayer book or prayer wheel','Vestments','5 sticks of incense','A set of common clothes']

    dnd_dict.character_dict.get("Misc").append(misc_items)

    dnd_features.acolyte_features()
    return

def anthropologist():
    dnd_language.double_language()

    print("Skill Proficiencies: Insight, Religion")

    dnd_dict.character_dict.get("background").append("Anthropologist")

    print("Equipment: A leather-bound diary, a bottle of ink, an ink pen, a set of traveler's clothes, one trinket of special significance, and a pouch containing 10 gp")

# Update skill proficiencies
    dnd_skills.insight_prof()
    dnd_skills.religion_prof()



    misc_items = ['A leather-bound diary','A bottle of ink','An ink pen','A set of traveler\'s clothes','One trinket of special significance']

    dnd_dict.character_dict.get("Misc").append(misc_items)

    dnd_dict.character_dict.get("gold").append("10")

    dnd_features.anthropologist_features()

    return

def archeologist():
    print("Skill Proficiencies: History, Survival")
    print("Tool proficiencies: Cartographer's Tools or Navigator's Tools")

    dnd_dict.character_dict.get("background").append("Archeologist")
    while True:
        choice = input("Choose your tool proficiency:\n1) Cartographer's Tools\n2) Navigator's Tools\nEnter your selection: ")
        if choice == '1':
            print("Cartographer's Tools Chosen")
            tool_update1 = "Cartographer's Tools"
            dnd_dict.character_dict.get("Tools").append(tool_update1)
            break
 
        elif choice == '2':
            print("Navigator's Tools Chosen")
            tool_update2 = "Navigator's Tools"
            dnd_dict.character_dict.get("Tools").append(tool_update2)
            break

        else:
            print("Invalid entry.")
            continue

    dnd_language.language()

# Update skill proficiencies

    dnd_skills.history_prof()
    dnd_skills.survival_prof()


    print("Equipment: A wooden case containing a map to a ruin or dungeon, a bullseye lantern, a miner's pick, a set of traveler's clothes, a shovel, a two-person tent, a trinket recovered from a dig site, and a pouch containing 25 gp")


    misc_items = ['A wooden case containing a map to a ruin or dungeon','A bullseye lantern','A miner\'s pick','A set of traveler\'s clothes','A shovel','A two person tent','A trinket recovered from a digsite']

    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("25")


    dnd_features.archeologist_features()

    return

def charlatan():
    print("Skill Proficiencies: Deception, Sleight of Hand")
    print("Tool Proficiencies: Disguise Kit, Forgery Kit")

    dnd_dict.character_dict.get("background").append("Charlatan")
    dnd_dict.character_dict.get("Kits").append('Disguise Kit')
    dnd_dict.character_dict.get("Kits").append('Forgery Kit')

# Update skill proficiencies

    dnd_skills.deception_prof()
    dnd_skills.sleight_of_hand_prof()

    print("Equipment A set of fine clothes, a disguise kit, tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke), and a belt pouch containing 15 gp")


    misc_items = ['A fine set of clothes','A disguise kit','Tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke)']
    dnd_dict.character_dict.get("Misc").append(misc_items)


    dnd_dict.character_dict.get("gold").append("15")

    dnd_features.charlatan_features()

    return

def city_watch():
    print("Skill Proficiencies: Athletics, Insight")

    dnd_dict.character_dict.get("background").append("City Watch")
    dnd_language.double_language()

# Update skill proficiencies

    dnd_skills.athletics_prof()
    dnd_skills.insight_prof()

    print("Equipment: A uniform in the style of your unit and indicative of your rank, a horn with which to summon help, a set of manacles, and a pouch containing 10 gp")


    misc_items = ['A uniform in the style of your unit and indicative of your rank','A horn with which to summon help','A set of manacles']
    dnd_dict.character_dict.get("Misc").append(misc_items)

    dnd_dict.character_dict.get("gold").append("10")


    dnd_features.city_watch_features()

    return

def cloistered_scholar():
    print("Skill Proficiencies: History, 1 from Arcana, Nature, or Religion")

    dnd_dict.character_dict.get("background").append("City Watch")
    dnd_language.double_language()


    dnd_skills.history_prof()

    while True:
        choice = input("Choose which skill you want proficiency in:\n1) Arcana\n2) Nature\n3) Religion\nEnter your selection: ")
        if choice =='1':
            if dnd_skills.skills_dict['arcana']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_arc = dnd_class.RaceStats.stat_bonus(arc_mod,dnd_skills.prof_bonus)
                dnd_skills.skills_dict['arcana']=updated_arc
                break
            elif dnd_skills.skills_dict['arcana']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already proficient")
                continue


    
        elif choice =='2':
            if dnd_skills.skills_dict['nature']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_nat = dnd_class.RaceStats.stat_bonus(nat_mod,dnd_skills.prof_bonus)
                dnd_skills.skills_dict['nature']=updated_nat
                print("Nature chosen.")
                break
            elif dnd_skills.skills_dict['nature']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already proficient.")
                continue
    
        elif choice =='3':
            if dnd_skills.skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,dnd_skills.prof_bonus)
                dnd_skills.skills_dict['religion']=updated_rel
                print("Religion chosen.")
                break
            elif dnd_skills.skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already proficient.")
                continue
    
        else:
            print("Invalid input\n")

    print("Equipment: The scholar's robes of your cloister, a writing kit (small pouch with a quill, ink, folded parchment, and a small penknife), a borrowed book on the subject of your current study, and a pouch containing 10 gp")


    misc_items = ['The scholar\'s robes of your cloister','A writing kit (small pouch with a quill, ink, folded parchment, and a small penknife','A borrowed book on the subject of your current study']
    dnd_dict.character_dict.get("Misc").append(misc_items)

    dnd_dict.character_dict.get("gold").append("10")


    dnd_features.cloistered_scholar_features()

    return

def criminal():
    print("Skill Proficiencies: Deception, Stealth")
    print("Tool Proficiencies: One Type of Gaming Set, Thieves' Tools")
    print("Equipment: A crowbar, a set of dark common clothes including a hood, and a belt pouch containing 15 gp")

    dnd_dict.character_dict.get("background").append("Criminal")
    dnd_dict.character_dict.get("Kits").append('Thieves\' Tools')
    dnd_tools.gaming_set()

# Update skill proficiencies
    dnd_skills.deception_prof()
    dnd_skills.stealth_prof()


    misc_items = ['A crowbar','A set of dark clothes, including a hood']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("15")


    dnd_features.criminal_features()

    return

def entertainer():
    print("Skill Proficiencies: Acrobatics, Performance")
    print("Tool Proficiencies: Disguise kit, One Type of Musical Instument")
    print("Equipment: A musical instrument (one of your choice), the favor of an admirer (love letter, lock of hair, or trinket), a costume, and a belt pouch containing 15 gp")


    dnd_dict.character_dict.get("background").append("Entertainer")
    dnd_dict.character_dict.get("Kits").append('Disguise Kit')
 

# Update skill proficiencies
    dnd_skills.acrobatics_prof()
    dnd_skills.performance_prof()

    dnd_tools.musical_instrument()
    musical_equip = input("What instrument do you want to take? ")
    dnd_dict.character_dict.get("Equipment").append(musical_equip)

    misc_items = ['The favor of an admirer (love letter, a lock of hair, or a trinket)','A costume']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("15")


    dnd_features.entertainer_features()

    return

def far_traveler():
    print("Skill Proficiencies: Insight, Perception")
    print("Tool Proficiencies: One Instrument and One Gaming Set")

    dnd_dict.character_dict.get("background").append("Far Traveler")
    dnd_language.language()
    gaming_set = dnd_tools.gaming_set()


    print("Equipment: One set of traveler's clothes, any one musical instrument or gaming set you are proficient with, poorly wrought maps from your homeland that depict where you are in the world, a small piece of jewelry worth 10 gp in the style of your homeland's craftsmanship, and a pouch containing 5 gp")

# Update skill proficiencies
    dnd_skills.insight_prof()
    dnd_skills.perception_prof()

    musical_equip = dnd_tools.musical_instrument()

    misc_items = ['One set of traveler\'s clothes','Poorly wrought maps from your homeland that depicts where you are in the world','A small piece of jewlery worth 10 gp in the style of your homeland\'s craftsmanship']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("5")

    dnd_features.far_traveler_features()
    return

def folk_hero():
    print("Skill Proficiencies: Animal Handling, Survival")
    print("Tool Proficiencies: One Type of Artisan's Tools, Vehicles(Land)")
    print("Equipment: A shovel, an iron pot, a set of common clothes, and a belt pouch containing 10 gp")

    dnd_dict.character_dict.get("background").append("Folk Hero")
    dnd_tools.artisan_tools()

# Update skill proficiencies
    dnd_skills.animal_handling_prof()
    dnd_skills.survival_prof()


    dnd_dict.character_dict.get("Vehicles").append('Land')

    misc_items = ['One set of common clothes','A shovel','An iron pot']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("10")

    dnd_features.folk_hero_features()
    return

def gladiator():
    print("Skill Proficiencies: Acrobatics, Performance")
    print("Tool Proficiencies: Disguise kit, One Type of Musical Instument")
    print("Equipment: A musical instrument (one of your choice), the favor of an admirer (love letter, lock of hair, or trinket), a costume, and a belt pouch containing 15 gp")

    dnd_dict.character_dict.get("background").append("Gladiator")

# Update skill proficiencies
    dnd_skills.acrobatics_prof()
    dnd_skills.performance_prof()


    dnd_dict.character_dict.get("Kits").append('Disguise Kit')
    dnd_tools.musical_instrument()

    gold_update = {'gold':15}

    musical_equip = input("What instrument do you want to take? ")
    dnd_dict.character_dict.get("Equipment").append(musical_equip)

    misc_items = ['The favor of an admirer (love letter, a lock of hair, or a trinket)','A costume']
    dnd_dict.character_dict.get("Misc").append(misc_items)

    dnd_features.gladiator_features()
    return

def guild_artisan():
    print("Skill Proficiencies: Insight, Persuasion")
    dnd_language.language()

    dnd_dict.character_dict.get("background").append("Guild Artisan")

# Update skill proficiencies
    dnd_skills.insight_prof()
    dnd_skills.persuasion_prof()


    print("Equipment: A set of artisan's tools (one of your choice), a letter of introduction from your guild, a set of traveler's clothes, and a belt pouch containing 15 gp")


    dnd_tools.artisan_tools_equip()

    misc_items = ['A set of traveler\'s clothes','A letter of introduction from your guild']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("15")


    dnd_features.guild_artisan_features()
    return

def guild_merchant():
    print("Skill Proficiencies: Insight, Persuasion")
    print("Tool Proficiency: navigator's tools")
    dnd_language.double_language()

    dnd_dict.character_dict.get("background").append("Guild Merchant")
    dnd_dict.character_dict.get("Tools").append('Navigator\'s Tools')

# Update skill proficiencies
    dnd_skills.insight_prof()
    dnd_skills.persuasion_prof()

    print("Equipment A mule and a cart, a letter of introduction from your guild, a set of traveler's clothes, and a belt pouch containing 15 gp")


    misc_items = ['A mule and a cart','A set of traveler\'s clothes','A letter of introduction from your guild']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("15")

    dnd_features.guild_merchant_features()
    return

def haunted_one():
    print("Skill Proficiencies: Two of Arcana, Investigation, Religion, or Survival")
    print("Equipment: Monster hunter’s pack, a set of common clothes, one trinket of special significance")
 
    dnd_dict.character_dict.get("background").append("Haunted One")

    dnd_pack.monster_hunter_pack()
    misc_items = ['A set of common clothes','One trinket of special significance']
    dnd_dict.character_dict.get("Misc").append(misc_items)

    while True:
        choice1 = input("Select the first of two skill proficiencies you want:\n1) Arcana\n2) Investigation\n3) Religion\n4) Survival\nEnter your selection: ")
        if choice1=='1':
            if dnd_skills.skills_dict['arcana']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_arc = dnd_class.RaceStats.stat_bonus(arc_mod,dnd_skills.prof_bonus)
                dnd_skills.skills_dict['arcana']=updated_arc
                break
            elif dnd_skills.skills_dict['arcana']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already Proficient")
                continue
 
        elif choice1=='2':
            if dnd_skills.skills_dict['investigation']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_inv = dnd_class.RaceStats.stat_bonus(inv_mod,dnd_skills.prof_bonus)
                dnd_skills.skills_dict['investigation']=updated_inv
                break
            elif dnd_skills.skills_dict['investigation']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already Proficient")
                continue
 
        elif choice1=='3':
            if dnd_skills.skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,dnd_skills.prof_bonus)
                dnd_skills.skills_dict['religion']=updated_rel
                break
            elif dnd_skills.skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already Proficient")
                continue
 
        elif choice1=='4':
            if dnd_skills.skills_dict['survival']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                sur_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                updated_sur = dnd_class.RaceStats.stat_bonus(sur_mod,dnd_skills.prof_bonus)
                dnd_skills.skills_dict['survival']=updated_sur
                break
            elif dnd_skills.skills_dict['survival']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                print("Already Proficient")
                continue

        else:
            print("Invalid Selection")
            continue


    while True:
        choice2 = input("Select the first of two skill proficiencies you want:\n1) Arcana\n2) Investigation\n3) Religion\n4) Survival\nEnter your selection: ")
        if choice2=='1':
            if dnd_skills.skills_dict['arcana']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_arc = dnd_class.RaceStats.stat_bonus(arc_mod,dnd_skills.prof_bonus)
                dnd_skills.skills_dict['arcana']=updated_arc
                break
            elif dnd_skills.skills_dict['arcana']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already Proficient")
                continue
 
        elif choice2=='2':
            if dnd_skills.skills_dict['investigation']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_inv = dnd_class.RaceStats.stat_bonus(inv_mod,dnd_skills.prof_bonus)
                dnd_skills.skills_dict['investigation']=updated_inv
                break
            elif dnd_skills.skills_dict['investigation']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already Proficient")
                continue
 
        elif choice2=='3':
            if dnd_skills.skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,dnd_skills.prof_bonus)
                dnd_skills.skills_dict['religion']=updated_rel
                break
            elif dnd_skills.skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already Proficient")
                continue
 
        elif choice2=='4':
            if dnd_skills.skills_dict['survival']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                sur_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                updated_sur = dnd_class.RaceStats.stat_bonus(sur_mod,dnd_skills.prof_bonus)
                dnd_skills.skills_dict['survival']=updated_sur
                break
            elif dnd_skills.skills_dict['survival']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                print("Already Proficient")
                continue

        else:
            print("Invalid Selection")
            continue


    dnd_language.exotic_language()
    dnd_dict.character_dict.get("gold").append("0")

    dnd_features.haunted_one_features()
    return

def hermit():
    print("Skill Proficiencies: Medicine, Religion")
    print("Tool Proficiency: Herbalism Kit")
    print("Equipment: A scroll case stuffed full of notes from your studies or prayers, a winter blanket, a set of common clothes, an herbalism kit, and 5 gp")

    dnd_dict.character_dict.get("background").append("Hermit")
    dnd_dict.character_dict.get("Kits").append('Herbalism Kit')


# Update skill proficiencies
    dnd_skills.medicine_prof()
    dnd_skills.religion_prof()

    dnd_dict.character_dict.get("Equipment").append('Herbalism Kit')
    misc_items = ['A scroll case stuffed full of notes from your studies or prayers','A set of common clothes','A winter blanket']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("5")

    dnd_language.language()

    dnd_features.hermit_features()
    return


def inquisitor():
    print("Skill Proficiencies: Investigation, Religion")
    print("Tool Proficiencies: Thieves' Tools, one set of artisan's tools of your choice")
    print("Equipment: A holy symbol, a set of traveler’s clothes, and a belt pouch containing 15 gp")

    dnd_dict.character_dict.get("background").append("Inquisitor")
    dnd_tools. artisan_tools()
    dnd_dict.character_dict.get("Kits").append('Thieves\' Tools')

# Update skill proficiencies
    dnd_skills.investigation_prof()
    dnd_skills.religion_prof()

    misc_items = ['A holy symbol','A set of traveler\'s clothes']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("15")


    dnd_features.inquisitor_features()
    return

def investigator():
    print("Skill Proficiencies: Athletics, Insight")
    print("Equipment: A uniform in the style of your unit and indicative of your rank, a horn with which to summon help, a set of manacles, and a pouch containing 10 gp")

    dnd_language.double_language()

    dnd_dict.character_dict.get("background").append("Investigator")

# Update skill proficiencies
    dnd_skills.athletics_prof()
    dnd_skills.insight_prof()

    misc_items = ['A uniform in the style of your unit and indicative of your rank','A horn with which to summon help','A set of manacles']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("10")


    dnd_features.investigator_features()
    return

def knight():
    print("Skill Proficiencies: History, Persuasion")
    print("Tool Proficiencies: One Type of Gaming Set")
    print("Equipment: A set of fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25 gp")

    dnd_language.language()
    dnd_dict.character_dict.get("background").append("Knight")

# Update skill proficiencies
    dnd_skills.history_prof()
    dnd_skills.persuasion_prof()


    dnd_tools.gaming_set()


    misc_items = ['A set of fine clothes','A signit ring','A scroll of pedigree']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("25")

    dnd_features.knight_features()
    return

def marine():
    print("Skill Proficiencies: Athletics, Survival")
    print("Tool Proficiencies: Vehicles (Land & Water)")
    print("Equipment: A dagger that belonged to a fallen comrade, a folded rag emblazoned with the symbol of your ship or company, a set of traveler's clothes, and a belt pouch containing 10 gp")

    dnd_dict.character_dict.get("background").append("Marine")
# Update skill proficiencies
    dnd_skills.athletics_prof()
    dnd_skills.survival_prof()


    dnd_dict.character_dict.get("Vehicles").append('Land')
    dnd_dict.character_dict.get("Vehicles").append('Water')


    misc_items = ['A dagger that belonged to a fallen comrade','A folded rag emblazoned with the symbol of your ship or company','A set of traveler\'s clothes']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("10")

    dnd_features.marine_features()
    return

def mercenary():
    print("Skill Proficiencies: Athletics, Persuasion")
    print("Tool Proficiencies: One Type of Gaming Set, Vehicles(Land)")
    print("Equipment: A uniform of your company (traveler's clothes in quality), an insignia of your rank, a gaming set of your choice, and a pouch containing the remainder of your last wages (10 gp)")

    dnd_dict.character_dict.get("background").append("Mercenary")
    dnd_tools.gaming_set()

# Update skill proficiencies
    dnd_skills.athletics_prof()
    dnd_skills.persuasion_prof()


    misc_items = ['A uniform of your company (traveler\'s clothes in quality','An insignia of your rank']
    dnd_dict.character_dict.get("Misc").append(misc_items)

# Choose the gaming set you want to have
    while True:
        choice=input("Choose the gaming set you want to have:\n1) Dice Game\n2) Card Game\nEnter your selection: ")
        if choice == '1':
            print("Dice Chosen")
            dnd_dict.character_dict.get("Misc").append("Dice Game")
            break

        elif choice == '2':
            print("Cards Chosen")
            dnd_dict.character_dict.get("Misc").append("Card Game")
            break

        else:
            print("Invalid Selection")
            continue

    dnd_dict.character_dict.get("gold").append("10")

    dnd_features.mercenary_features()
    return

def noble():

    print("Skill Proficiencies: History, Persuasion")
    print("Tool Proficiencies: One Type of Gaming Set")
    print("Equipment: A set of fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25 gp")

    dnd_language.language()
    dnd_tools.gaming_set()
    dnd_dict.character_dict.get("background").append("Noble")

# Update skill proficiencies
    dnd_skills.history_prof()
    dnd_skills.persuasion_prof()

    misc_items = ['A set of fine clothes','A signit ring','A scroll of pedigree']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("25")

    dnd_features.noble_features()
    return

def outlander():
    print("Skill Proficiencies: Athletics, Survival")
    print("Tool Proficiencies: One Type of Musical Instrument")
    print("Equipment: A staff, a hunting trap, a trophy from an animal you killed, a set of traveler's clothes, and a belt pouch containing 10 gp")

    dnd_language.language()
    dnd_tools.musical_instrument()
    dnd_dict.character_dict.get("background").append("Outlander")

# Update skill proficiencies
    dnd_skills.athletics_prof()
    dnd_skills.survival_prof()


    misc_items = ['A staff','A hunting trap','A trophy from an animal you killed','A set of traveler\'s clothes']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("10")

    dnd_features.outlander_features()
    return

def pirate():
    print("Skill Proficiencies: Athletics, Perception")
    print("Tool Proficiencies: Navigator's Tools, Vehicles(Water)")
    print("Equipment: A belaying pin (club), 50 feet of silk rope, a lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table in chapter 5), a set of common clothes, and a belt pouch containing 10 gp")

    dnd_dict.character_dict.get("background").append("Pirate")

# Update skill proficiencies
    dnd_skills.athletics_prof()
    dnd_skills.perception_prof()

    dnd_dict.character_dict.get("Tools").append('Navigator\'s Tools')
    dnd_dict.character_dict.get("Vehicles").append('Water')


    misc_items = ['A belaying pin(club)','50 feet of silk rope','A lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table in chapter 5)','A set of common clothes']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("10")

    dnd_features.pirate_features()
    return

def sage():
    print("Skill Proficiencies: Arcana, History")

    dnd_language.double_language()
    dnd_dict.character_dict.get("background").append("Sage")

# Update skill proficiencies
    dnd_skills.arcana_prof()
    dnd_skills.history_prof()

    print("Equipment: A bottle of black ink, a quill, a small knife, a letter from a dead colleague posing a question you have not yet been able to answer, a set of common clothes, and a belt pouch containing 10 gp")

    misc_items = ['A bottle of black ink','A quill','A letter from a dead colleague posing a question you have not yet been able to answer','A set of common clothes']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("10")

    dnd_features.sage_features()
    return

def sailor():
    print("Skill Proficiencies: Athletics, Perception")
    print("Tool Proficiencies: Navigator's Tools, Vehicles(Water)")
    print("Equipment: A belaying pin (club), 50 feet of silk rope, a lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table in chapter 5), a set of common clothes, and a belt pouch containing 10 gp")

    dnd_dict.character_dict.get("background").append("Sailor")
# Update skill proficiencies
    dnd_skills.athletics_prof()
    dnd_skills.perception_prof()

    dnd_dict.character_dict.get("Tools").append('Navigator\'s Tools')
    dnd_dict.character_dict.get("Vehicles").append('Water')

    misc_items = ['A belaying pin(club)','50 feet of silk rope','A lucky charm such as a rabbit foot or a small stone with a hole in the center (or you may roll for a random trinket on the Trinkets table in chapter 5)','A set of common clothes']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("10")

    dnd_features.sailor_features()
    return

def soldier():
    print("Skill Proficiencies: Athletics, Intimidation")
    print("Tool Proficiencies: One Type of Gaming Set, Vehicles (Land)")
    print("Equipment: An insignia of rank, a trophy taken from a fallen enemy (a dagger, broken blade, or piece of a banner), a set of bone dice or deck of cards, a set of common clothes, and a belt pouch containing 10 gp")

    dnd_tools.gaming_set()
    dnd_dict.character_dict.get("background").append("Soldier")

# Update skill proficiencies
    dnd_skills.athletics_prof()
    dnd_skills.intimidation_prof()

    dnd_dict.character_dict.get("Vehicles").append('Land')



    misc_items = ['An insignia of rank','A trophy taken from a fallen enemy (a dagger, broken blade, or a piece of a banner)','A set of common clothes']
    dnd_dict.character_dict.get("Misc").append(misc_items)

    while True:
        choice=input("Choose the gaming set you want to have:\n1) Dice Game\n2) Card Game\nEnter your selection: ")
        if choice == '1':
            print("Dice Chosen")
            dnd_dict.character_dict.get("Misc").append("Dice Game")
            break

        elif choice == '2':
            print("Cards Chosen")
            dnd_dict.character_dict.get("Misc").append("Card Game")
            break

        else:
            print("Invalid Selection")
            continue

    dnd_dict.character_dict.get("gold").append("10")

    dnd_features.soldier_features()
    return

def spy():
    print("Proficiencies: Deception, Stealth")
    print("Tools: One Type of Gaming Set, Thieves' Tools")
    print("Equipment: A crowbar, a set of dark common clothes including a hood, and a belt pouch containing 15 gp")

    dnd_tools.gaming_set()
    dnd_dict.character_dict.get("Kits").append('Thieves\' Tools')
    dnd_dict.character_dict.get("background").append("Spy")

# Update skill proficiencies
    dnd_skills.deception_prof()
    dnd_skills.stealth_prof()

    gold_update = {'gold':15}

    misc_items = ['A crowbar','A set of dark clothes, including a hood']
    dnd_dict.character_dict.get("Misc").append(misc_items)

    dnd_features.spy_features()
    return


def urban_bounty_hunter():
    print("Skill Proficiencies: Choose Two From Deception, Persuasion, and Stealth")
    print("Tool Proficiencies: Two From Among One Type of Gaming Set, One Musical Instrument, and Thieves' Tools")
    print("Equipment: A set of clothes appropriate to your duties and a pouch containing 20 gp")

    dnd_dict.character_dict.get("background").append("Urban Bounty Hunter")
#Choosing the Tool Proficiencies
    while True:
       choice1 =input("Select your first choice:\n1) One Instrument\n2) One Type of Gaming Set\n3) Thieves' Tools\nEnter your selection: ")
       if choice1=='1':
           dnd_tools.musical_instrument()
           break

       elif choice1=='2':
           dnd_tools.gaming_set()
           break

       elif choice1=='3':
           print("Thieves\' Tools selected")
           dnd_tools.character_dict.get("Kits").append('Thieves\' Tools')
           break

       else:
           print("Invalid Selection")
           continue

    while True:
        choice2 =input("Select your second choice:\n1) One Musical Instrument\n2) One Gaming Set\n3) Thieves' Tools\nEnter your selection: ")
        if choice2=='1':
            if choice1=='1':
                print("Already Selected")
                continue
            else: 
                dnd_tools.musical_instrument()
                break

        elif choice2=='2':
            if choice1=='2':
                print("Already Selected")
                continue
            else:
                dnd_tools.gaming_set()
                break

        elif choice2=='3':
            if choice1=='3':
                print("Already Selected")
                continue
            else:
                print("Thieves\' Tools selected")
                dnd_tools.character_dict.get("Kits").append('Thieves\' Tools')
                break

        else:
            print("Invalid Selection")
            continue

#Choose your skills, if proficient with all three skills, then continue with the program.
    i = 1
    while i < 3:
        if dnd_skills.skills_dict['deception']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['charisma']['mod'],dnd_skills.prof_bonus) and dnd_skills.skills_dict['persuasion']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['charisma']['mod'],dnd_skills.prof_bonus) and dnd_skills.skills_dict['stealth']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['dexterity']['mod'],dnd_skills.prof_bonus):
            print("You are proficient with all three skills. Continuing with the program.")
            i+=2
            break
        else:
            while True:
                print(f'{i}/2')
                choice1 = input("Select the skill proficiencies you want:\n1) Deception\n2) Persuasion\n3) Stealth\nEnter your selection: ")
                if choice1=='1':
                    if dnd_skills.skills_dict['deception']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                        dec_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                        updated_dec = dnd_class.RaceStats.stat_bonus(dec_mod,dnd_skills.prof_bonus)
                        dnd_skills.skills_dict['deception']=updated_dec
                        i+=1
                        break
                    elif dnd_skills.skills_dict['deception']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                        print("Already Proficient")
                        continue

                elif choice1=='2':
                    if dnd_skills.skills_dict['persuasion']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                        per_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                        updated_per = dnd_class.RaceStats.stat_bonus(per_mod,dnd_skills.prof_bonus)
                        dnd_skills.skills_dict['persuasion']=updated_per
                        i+=1
                        break
                    elif dnd_skills.skills_dict['persuasion']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                        print("Already Proficient")
                        continue

                elif choice1=='3':
                    if dnd_skills.skills_dict['stealth']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                        stl_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                        updated_stl = dnd_class.RaceStats.stat_bonus(stl_mod,dnd_skills.prof_bonus)
                        dnd_skills.skills_dict['stealth']=updated_stl
                        i+=1
                        break
                    elif dnd_skills.skills_dict['stealth']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                        print("Already Proficient")
                        continue

                else:
                   print("Invalid Selection")
                   continue





    dnd_dict.character_dict.get("Misc").append('A set of clothes appropriate to your duties')
    dnd_dict.character_dict.get("gold").append("20")

    dnd_features.urban_bounty_hunter_features()
    return

def urchin():
    print("Skill Proficiencies: Sleight of Hand, Stealth")
    print("Tool Proficiencies: Disguise Kit, Thieves' Tools")
    print("Equipment: A small knife, a map of the city you grew up in, a pet mouse, a token to remember your parents by, a set of common clothes, and a belt pouch containing 10 gp")

    dnd_dict.character_dict.get("background").append("Urchin")
# Update skill proficiencies
    dnd_skills.sleight_of_hand_prof()
    dnd_skills.stealth_prof()

    dnd_dict.character_dict.get("Tools").append('Disguise Kit')
    dnd_dict.character_dict.get("Tools").append('Thieves\' Tools')

    misc_items = ['A small knife','A map of the city you grew up in','A pet mouse','A token to remember your parents by','A set of common clothes']
    dnd_dict.character_dict.get("Misc").append(misc_items)
    dnd_dict.character_dict.get("gold").append("10")

    dnd_features.urchin_features()
    return

def player_background():
# If the user used the config file, automatically go to the background they selected
    if "Acolyte" in dnd_dict.character_dict.get("background"):
        acolyte()

    elif "Anthropologist" in dnd_dict.character_dict.get("background"):
        anthropologist()

    elif "Archeologist" in dnd_dict.character_dict.get("background"):
        archeologist()

    elif "Charlatan" in dnd_dict.character_dict.get("background"):
        charlatan()

    elif "City Watch" in dnd_dict.character_dict.get("background"):
        city_watch()

    elif "Cloistered Scholar" in dnd_dict.character_dict.get("background"):
        cloistered_scholar()

    elif "Criminal" in dnd_dict.character_dict.get("background"):
        criminal()

    elif "Entertainer" in dnd_dict.character_dict.get("background"):
        entertainer()

    elif "Far Traveler" in dnd_dict.character_dict.get("background"):
        far_traveler()

    elif "Folk Hero" in dnd_dict.character_dict.get("background"):
        folk_hero()

    elif "Gladiator" in dnd_dict.character_dict.get("background"):
        gladiator()

    elif "Guild Artisan" in dnd_dict.character_dict.get("background"):
        guild_artisan()

    elif "Guild Merchant" in dnd_dict.character_dict.get("background"):
        guild_merchant()

    elif "Haunted One" in dnd_dict.character_dict.get("background"):
        haunted_one()

    elif "Hermit" in dnd_dict.character_dict.get("background"):
        hermit()

    elif "Inquisitor" in dnd_dict.character_dict.get("background"):
        inquisitor()

    elif "Investigator" in dnd_dict.character_dict.get("background"):
        investigator()

    elif "Knight" in dnd_dict.character_dict.get("background"):
        knight()

    elif "Marine" in dnd_dict.character_dict.get("background"):
        marine()

    elif "Mercenary" in dnd_dict.character_dict.get("background"):
        mercenary()

    elif "Noble" in dnd_dict.character_dict.get("background"):
        noble()

    elif "Outlander" in dnd_dict.character_dict.get("background"):
        outlander()

    elif "Pirate" in dnd_dict.character_dict.get("background"):
        pirate()

    elif "Sage" in dnd_dict.character_dict.get("background"):
        sage()

    elif "Sailor" in dnd_dict.character_dict.get("background"):
        sailor()

    elif "Soldier" in dnd_dict.character_dict.get("background"):
        soldier()

    elif "Spy" in dnd_dict.character_dict.get("background"):
        spy()

    elif "Urban Bounty Hunter" in dnd_dict.character_dict.get("background"):
        urban_bounty_hunter()

    elif "Urchin" in dnd_dict.character_dict.get("background"):
        urchin()

    else:
# If the config.ini has no background selected, delete that from the dictionary.
        del dnd_dict.character_dict.get("background")[0]
        while True:
            background_choice = input("Choose your background:\n1) Acolyte\n2) Anthropologist\n3) Archeologist\n4) Charlatan\n5) City Watch\n6) Cloistered Scholar\n7) Criminal\n8) Entertainer\n9) Far Traveler\n10) Folk Hero\n11) Gladiator\n12) Guild Artisan\n13) Guild Merchant\n14) Haunted One\n15) Hermit\n16) Inquisitor\n17) Investigator\n18) Knight\n19) Marine\n20) Mercenary\n21) Noble\n22) Outlander\n23) Pirate\n24) Sage\n25) Sailor\n26) Soldier\n27) Spy\n28) Urban Bounty Hunter\n29) Urchin\nEnter your selection: ")

            if background_choice == '1':
                acolyte()
                break
 
            elif background_choice == '2':
                anthropologist()
                break

            elif background_choice == '3':
                archeologist()
                break

            elif background_choice == '4':
                charlatan()
                break

            elif background_choice == '5':
                city_watch()
                break

            elif background_choice == '6':
                cloistered_scholar()
                break

            elif background_choice == '7':
                criminal()
                break

            elif background_choice == '8':
                entertainer()
                break

            elif background_choice == '9':
                far_traveler()
                break

            elif background_choice == '10':
                folk_hero()
                break

            elif background_choice == '11':
                gladiator()
                break

            elif background_choice == '12':
                guild_artisan()
                break

            elif background_choice == '13':
                guild_merchant()
                break

            elif background_choice == '14':
                haunted_one()
                break

            elif background_choice == '15':
                hermit()
                break

            elif background_choice == '16':
                inquisitor()
                break

            elif background_choice == '17':
                investigator()
                break

            elif background_choice == '18':
                knight()
                break

            elif background_choice == '19':
                marine()
                break

            elif background_choice == '20':
                mercenary()
                break

            elif background_choice == '21':
                noble()
                break

            elif background_choice == '22':
                outlander()
                break

            elif background_choice == '23':
                pirate()
                break

            elif background_choice == '24':
                sage()
                break

            elif background_choice == '25':
                sailor()
                break

            elif background_choice == '26':
                soldier()
                break

            elif background_choice == '27':
                spy()
                break

            elif background_choice == '28':
                urban_bounty_hunter()
                break

            elif background_choice == '29':
                urchin()
                break

            else:
                print("Invalid input")
                continue
