import dnd_dict,dnd_class

def simple_weapon():
    while True:
        choice = input("Choose your simple weapon:\n1) Club\n2) Dagger\n3) Great-Club\n4) Hand-Axe\n5) Javelin\n6) Light Hammer\n7) Mace\n8) Quarterstaff\n9) Sickle\n10) Spear\n11) Light Crossbow\n12) Dart\n13) Shortbow\n14) Sling\nEnter your Selection: ")
        if choice=='1':
            dnd_dict.character_dict.get("Equipment").append('Club')
            break
 
        elif choice=='2':
            dnd_dict.character_dict.get("Equipment").append('Dagger')
            break

        elif choice=='3':
            dnd_dict.character_dict.get("Equipment").append('Great-Club')
            break

        elif choice=='4':
            dnd_dict.character_dict.get("Equipment").append('Hand-Axe')
            break

        elif choice=='5':
            dnd_dict.character_dict.get("Equipment").append('Javelin')
            break

        elif choice=='6':
            dnd_dict.character_dict.get("Equipment").append('Light Hammer')
            break

        elif choice=='7':
            dnd_dict.character_dict.get("Equipment").append('Mace')
            break

        elif choice=='8':
            dnd_dict.character_dict.get("Equipment").append('Quarterstaff')
            break

        elif choice=='9':
            dnd_dict.character_dict.get("Equipment").append('Sickle')
            break

        elif choice=='10':
            dnd_dict.character_dict.get("Equipment").append('Spear')
            break

        elif choice=='11':
            dnd_dict.character_dict.get("Equipment").append('Light Crossbow')
            break

        elif choice=='12':
            dnd_dict.character_dict.get("Equipment").append('Dart')
            break

        elif choice=='13':
            dnd_dict.character_dict.get("Equipment").append('Shortbow')
            break

        elif choice=='14':
            dnd_dict.character_dict.get("Equipment").append('Sling')
            break

        else:
            print("Invalid Selection")
            continue


def simple_melee():
    while True:
        choice = input("Choose your simple melee weapon:\n1) Club\n2) Dagger\n3) Great-Club\n4) Hand-Axe\n5) Javelin\n6) Light Hammer\n7) Mace\n8) Quarterstaff\n9) Sickle\n10) Spear\nEnter your Selection: ")
        if choice=='1':
            dnd_dict.character_dict.get("Equipment").append('Club')
            break
 
        elif choice=='2':
            dnd_dict.character_dict.get("Equipment").append('Dagger')
            break

        elif choice=='3':
            dnd_dict.character_dict.get("Equipment").append('Great-Club')
            break

        elif choice=='4':
            dnd_dict.character_dict.get("Equipment").append('Hand-Axe')
            break

        elif choice=='5':
            dnd_dict.character_dict.get("Equipment").append('Javelin')
            break

        elif choice=='6':
            dnd_dict.character_dict.get("Equipment").append('Light Hammer')
            break

        elif choice=='7':
            dnd_dict.character_dict.get("Equipment").append('Mace')
            break

        elif choice=='8':
            dnd_dict.character_dict.get("Equipment").append('Quarterstaff')
            break

        elif choice=='9':
            dnd_dict.character_dict.get("Equipment").append('Sickle')
            break

        elif choice=='10':
            dnd_dict.character_dict.get("Equipment").append('Spear')
            break

        else:
            print("Invalid Selection")
            continue


def double_simple():
    x = 1
    while x < 3:
        if x < 3:
            print(f'{x}/2')
            simple_weapon()
            x+=1
        elif x == 3:
            break

def double_simple_melee():
    x = 1
    while x < 3:
        if x < 3:
            print(f'{x}/2')
            simple_melee()
            x+=1
        elif x == 3:
            break

