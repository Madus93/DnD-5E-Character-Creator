#!/usr/bin/python3
import dnd_dict

# Checks if the spell is selected. If it is, redo the choice
def spell_check(u_spell,spell_list):
    if any(u_spell in spell for spell in spell_list):
        return True

# Artificer Cantrips
def artificer_cantrip():
    while True:
        check_spell = dnd_dict.character_dict.get("cantrip")
        choice = input("Choose your cantrips:\n1) Acid Splash\n2) Booming Blade\n3) Create Bonfire\n4) Dancing Lights\n5) Fire Bolt\n6) Frostbite\n7) Green-Flame Blade\n8) Guidance\n9) Light\n10) Lightning Lure\n11) Mage Hand\n12) Magic Stone\n13) Mending\n14) Message\n15) Poison Spray\n16) Prestidigitation\n17) Ray of Frost\n18) Resistance\n19) Shocking Grasp\n20) Spare the Dying\n21) Sword Burst\n22) Thorn Whip\n23) Thunderclap\nEnter your selection: ")
        if choice =='1':
            spell_picked = 'Acid Splash'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Booming Blade'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Create Bonfire'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Dancing Lights'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Fire Bolt'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Frostbite'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Green-Flame Blade'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Guidance'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Light'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Lightning Lure'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Mage Hand'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Magic Stone'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Mending'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='14':
            spell_picked = 'Message'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='15':
            spell_picked = 'Poison Spray'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='16':
            spell_picked = 'Prestidigitation'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='17':
            spell_picked = 'Ray of Frost'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='18':
            spell_picked = 'Resistance'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='19':
            spell_picked = 'Shocking Grasp'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='20':
            spell_picked = 'Spare the Dying'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='21':
            spell_picked = 'Sword Burst'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='22':
            spell_picked = 'Thorn Whip'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='23':
            spell_picked = 'Thunderclap'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        else:
            print("Invalid Input")
            continue

def artificer_first():
        art_magic=['Absorb Elements', 'Alarm', 'Catapult', 'Cure Wounds', 'Detect Magic', 'Disguise Self', 'Expeditious Retreat', 'Faerie Fire', 'False Life', 'Feather Fall', 'Grease', 'Identify', 'Jump', 'Longstrider', 'Purify Food and Drink', 'Sanctuary', 'Snare', 'Tasha\'s Caustic Brew']
        dnd_dict.character_dict.get("first_level").append(art_magic)

# Select two artificer cantrips and get all 1st level spells\
def artificer_magic():
    x=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            artificer_cantrip()
            x+=1
        elif x == 3:
            artificer_first()
            x+=1
            break

def bard_cantrip():
    while True:
        check_spell = dnd_dict.character_dict.get("cantrip")
        choice = input("Choose your cantrips:\n1) Blade Ward\n2) Dancing Lights\n3) Friends\n4) Light\n5) Mage Hand\n6) Mending\n7) Message\n8) Minor Illusion\n9) Prestidigitation\n10) Thunderclap\n11) True Strike\n12) Vicious Mockery\nEnter your selection: ") 

        if choice =='1':
            spell_picked = 'Blade Ward'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Dancing Lights'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Friends'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Light'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Mage Hand'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Mending'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Message'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Minor Illusion'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Prestidigitation'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Thunderclap'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'True Strike'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Vicious Mockery'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break
        else:
            print("Invalid Input")
            continue

