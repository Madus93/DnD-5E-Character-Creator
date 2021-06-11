#!/usr/bin/python3
import random, dnd_dict, dnd_class


# If the sum of the rolls is less than 72, reroll. Otherwise, print the results as normal. Retry if there are 5 failed attempts


def check_roll(num):
    counter = 1
    while True:
        if num>72:
            break
        else:
            if counter < 5:
                init_stats()
                counter += 1
            elif counter == 5:
                print("Error: Too Many Failed Attempts. Please Try Again.")
                exit()

def initial_stats():
    dnd_dict.character_dict['Stats']['strength']['base'] = dnd_class.Character.initial_stat("Strength")
    dnd_dict.character_dict['Stats']['dexterity']['base'] = dnd_class.Character.initial_stat("Dexterity")
    dnd_dict.character_dict['Stats']['constitution']['base'] = dnd_class.Character.initial_stat("Constitution")
    dnd_dict.character_dict['Stats']['intelligence']['base'] =  dnd_class.Character.initial_stat("Intelligence")
    dnd_dict.character_dict['Stats']['wisdom']['base'] = dnd_class.Character.initial_stat("Wisdom")
    dnd_dict.character_dict['Stats']['charisma']['base'] = dnd_class.Character.initial_stat("Charisma")

def init_stats():
    t_stat = 0
    for stat in range(0, 6):
        results = [random.randint(1,6) for results in range (4)]
        lowest = min(results)
        results.remove(lowest)
        t_stat+=sum(results)
        print(sum(results))
    print("\n")
    return t_stat

#Roll 4 d6, drop the lowest die
def stat_roll():
    init_count = 1
    print("Put these rolls in any stat:")
    t_stat = init_stats()
    while True:
        if t_stat > 72:
            break
        else:
            if init_count < 5:
                t_stat =init_stats()
                init_count+=1
            elif init_count == 5:
                print("Too Many Attempts")
                exit()


    initial_stats()


