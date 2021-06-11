#!/usr/bin/python3
import dnd_dict
from dnd_dict import character_dict as character_dict

# Determine the type of artisan tools the player wants proficiency in
def artisan_tools():
    while True:
        check_tool = dnd_dict.character_dict.get("Tools")
        choice = input("Choose the Artisan Tools you want proficiency in:\n1) Alchemist's Supplies\n2) Tinker's Tools\n3) Glassblower's Tools\n4) Jewler's Tools\n5) Brewer's Supplies\n6) Smith's Tools\n7) Cartographer's Tools\n8) Mason's Tools\n9) Calligrapher's Supplies\n10) Painter's Tools\n11) Carpenter's Tools\n12) Cobbler's Tools\n13) Leatherworker's Tools\n14) Cook's Utensils\n15) Weaver's Tools\n16) Woodcarver's Tools\nEnter your selection: ")

        if choice=='1':
            tool_picked = 'Alchemist\'s Supplies'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break

        elif choice=='2':
            tool_picked = 'Tinker\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='3':
            tool_picked = 'Glassblower\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='4':
            tool_picked = 'Jewler\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='5':
            tool_picked = 'Brewer\'s Supplies'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='6':
            tool_picked = 'Smith\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='7':
            tool_picked = 'Cartographer\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='8':
            tool_picked = 'Mason\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='9':
            tool_picked = 'Calligrapher\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='10':
            tool_picked = 'Painter\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='11':
            tool_picked = 'Carpenter\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='12':
            tool_picked = 'Cobbler\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='13':
            tool_picked = 'Leatherworker\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
 
        elif choice=='14':
            tool_picked = 'Cook\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
         
        elif choice=='15':
            tool_picked = 'Weaver\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break
        
 
        elif choice=='16':
            tool_picked = 'Woodcarver\'s Tools'
            if tool_picked in check_tool:
                print(f'You are already proficient with {tool_picked}, please pick again')
                continue
            else:
                dnd_dict.character_dict.get("Tools").append(tool_picked)
                break


        else:
            print("Invalid input.")
            continue

#Used for Guild Artisan to give a set of artisan's tools

def artisan_tools_equip():
    while True:
        choice = input("Choose the Artisan Tools you want to have:\n1) Alchemist's Supplies\n2) Tinker's Tools\n3) Glassblower's Tools\n4) Jewler's Tools\n5) Brewer's Supplies\n6) Smith's Tools\n7) Cartographer's Tools\n8) Mason's Tools\n9) Calligrapher's Supplies\n10) Painter's Tools\n11) Carpenter's Tools\n12) Cobbler's Tools\n13) Leatherworker's Tools\n14) Cook's Utensils\n15) Weaver's Tools\n16) Woodcarver's Tools\nEnter your selection: ")

        if choice=='1':
            dnd_dict.character_dict.get("Equipment").append("Alchemist's Supplies")
            break
 
        elif choice=='2':
            dnd_dict.character_dict.get("Equipment").append("Tinker's Tools")
            break
 
 
        elif choice=='3':
            dnd_dict.character_dict.get("Equipment").append("Glassblower's Tools")
            break
 
        elif choice=='4':
            dnd_dict.character_dict.get("Equipment").append("Jewler's Tools")
            break
 
        elif choice=='5':
            dnd_dict.character_dict.get("Equipment").append("Brewer's Supplies")
            break
 
        elif choice=='6':
            dnd_dict.character_dict.get("Equipment").append("Smith's Tools")
            break
 
        elif choice=='7':
            dnd_dict.character_dict.get("Equipment").append("Cartographer's's Tools")
            break
 
        elif choice=='8':
            dnd_dict.character_dict.get("Equipment").append("Mason's Tools")
            break
 
        elif choice=='9':
            dnd_dict.character_dict.get("Equipment").append("Calligrapher's Tools")
            break
 
        elif choice=='10':
            dnd_dict.character_dict.get("Equipment").append("Painter's Tools")
            break
 
        elif choice=='11':
            dnd_dict.character_dict.get("Equipment").append("Carpenter's Tools")
            break
 
        elif choice=='12':
            dnd_dict.character_dict.get("Equipment").append("Cobbler's Tools")
            break
 
        elif choice=='13':
            dnd_dict.character_dict.get("Equipment").append("Leatherworker's Tools")
            break
 
        elif choice=='14':
            dnd_dict.character_dict.get("Equipment").append("Cook's Tools")
            break
         
        elif choice=='15':
            dnd_dict.character_dict.get("Equipment").append("Weaver's Tools")
            break
        
 
        elif choice=='16':
            dnd_dict.character_dict.get("Equipment").append("Woodcarver's Tools")
            break

        else:
            print("Invalid input.")
            continue


def gaming_set():
    while True:
        choice=input("Choose gaming set are you proficient with:\n1) Dice\n2) Cards\nEnter your selection: ")
        if choice =='1':
            print("Dice Chosen")
            dnd_dict.character_dict.get("Gaming_Set").append('Dice')
            break
 
        elif choice =='2':
            print("Cards Chosen")
            dnd_dict.character_dict.get("Gaming_Set").append('Cards')
            break

        else:
            print("Invalid Selection")
            continue

def musical_instrument():
    musical_choice = input("What instrument are your proficient with? ")
    dnd_dict.character_dict.get("Instruments").append(musical_choice)