def bard_first():
    while True:
        check_spell = dnd_dict.character_dict.get("first_level")
        choice = input("Choose your 1st level spells:\n1) Animal Friendship\n2) Bane\n3) Charm Person\n4) Comprehend Languages\n5) Cure Wounds\n6) Detect Magic\n7) Disguise Self\n8) Dissonant Whispers\n9) Distort Value\n10) Earth Tremor\n11) Faerie Fire\n12) Feather Fall\n13) Healing Word\n14) Heroism\n15) Hideous Laughter\n16) Identify\n17) Illusory Script\n18) Longstrider\n19) Silent Image\n20) Sleep\n21) Speak with Animals\n22) Tasha's Hideous Laughter\n23) Thunderwave\n24) Unseen Servant\nEnter your selection: ")

        if choice =='1':
            spell_picked = 'Animal Friendship'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Bane'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Charm Person'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Comprehend Languages'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Cure Wounds'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Detect Magic'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Disguise Self'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Dissonant Whispers'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Distort Value'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Earth Tremor'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Faerie Fire'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Feather Fall'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Healing Word'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='14':
            spell_picked = 'Heroism'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='15':
            spell_picked = 'Hideous Laughter'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='16':
            spell_picked = 'Identify'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='17':
            spell_picked = 'Illusory Script'
            if spell_picked  in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='18':
            spell_picked = 'Longstrider'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='19':
            spell_picked = 'Silent Image'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='20':
            spell_picked = 'Sleep'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='21':
            spell_picked = 'Speak with Animals'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='22':
            spell_picked = 'Tasha\'s Hideous Laughter'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='23':
            spell_picked = 'Thunderwave'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='24':
            spell_picked = 'Unseen Servant'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        else:
            print("Invalid Input")
            continue

# Select two bard cantrips and get four 1st level spells
def bard_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            bard_cantrip()
            x+=1
        elif x == 3:
            while y < 6:
                if y < 5:
                    print(f'{y}/4')
                    bard_first()
                    y+=1
                elif y ==5:
                    y+=1
                    x+=1
                    break

# Cleric Cantrips
def cleric_cantrip():
    while True:
        check_spell = dnd_dict.character_dict.get("cantrip")
        choice = input("Choose your cantrips:\n1) Guidance\n2) Light\n3) Mending\n4) Resistance\n5) Sacred Flame\n6) Spare the Dying\n7) Thaumaturgy\n8) Toll the Dead\n9) Word of Radiance\nEnter your selection: ")
        if choice =='1':
            spell_picked = 'Guidance'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Light'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Mending'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Resistance'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Sacred Flame'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Spare the Dying'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Thaumaturgy'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Toll the Dead'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Word of Radiance'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        else:
            print("Invalid Input")
            continue


def cleric_first():
        cleric_spell = ['Bane', 'Bless', 'Ceremony', 'Command', 'Create or Destroy Water', 'Cure Wounds', 'Detect Evil and Good', 'Detect Poison and Disease', 'Guiding Bolt', 'Healing Word', 'Inflict Wounds', 'Protection from Evil and Good', 'Purify Food and Drink', 'Sanctuary', 'Shield of Faith']
        dnd_dict.character_dict.get("first_level").append(cleric_spell)

def cleric_magic():
    x=1
    while x < 5:
        if x<4:
            print(f'{x}/3')
            cleric_cantrip()
            x+=1
        elif x == 4:
            cleric_first()
            x+=1
            break

def druid_cantrip():
    while True:
        check_spell = dnd_dict.character_dict.get("cantrip")
        choice = input("Choose your cantrips:\n1) Control Flames\n2) Create Bonfire\n3) Druidcraft\n4) Frostbite\n5) Guidance\n6) Gust\n7) Infestation\n8) Magic Stone\n9) Mending\n10) Mold Earth\n11) Poison Spray\n12) Primal Savagery\n13) Produce Flame\n14) Resistance\n15) Shape Water\n16) Shillelagh\n17) Thornwhip\n18) Thunderclap\nEnter your selection: ")
        if choice =='1':
            spell_picked = 'Control Flames'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Create Bonfire'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Druidcraft'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Frostbite'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Guidance'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Gust'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Infestation'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Magic Stone'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Mending'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Mold Earth'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Poison Spray'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Primal Savagery'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Produce Flame'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='14':
            spell_picked = 'Resistance'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='15':
            spell_picked = 'Shape Water'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='16':
            spell_picked = 'Shillelagh'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='17':
            spell_picked = 'Thornwhip'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='18':
            spell_picked = 'Thunderclap'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        else:
            print("Invalid Input")
            continue