# Standard point array, have the player choose the stats they want to be 15, 14, 13, 12, 10, and 8. Submit an error if they select a stat that has already been chosen
def point_array():
    i = 1
    while i < 7:
        if i == 1:
            while True:
                choice1 = input("What stat would you like to be 15?\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\n6) Charisma\nEnter your selection: ")
                if choice1 == '1':
                    dnd_dict.character_dict['Stats']['strength']['base'] = 15
                    i +=1
                    break
                elif choice1 == '2':
                    dnd_dict.character_dict['Stats']['dexterity']['base'] = 15
                    i +=1
                    break

                elif choice1 == '3':
                    dnd_dict.character_dict['Stats']['constitution']['base'] = 15
                    i +=1
                    break

                elif choice1 == '4':
                    dnd_dict.character_dict['Stats']['intelligence']['base'] = 15
                    i +=1
                    break

                elif choice1 == '5':
                    dnd_dict.character_dict['Stats']['wisdom']['base'] = 15
                    i +=1
                    break

                elif choice1 == '6':
                    dnd_dict.character_dict['Stats']['charisma']['base'] = 15
                    i +=1
                    break
 
                else:
                    print("Invalid Selection")
                    continue
 
        elif i == 2:
            while True:
                choice2 = input("What stat would you like to be 14?\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\n6) Charisma\nEnter your selection: ")
                if choice2 == '1':
                    if dnd_dict.character_dict['Stats']['strength']['base'] ==0:
                        dnd_dict.character_dict['Stats']['strength']['base'] = 14
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice2 == '2':
                    if dnd_dict.character_dict['Stats']['dexterity']['base'] ==0:
                        dnd_dict.character_dict['Stats']['dexterity']['base'] = 14
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice2 == '3':
                    if dnd_dict.character_dict['Stats']['constitution']['base'] ==0:
                        dnd_dict.character_dict['Stats']['constitution']['base'] = 14
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice2 == '4':
                    if dnd_dict.character_dict['Stats']['intelligence']['base'] ==0:
                        dnd_dict.character_dict['Stats']['intelligence']['base'] = 14
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice2 == '5':
                    if dnd_dict.character_dict['Stats']['wisdom']['base'] ==0:
                        dnd_dict.character_dict['Stats']['wisdom']['base'] = 14
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice2 == '6':
                    if dnd_dict.character_dict['Stats']['charisma']['base'] ==0:
                        dnd_dict.character_dict['Stats']['charisma']['base'] = 14
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue
 
                else:
                    print("Invalid Selection")
                    continue

        elif i == 3:
            while True:
                choice3 = input("What stat would you like to be 13?\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\n6) Charisma\nEnter your selection: ")
                if choice3 == '1':
                    if dnd_dict.character_dict['Stats']['strength']['base'] ==0:
                        dnd_dict.character_dict['Stats']['strength']['base'] = 13
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice3 == '2':
                    if dnd_dict.character_dict['Stats']['dexterity']['base'] ==0:
                        dnd_dict.character_dict['Stats']['dexterity']['base'] = 13
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue
 
                elif choice3 == '3':
                    if dnd_dict.character_dict['Stats']['constitution']['base'] ==0:
                        dnd_dict.character_dict['Stats']['constitution']['base'] = 13
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice3 == '4':
                    if dnd_dict.character_dict['Stats']['intelligence']['base'] ==0:
                        dnd_dict.character_dict['Stats']['intelligence']['base'] = 13
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice3 == '5':
                    if dnd_dict.character_dict['Stats']['wisdom']['base'] ==0:
                        dnd_dict.character_dict['Stats']['wisdom']['base'] = 13
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice3 == '6':
                    if dnd_dict.character_dict['Stats']['charisma']['base'] ==0:
                        dnd_dict.character_dict['Stats']['charisma']['base'] = 13
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                else:
                    print("Invalid Selection")
                    continue

        elif i == 4:
            while True:
                choice4 = input("What stat would you like to be 12?\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\n6) Charisma\nEnter your selection: ")
                if choice4 == '1':
                    if dnd_dict.character_dict['Stats']['strength']['base'] ==0:
                        dnd_dict.character_dict['Stats']['strength']['base'] = 12
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice4 == '2':
                    if dnd_dict.character_dict['Stats']['dexterity']['base'] ==0:
                        dnd_dict.character_dict['Stats']['dexterity']['base'] = 12
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice4 == '3':
                    if dnd_dict.character_dict['Stats']['constitution']['base'] ==0:
                        dnd_dict.character_dict['Stats']['constitution']['base'] = 12
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice4 == '4':
                    if dnd_dict.character_dict['Stats']['intelligence']['base'] ==0:
                        dnd_dict.character_dict['Stats']['intelligence']['base'] = 12
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice4 == '5':
                    if dnd_dict.character_dict['Stats']['wisdom']['base'] ==0:
                        dnd_dict.character_dict['Stats']['wisdom']['base'] = 12
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice4 == '6':
                    if dnd_dict.character_dict['Stats']['charisma']['base'] ==0:
                        dnd_dict.character_dict['Stats']['charisma']['base'] = 12
                        i +=1
                        break

                    else:
                        print("This stat is already taken")
                        continue

                else:
                    print("Invalid Selection")
                    continue
        
        elif i == 5:
            while True:
                choice5 = input("What stat would you like to be 10?\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\n6) Charisma\nEnter your selection: ")
                if choice5 == '1':
                    if dnd_dict.character_dict['Stats']['strength']['base'] ==0:
                        dnd_dict.character_dict['Stats']['strength']['base'] = 10
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice5 == '2':
                    if dnd_dict.character_dict['Stats']['dexterity']['base'] ==0:
                        dnd_dict.character_dict['Stats']['dexterity']['base'] = 10
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice5 == '3':
                    if dnd_dict.character_dict['Stats']['constitution']['base'] ==0:
                        dnd_dict.character_dict['Stats']['constitution']['base'] = 10
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice5 == '4':
                    if dnd_dict.character_dict['Stats']['intelligence']['base'] ==0:
                        dnd_dict.character_dict['Stats']['intelligence']['base'] = 10
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice5 == '5':
                    if dnd_dict.character_dict['Stats']['wisdom']['base'] ==0:
                        dnd_dict.character_dict['Stats']['wisdom']['base'] = 10
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice5 == '6':
                    if dnd_dict.character_dict['Stats']['charisma']['base'] ==0:
                        dnd_dict.character_dict['Stats']['charisma']['base'] = 10
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue
 
                else:
                    print("Invalid Selection")
                    continue
 
        elif i == 6:
            while True:
                choice6 = input("What stat would you like to be 8?\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\n6) Charisma\nEnter your selection: ")
                if choice6 == '1':
                    if dnd_dict.character_dict['Stats']['strength']['base'] ==0:
                        dnd_dict.character_dict['Stats']['strength']['base'] = 8
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice6 == '2':
                    if dnd_dict.character_dict['Stats']['dexterity']['base'] ==0:
                        dnd_dict.character_dict['Stats']['dexterity']['base'] = 8
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice6 == '3':
                    if dnd_dict.character_dict['Stats']['constitution']['base'] ==0:
                        dnd_dict.character_dict['Stats']['constitution']['base'] = 8
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice6 == '4':
                    if dnd_dict.character_dict['Stats']['intelligence']['base'] ==0:
                        dnd_dict.character_dict['Stats']['intelligence']['base'] = 8
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice6 == '5':
                    if dnd_dict.character_dict['Stats']['wisdom']['base'] ==0:
                        dnd_dict.character_dict['Stats']['wisdom']['base'] = 8
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue

                elif choice6 == '6':
                    if dnd_dict.character_dict['Stats']['charisma']['base'] ==0:
                        dnd_dict.character_dict['Stats']['charisma']['base'] = 8
                        i +=1
                        break
                    else:
                        print("This stat is already taken")
                        continue
 
                else:
                    print("Invalid Selection")
                    continue
        elif i == 7:
            break
  
