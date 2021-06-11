#!/usr/bin/python3
import dnd_dict

# Checks if the language is selected. If it is, redo the choice
def lang_check(u_lang,lang_list):
    if any(u_lang in lang for lang in lang_list):
        return True

def elf_lang():
# If the config has already been set, don't bother picking a language
    while True:
        check_lang = dnd_dict.character_dict.get("Languages")
        choice = input("Choose an additional language you want to include:\n1) Abyssal\n2) Celestial\n3) Deep Speech\n4) Draconic\n5) Dwarvish\n6) Giant\n7) Gnomish\n8) Goblin\n9) Infernal\n10) Halfling\n11) Orc\n12) Primordial\n13) Sylvan\n14) Undercommon\nEnter your selection: ")

        if choice =='1':
            language_picked='Abyssal'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='2':
            language_picked='Celestial'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='3':
            language_picked='Deep Speech'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='4':
            language_picked='Draconic'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='5':
            language_picked='Dwarven'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='6':
            language_picked='Giant'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='7':
            language_picked='Gnomish'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='8':
            language_picked='Goblin'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='9':
            language_picked='Infernal'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='10':
            language_picked='Halfling'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='11':
            language_picked='Orc'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='12':
            language_picked='Primordial'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='13':
            language_picked='Sylvan'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='14':
            language_picked='Undercommon'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        else:
            print("Invalid input.\n")
            continue

def language():
    while True:
        check_lang = dnd_dict.character_dict.get("Languages")
        choice = input("Choose a language you want to include:\n1) Abyssal\n2) Celestial\n3) Deep Speech\n4) Draconic\n5) Dwarvish\n6) Elven\n7) Giant\n8) Gnomish\n9) Goblin\n10) Infernal\n11) Halfling\n12) Orc\n13) Primordial\n14) Sylvan\n15) Undercommon\nEnter your selection: ")

        if choice =='1':
            language_picked='Abyssal'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='2':
            language_picked='Celestial'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='3':
            language_picked='Deep Speech'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='4':
            language_picked='Draconic'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='5':
            language_picked='Dwarven'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='6':
            language_picked='Elven'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='7':
            language_picked='Giant'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='8':
            language_picked='Gnomish'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='9':
            language_picked='Goblin'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='10':
            language_picked='Infernal'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='11':
            language_picked='Halfling'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='12':
            language_picked='Orc'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='13':
            language_picked='Primordial'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='14':
            language_picked='Sylvan'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice =='15':
            language_picked='Undercommon'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        else:
            print("Invalid input.\n")
            continue


#Used for backgrounds that give two new languages.
def double_language():
    y = 1
    while y < 3:
        print(f'{y}/2')
        if y < 3:
            language()
            y+=1
        elif y == 0:
            break

#Used for Haunted One background
def exotic_language():
    while True:
        check_lang = dnd_dict.character_dict.get("Languages")
        choice = input("Choose a language you want to learn:\n1) Abyssal\n2) Celestial\n3) Deep Speech\n4) Draconic\n5) Infernal\n6) Primordial\n7) Sylvan\n8) Undercommon\nEnter your selection: ")
        if choice=='1':
            language_picked='Abyssal'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice=='2':
            language_picked='Celestial'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice=='3':
            language_picked='Deep Speech'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice=='4':
            language_picked='Draconic'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice=='5':
            language_picked='Infernal'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice=='6':
            language_picked='Primordial'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice=='7':
            language_picked='Sylvan'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        elif choice=='8':
            language_picked='Undercommon'
            if language_picked in check_lang:
                print(f'{language_picked} already selected, please pick again: ')
                continue
            else:
                dnd_dict.character_dict.get("Languages").append(language_picked)
                break

        else:
            print("Invalid Selection")
            continue