def druid_first():
        druid_spell = ['Absorb Elements', 'Animal Friendship', 'Beast Bond', 'Charm Person', 'Create or Destroy Water', 'Cure Wounds', 'Detect Magic', 'Detect Poison and Disease', 'Earth Tremor', 'Entangle', 'Faerie Fire', 'Fog Cloud', 'Goodberry', 'Healing Word', 'Ice Knife', 'Jump', 'Longstrider', 'Purify Food and Drink', 'Snare', 'Speak with Animals', 'Thunderwave']
        dnd_dict.character_dict.get("first_level").append(druid_spell)

def druid_magic():
    x=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            druid_cantrip()
            x+=1
        elif x == 3:
            druid_first()
            x+=1
            break

def sorcerer_cantrip():
    while True:
        check_spell = dnd_dict.character_dict.get("cantrip")
        choice = input("Choose your cantrips:\n1) Acid Splash\n2) Blade Ward\n3) Booming Blade\n4) Chill Touch\n5) Control Flames\n6) Create Bonfire\n7) Dancing Lights\n8) Fire Bolt\n9) Friends\n10) Frostbite\n11) Green-Flame Blade\n12) Gust\n13) Infestation\n14) Light\n15) Lightning Lure\n16) Mage Hand\n17) Mending\n18) Message\n19) Mind Sliver\n20) Minor Illusion\n21) Mold Earth\n22) Poison Spray\n23) Prestidigitation\n24) Ray of Frost\n25) Shape Water\n26) Shocking Grasp\n27) Sword Burst\n28) Thunderclap\n29) True Strike\nEnter your selection: ")
        if choice =='1':
            spell_picked = 'Acid Splash'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Blade Ward'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Booming Blade'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Chill Touch'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Control Flames'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Create Bonfire'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Dancing Lights'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Fire Bolt'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Friends'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Frostbite'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Green-Flame Blade'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Gust'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Infestation'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='14':
            spell_picked = 'Light'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='15':
            spell_picked = 'Lightning Lure'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='16':
            spell_picked = 'Mage Hand'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='17':
            spell_picked = 'Mending'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='18':
            spell_picked = 'Message'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='19':
            spell_picked = 'Mind Sliver'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='20':
            spell_picked = 'Minor Illusion'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='21':
            spell_picked = 'Mold Earth'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='22':
            spell_picked = 'Poison Spray'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='23':
            spell_picked = 'Prestidigitation'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='24':
            spell_picked = 'Ray of Frost'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='25':
            spell_picked = 'Shape Water'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='26':
            spell_picked = 'Shocking Grasp'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='27':
            spell_picked = 'Sword Burst'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='28':
            spell_picked = 'Thunderclap'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='29':
            spell_picked = 'True Strike'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        else:
            print("Invalid Input")
            continue