# Point Buy stat selection, where you have 27 points to distribute between the stats, which can be from 8-15 for all of them. The stat and cost are: 8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:7, 15:9.
# Input the stats, and then put them into the dictionary at the end if they are not already in the config file

def point_buy():
    x = 27
    y = 0
    while y < 7:
        if y ==0:
            print("Point Buy Selection: choose from a pool of 27 points to distribute in the stats that you choose, which must be from 8-15. The stat:point conversion is: 8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:7, 15:9.")
            print(f'{x}/27 Points Remaining')
            strength_choice = dnd_class.RaceStats.point_buy_selection("Strength")
            x = dnd_class.RaceStats.point_buy_cost(strength_choice,x)
            y +=1
        elif y ==1:
            print(f'{x}/27 Points Remaining')
            dex_choice = dnd_class.RaceStats.point_buy_selection("Dexterity")
            x = dnd_class.RaceStats.point_buy_cost(dex_choice,x)
            y +=1
        elif y ==2:
            print(f'{x}/27 Points Remaining')
            con_choice = dnd_class.RaceStats.point_buy_selection("Constitution")
            x = dnd_class.RaceStats.point_buy_cost(con_choice,x)
            if x == 0:
# If all available points have been used, then the rest of the scores must be 8.
                dnd_dict.character_dict['Stats']['strength']['base']=strength_choice
                dnd_dict.character_dict['Stats']['dexterity']['base']=dex_choice
                dnd_dict.character_dict['Stats']['constitution']['base']=con_choice
                dnd_dict.character_dict['Stats']['intelligence']['base']=8
                dnd_dict.character_dict['Stats']['wisdom']['base']=8
                dnd_dict.character_dict['Stats']['charisma']['base']=8
                y +=4
            elif x >0:
                y +=1

        elif y ==3:
            print(f'{x}/27 Points Remaining')
            int_choice = dnd_class.RaceStats.point_buy_selection("Intelligence")
            x = dnd_class.RaceStats.point_buy_cost(int_choice,x)
            if x == 0:
                dnd_dict.character_dict['Stats']['strength']['base']=strength_choice
                dnd_dict.character_dict['Stats']['dexterity']['base']=dex_choice
                dnd_dict.character_dict['Stats']['constitution']['base']=con_choice
                dnd_dict.character_dict['Stats']['intelligence']['base']=int_choice
                dnd_dict.character_dict['Stats']['wisdom']['base']=8
                dnd_dict.character_dict['Stats']['charisma']['base']=8
                y +=3
            elif x >0:
                y +=1

        elif y ==4:
            print(f'{x}/27 Points Remaining')
            wis_choice = dnd_class.RaceStats.point_buy_selection("Wisdom")
            x = dnd_class.RaceStats.point_buy_cost(wis_choice,x)
            if x == 0:
                dnd_dict.character_dict['Stats']['strength']['base']=strength_choice
                dnd_dict.character_dict['Stats']['dexterity']['base']=dex_choice
                dnd_dict.character_dict['Stats']['constitution']['base']=con_choice
                dnd_dict.character_dict['Stats']['intelligence']['base']=int_choice
                dnd_dict.character_dict['Stats']['wisdom']['base']=wis_choice
                dnd_dict.character_dict['Stats']['charisma']['base']=8
                y +=2
            elif x >0:
                y +=1
        elif y ==5:
            print(f'{x}/27 Points Remaining')
            cha_choice = dnd_class.RaceStats.point_buy_selection("Charisma")
            x = dnd_class.RaceStats.point_buy_cost(cha_choice,x)
            if x == 0:
                dnd_dict.character_dict['Stats']['strength']['base']=strength_choice
                dnd_dict.character_dict['Stats']['dexterity']['base']=dex_choice
                dnd_dict.character_dict['Stats']['constitution']['base']=con_choice
                dnd_dict.character_dict['Stats']['intelligence']['base']=int_choice
                dnd_dict.character_dict['Stats']['wisdom']['base']=wis_choice
                dnd_dict.character_dict['Stats']['charisma']['base']=cha_choice
                y +=1
            elif x >0:
                print("Must use all available points.")
                x =27
                y -=5

        if y == 6:
            break

# Enter the character's name with a maximum of 15 characters
def name_selection():
    while True:
        name_input = input("Enter your name (max 15 characters): ")
        if len(name_input) <=15:
            dnd_dict.character_dict.get("name").append(name_input)
            break
        else:
            print("Too many characters, please select again.")
            continue

# Choose if you want to use the standard point array or the stat roller
def stat_selection():
    name_selection()
    while True:
        choice1 = input("Select the stat distribution would you like to use:\n1) Point Buy\n2) Rolling\n3) Point Array\nEnter your selection: ")
        if choice1 == '1':
            point_buy()
            break

        elif choice1 == '2':
            stat_roll()
            break

        elif choice1 == '3':
            point_array()
            break

        else:
            print("Invalid Selection")
            continue