def martial_weapon():
    while True:
        choice = input("Enter your martial weapon:\n1) Battleaxe\n2) Flail\n3) Glaive\n4) Greataxe\n5) Greatsword\n6) Halberd\n7) Lance\n8) Longsword\n9) Maul\n10) Morningstar\n11) Pike\n12) Rapier\n13) Scimitar\n14) Shortsword\n15) Trident\n16) War Pick\n17) Warhammer\n18) Whip\n19) Blowgun\n20) Hand Crossbow\n21) Heavy Crossbow\n22) Longbow\n23) Net\nEnter your selection: ")
    
        if choice=='1':
            dnd_dict.character_dict.get("Equipment").append('Battleaxe')
            break

        elif choice=='2':
            dnd_dict.character_dict.get("Equipment").append('Flail')
            break

        elif choice=='3':
            dnd_dict.character_dict.get("Equipment").append('Glaive')
            break

        elif choice=='4':
            dnd_dict.character_dict.get("Equipment").append('Greataxe')
            break

        elif choice=='5':
            dnd_dict.character_dict.get("Equipment").append('Greatsword')
            break

        elif choice=='6':
            dnd_dict.character_dict.get("Equipment").append('Halberd')
            break

        elif choice=='7':
            dnd_dict.character_dict.get("Equipment").append('Lance')
            break

        elif choice=='8':
            dnd_dict.character_dict.get("Equipment").append('Longsword')
            break

        elif choice=='9':
            dnd_dict.character_dict.get("Equipment").append('Maul')
            break

        elif choice=='10':
            dnd_dict.character_dict.get("Equipment").append('Morningstar')
    
        elif choice=='11':
            dnd_dict.character_dict.get("Equipment").append('Pike')
            break

        elif choice=='12':
            dnd_dict.character_dict.get("Equipment").append('Rapier')
            break

        elif choice=='13':
            dnd_dict.character_dict.get("Equipment").append('Scimitar')
            break

        elif choice=='14':
            dnd_dict.character_dict.get("Equipment").append('Shortsword')
            break

        elif choice=='15':
            dnd_dict.character_dict.get("Equipment").append('Trident')
            break

        elif choice=='16':
            dnd_dict.character_dict.get("Equipment").append('War Pick')
            break

        elif choice=='17':
            dnd_dict.character_dict.get("Equipment").append('Warhammer')
            break

        elif choice=='18':
            dnd_dict.character_dict.get("Equipment").append('Whip')
            break

        elif choice=='19':
            dnd_dict.character_dict.get("Equipment").append('Blowgun')
            break

        elif choice=='20':
            dnd_dict.character_dict.get("Equipment").append('Hand Crossbow')
            break

        elif choice=='21':
            dnd_dict.character_dict.get("Equipment").append('Heavy Crossbow')
            break

        elif choice=='22':
            dnd_dict.character_dict.get("Equipment").append('Longbow')
            break

        elif choice=='23':
            dnd_dict.character_dict.get("Equipment").append('Net')
            break

        else:
            print("Invalid Selection")
            continue

def double_martial():
    x = 1
    while x < 3:
        if x < 3:
            print(f'{x}/2')
            martial_weapon()
            x+=1
        elif x == 3:
            break

def martial_melee():
    while True:
        choice = input("Enter your martial weapon:\n1) Battleaxe\n2) Flail\n3) Glaive\n4) Greataxe\n5) Greatsword\n6) Halberd\n7) Lance\n8) Longsword\n9) Maul\n10) Morningstar\n11) Pike\n12) Rapier\n13) Scimitar\n14) Shortsword\n15) Trident\n16) War Pick\n17) Warhammer\n18) Whip\nEnter your selection: ")
    
        if choice=='1':
            dnd_dict.character_dict.get("Equipment").append('Battleaxe')
            break
 
        elif choice=='2':
            dnd_dict.character_dict.get("Equipment").append('Flail')
            break

        elif choice=='3':
            dnd_dict.character_dict.get("Equipment").append('Glaive')
            break

        elif choice=='4':
            dnd_dict.character_dict.get("Equipment").append('Greataxe')
            break

        elif choice=='5':
            dnd_dict.character_dict.get("Equipment").append('Greatsword')
            break

        elif choice=='6':
            dnd_dict.character_dict.get("Equipment").append('Halberd')
            break

        elif choice=='7':
            dnd_dict.character_dict.get("Equipment").append('Lance')
            break

        elif choice=='8':
            dnd_dict.character_dict.get("Equipment").append('Longsword')
            break

        elif choice=='9':
            dnd_dict.character_dict.get("Equipment").append('Maul')
            break

        elif choice=='10':
            dnd_dict.character_dict.get("Equipment").append('Morningstar')
            break

        elif choice=='11':
            dnd_dict.character_dict.get("Equipment").append('Pike')
            break

        elif choice=='12':
            dnd_dict.character_dict.get("Equipment").append('Rapier')
            break

        elif choice=='13':
            dnd_dict.character_dict.get("Equipment").append('Scimitar')
            break

        elif choice=='14':
            dnd_dict.character_dict.get("Equipment").append('Shortsword')
            break

        elif choice=='15':
            dnd_dict.character_dict.get("Equipment").append('Trident')
            break

        elif choice=='16':
            dnd_dict.character_dict.get("Equipment").append('War Pick')
            break

        elif choice=='17':
            dnd_dict.character_dict.get("Equipment").append('Warhammer')
            break

        elif choice=='18':
            dnd_dict.character_dict.get("Equipment").append('Whip')
            break

        else:
            print("Invalid Selection")
            continue

#Leather Armor
def leather_armor():
    leather = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")),11)
    return leather

#Studded Leather Armor
def studded_leather_armor():
    studded_leather = dnd_class.RaceStats.stat_bonus((dnd_dict.character_dict.get("Stats").get("dexterity").get("mod")),12)
    return studded_leather