def sorcerer_first():
    while True:
        check_spell = dnd_dict.character_dict.get("first_level")
        choice = input("Choose your 1st level spells:\n1) Absorb Elements\n2) Burning Hands\n3) Catapult\n4) Chaos Bolt\n5) Charm Person\n6) Chromatic Orb\n7) Color Spray\n8) Comprehend Languages\n9) Detect Magic\n10) Disguise Self\n11) Distort Value\n12) Earth Tremor\n13) Expeditious Retreat\n14) False Life\n15) Feather Fall\n16) Fog Cloud\n17) Ice Knife\n18) Jump\n19) Mage Armor\n20) Magic Missile\n21) Ray of Sickness\n22) Shield\n23) Silent Image\n24) Sleep\n25) Tasha's Caustic Brew\n26) Thunderwave\n27) Witch Bolt\nEnter your selection: ")

        if choice =='1':
            spell_picked = 'Absorb Elements'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Burning Hands'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Catapult'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Chaos Bolt'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Charm Person'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Chromatic Orb'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Color Spray'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Comprehend Languages'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Detect Magic'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Disguise Self'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Distort Value'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Earth Tremor'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Expeditious Retreat'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='14':
            spell_picked = 'False Life'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='15':
            spell_picked = 'Feather Fall'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='16':
            spell_picked = 'Fog Cloud'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='17':
            spell_picked = 'Ice Knife'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='18':
            spell_picked = 'Jump'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='19':
            spell_picked = 'Mage Armor'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='20':
            spell_picked = 'Magic Missile'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='21':
            spell_picked = 'Ray of Sickness'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='22':
            spell_picked = 'Shield'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='23':
            spell_picked = 'Silent Image'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='24':
            spell_picked = 'Sleep'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='25':
            spell_picked = 'Tasha\'s Caustic Brew'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='26':
            spell_picked = 'Thunderwave'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='27':
            spell_picked = 'Witch Bolt'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        else:
            print("Invalid Input")
            continue


# Select four sorcerer cantrips and get two 1st level spells
def sorcerer_magic():
    x=1
    y=1
    while x < 6:
        if x<5:
            print(f'{x}/4')
            sorcerer_cantrip()
            x+=1
        elif x == 5:
            while y < 4:
                if y < 3:
                    print(f'{y}/2')
                    sorcerer_first()
                    y+=1
                elif y ==3:
                    y+=1
                    x+=1
                    break

def warlock_cantrip():
    while True:
        check_spell = dnd_dict.character_dict.get("cantrip")
        choice = input("Choose your cantrips:\n1) Blade Ward\n2) Booming Blade\n3) Chill Touch\n4) Create Bonfire\n5) Eldritch Blast\n6) Friends\n7) Frostbite\n8) Green-Flame Blade\n9) Infestation\n10) Lightning Lure\n11) Mage Hand\n12) Magic Stone\n13) Mind Sliver\n14) Minor Illusion\n15) Poison Spray\n16) Prestidigitation\n17) Sword Burst\n18) Thunderclap\n19) Toll the Dead\n20) True Strike\nEnter your selection: ")
        if choice =='1':
            spell_picked = 'Blade Ward'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Booming Blade'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Chill Touch'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Create Bonfire'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Eldritch Blast'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Friends'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Frostbite'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Green-Flame Blade'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Infestation'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Lightning Lure'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Mage Hand'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Magic Stone'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Mind Sliver'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='14':
            spell_picked = 'Minor Illusion'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='15':
            spell_picked = 'Poison Spray'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='16':
            spell_picked = 'Prestidigitation'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='17':
            spell_picked = 'Sword Burst'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='18':
            spell_picked = 'Thunderclap'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='19':
            spell_picked = 'Toll the Dead'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='20':
            spell_picked = 'True Strike'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        else:
            print("Invalid Input")
            continue

# Basic Warlock Spell list without a patron
def warlock_first():
    while True:
        check_spell = dnd_dict.character_dict.get("first_level")
        choice = input("Choose your 1st level spells:\n1) Armor of Agathys\n2) Arms of Hadar\n3) Cause Fear\n4) Charm Person\n5) Comprehend Languages\n6) Distort Value\n7) Expeditious Retreat\n8) Hellish Rebuke\n9) Hex\n10) Illusory Script\n11) Protection from Evil and Good\n12) Unseen Servant\n13) Witch Bolt\nEnter your selection: ")

        if choice =='1':
            spell_picked = 'Armor of Agathys'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Arms of Hadar'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Cause Fear'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Charm Person'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Comprehend Languages'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Distort Value'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Expeditious Retreat'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Hellish Rebuke'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Hex'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Illusory Script'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Protection from Evil and Good'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Unseen Servant'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Witch Bolt'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break
        else:
            print("Invalid Input")
            continue

# Expanded Spell List for Archfey Warlock. Faerie Fire and Sleep added
def archfey_warlock_first():
    while True:
        check_spell = dnd_dict.character_dict.get("first_level")
        choice = input("Choose your 1st level spells:\n1) Armor of Agathys\n2) Arms of Hadar\n3) Cause Fear\n4) Charm Person\n5) Comprehend Languages\n6) Distort Value\n7) Expeditious Retreat\n8) Hellish Rebuke\n9) Hex\n10) Illusory Script\n11) Protection from Evil and Good\n12) Unseen Servant\n13) Witch Bolt\n14) Faerie Fire\n15) Sleep\nEnter your selection: ")

        if choice =='1':
            spell_picked = 'Armor of Agathys'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Arms of Hadar'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Cause Fear'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Charm Person'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Comprehend Languages'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Distort Value'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Expeditious Retreat'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Hellish Rebuke'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Hex'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Illusory Script'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Protection from Evil and Good'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Unseen Servant'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Witch Bolt'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='14':
            spell_picked = 'Faerie Fire'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='15':
            spell_picked = 'Sleep'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break
        else:
            print("Invalid Input")
            continue


# Expanded Spell List for Fiend Warlock. Burning Hands and Command added
def fiend_warlock_first():
    while True:
        check_spell = dnd_dict.character_dict.get("first_level")
        choice = input("Choose your 1st level spells:\n1) Armor of Agathys\n2) Arms of Hadar\n3) Cause Fear\n4) Charm Person\n5) Comprehend Languages\n6) Distort Value\n7) Expeditious Retreat\n8) Hellish Rebuke\n9) Hex\n10) Illusory Script\n11) Protection from Evil and Good\n12) Unseen Servant\n13) Witch Bolt\n14) Burning Hands\n15) Command\nEnter your selection: ")

        if choice =='1':
            spell_picked = 'Armor of Agathys'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Arms of Hadar'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Cause Fear'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Charm Person'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Comprehend Languages'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Distort Value'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Expeditious Retreat'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Hellish Rebuke'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Hex'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Illusory Script'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Protection from Evil and Good'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Unseen Servant'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Witch Bolt'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='14':
            spell_picked = 'Burning Hands'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='15':
            spell_picked = 'Command'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break
        else:
            print("Invalid Input")
            continue


# Expanded Spell List for Great Old One Warlock. Dissonant Whispers and Tasha's Hideous Laughter added
def goo_warlock_first():
    while True:
        check_spell = dnd_dict.character_dict.get("first_level")
        choice = input("Choose your 1st level spells:\n1) Armor of Agathys\n2) Arms of Hadar\n3) Cause Fear\n4) Charm Person\n5) Comprehend Languages\n6) Distort Value\n7) Expeditious Retreat\n8) Hellish Rebuke\n9) Hex\n10) Illusory Script\n11) Protection from Evil and Good\n12) Unseen Servant\n13) Witch Bolt\n14) Dissonant Whispers\n15) Tasha's Hideous Laughter\nEnter your selection: ")

        if choice =='1':
            spell_picked = 'Armor of Agathys'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Arms of Hadar'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Cause Fear'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Charm Person'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Comprehend Languages'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Distort Value'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Expeditious Retreat'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Hellish Rebuke'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Hex'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Illusory Script'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Protection from Evil and Good'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Unseen Servant'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Witch Bolt'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='14':
            spell_picked = 'Dissonant Whispers'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='15':
            spell_picked = 'Tasha\'s Hideous Laughter'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break
        else:
            print("Invalid Input")
            continue

# Select two warlock cantrips and get two 1st level spells
def archfey_warlock_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            warlock_cantrip()
            x+=1
        elif x == 3:
            while y < 4:
                if y < 3:
                    print(f'{y}/2')
                    archfey_warlock_first()
                    y+=1
                elif y ==3:
                    y+=1
                    x+=1
                    break

# Select two warlock cantrips and get two 1st level spells
def fiend_warlock_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            warlock_cantrip()
            x+=1
        elif x == 3:
            while y < 4:
                if y < 3:
                    print(f'{y}/2')
                    fiend_warlock_first()
                    y+=1
                elif y ==3:
                    y+=1
                    x+=1
                    break

# Select two warlock cantrips and get two 1st level spells
def goo_warlock_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            warlock_cantrip()
            x+=1
        elif x == 3:
            while y < 4:
                if y < 3:
                    print(f'{y}/2')
                    goo_warlock_first()
                    y+=1
                elif y ==3:
                    y+=1
                    x+=1
                    break
# Basic Warlock spell selection without patrons
def warlock_magic():
    x=1
    y=1
    while x < 4:
        if x<3:
            print(f'{x}/2')
            warlock_cantrip()
            x+=1
        elif x == 3:
            while y < 4:
                if y < 3:
                    print(f'{y}/2')
                    warlock_first()
                    y+=1
                elif y ==3:
                    y+=1
                    x+=1
                    break


def wizard_cantrip():
    while True:
        check_spell = dnd_dict.character_dict.get("cantrip")
        choice = input("Choose your cantrips:\n1) Acid Splash\n2) Blade Ward\n3) Booming Blade\n4) Chill Touch\n5) Control Flames\n6) Create Bonfire\n7) Dancing Lights\n8) Encode Thoughts\n9) Fire Bolt\n10) Friends\n11) Frostbite\n12) Green-Flame Blade\n13) Gust\n14) Infestation\n15) Light\n16) Lightning Lure\n17) Mage Hand\n18) Mending\n19) Message\n20) Mind Sliver\n21) Minor Illusion\n22) Mold Earth\n23) Poison Spray\n24) Prestidigitation\n25) Ray of Frost\n26) Shape Water\n27) Shocking Grasp\n28) Sword Burst\n29) Thunderclap\n30) Toll the Dead\n31) True Strike\nEnter your selection: ")
        if choice =='1':
            spell_picked = 'Acid Splash'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Blade Ward'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Booming Blade'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Chill Touch'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Control Flames'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Create Bonfire'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Dancing Lights'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Encode Thoughts'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Fire Bolt'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Friends'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Frostbite'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Green-Flame Blade'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Gust'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='14':
            spell_picked = 'Infestation'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='15':
            spell_picked = 'Light'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='16':
            spell_picked = 'Lightning Lure'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='17':
            spell_picked = 'Mage Hand'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='18':
            spell_picked = 'Mending'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='19':
            spell_picked = 'Message'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='20':
            spell_picked = 'Mind Sliver'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='21':
            spell_picked = 'Minor Illusion'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='22':
            spell_picked = 'Mold Earth'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='23':
            spell_picked = 'Poison Spray'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='24':
            spell_picked = 'Prestidigitation'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='25':
            spell_picked = 'Ray of Frost'
            if spell_picked not in check_spell:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break
            else:
                print(f'{spell_picked} already selected, please pick again')
                continue

        elif choice =='26':
            spell_picked = 'Shape Water'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='27':
            spell_picked = 'Shocking Grasp'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='28':
            spell_picked = 'Sword Burst'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='29':
            spell_picked = 'Thunderclap'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='30':
            spell_picked = 'Toll the Dead'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        elif choice =='31':
            spell_picked = 'True Strike'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("cantrip").append(spell_picked)
                break

        else:
            print("Invalid Input")
            continue


def wizard_first():
    while True:
        check_spell = dnd_dict.character_dict.get("first_level")
        choice = input("Choose your 1st level spells:\n1) Absorb Elements\n2) Alarm\n3) Burning Hands\n4) Catapult\n5) Cause Fear\n6) Charm Person\n7) Chromatic Orb\n8) Color Spray\n9) Comprehend Languages\n10) Detect Magic\n11) Disguise Self\n12) Distort Value\n13) Earth Tremor\n14) Expeditious Retreat\n15) False Life\n16) Feather Fall\n17) Find Familiar\n18) Floating Disk\n19) Fog Cloud\n20) Frost Fingers\n21) Grease\n22) Hideous Laughter\n23) Ice Knife\n24) Identify\n25) Illusory Script\n26) Jim's Magic Missile\n27) Jump\n28) Longstrider\n29) Mage Armor\n30) Magic Missile\n31) Protection from Evil and Good\n32) Ray of Sickness\n33) Shield\n34) Silent Image\n35) Sleep\n36) Snare\n37) Tasha's Hideous Laughter\n38) Tasha's Caustic Brew\n39) Tenser's Floating Disk\n40) Thunderwave\n41) Unseen Servant\n42) Witch Bolt\nEnter your selection: ")

        if choice =='1':
            spell_picked = 'Absorb Elements'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='2':
            spell_picked = 'Alarm'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='3':
            spell_picked = 'Burning Hands'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='4':
            spell_picked = 'Catapult'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='5':
            spell_picked = 'Cause Fear'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='6':
            spell_picked = 'Charm Person'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='7':
            spell_picked = 'Chromatic Orb'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='8':
            spell_picked = 'Color Spray'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='9':
            spell_picked = 'Comprehend Languages'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='10':
            spell_picked = 'Detect Magic'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='11':
            spell_picked = 'Disguise Self'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='12':
            spell_picked = 'Distort Value'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='13':
            spell_picked = 'Earth Tremor'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='14':
            spell_picked = 'Expeditious Retreat'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='15':
            spell_picked = 'False Life'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='16':
            spell_picked = 'Feather Fall'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='17':
            spell_picked = 'Find Familiar'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='18':
            spell_picked = 'Floating Disk'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='19':
            spell_picked = 'Fog Cloud'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='20':
            spell_picked = 'Frost Fingers'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='21':
            spell_picked = 'Grease'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='22':
            spell_picked = 'Hideous Laughter'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='23':
            spell_picked = 'Ice Knife'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='24':
            spell_picked = 'Identify'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='25':
            spell_picked = 'Illusory Script'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='26':
            spell_picked = 'Jim\'s Magic Missile'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='27':
            spell_picked = 'Jump'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='28':
            spell_picked = 'Longstrider'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='29':
            spell_picked = 'Mage Armor'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='30':
            spell_picked = 'Magic Missile'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='31':
            spell_picked = 'Protection from Evil and Good'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='32':
            spell_picked = 'Ray of Sickness'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='33':
            spell_picked = 'Shield'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='34':
            spell_picked = 'Silent Image'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='35':
            spell_picked = 'Sleep'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='36':
            spell_picked = 'Snare'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='37':
            spell_picked = 'Tasha\'s Hideous Laughter'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='38':
            spell_picked = 'Tasha\'s Caustic Brew'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='39':
            spell_picked = 'Tenser\'s Floating Disk'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='40':
            spell_picked = 'Thunderwave'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='41':
            spell_picked = 'Unseen Servant'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        elif choice =='42':
            spell_picked = 'Witch Bolt'
            if spell_picked in check_spell:
                print(f'{spell_picked} already selected, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("first_level").append(spell_picked)
                break

        else:
            print("Invalid Input")
            continue



# Select three wizard cantrips and get six 1st level spells
def wizard_magic():
    x=1
    y=1
    while x < 5:
        if x<4:
            print(f'{x}/3')
            wizard_cantrip()
            x+=1
        elif x == 4:
            while y < 8:
                if y < 5:
                    print('{y}/6')
                    wizard_first()
                    y+=1
                elif y ==5:
                    y+=1
                    x+=1
                    break
