#!/usr/bin/python3
from __future__ import print_function
import os, math

class Character:
    def __init__(self, stat,skill,bonus):
        self.stat = stat
        self.bonus = bonus
        self.skill = skill


# Determines the initial stats of the character.
# Only accepts integers
# Must be between 3 and 18
    def initial_stat(stat_type):
        while True:
            try:
                stat = int(input(f'Enter your {stat_type}: '))
                if stat > 2 and stat < 19:
                    break
                else:
                    print("Invalid Input. Must Be An Integer Between 3 and 18")
            except ValueError:
                print("Invalid Input Enter an Integer")
        return stat

# Used to determine the modifiers, +1 for every even above 10, -1 for every odd below 10. A score of 10 is a +0 modifier.
    def mod(stat):
        count = 0
        if stat == 10:
            count = 0
            return count

#Add 1 to the modifier for every even number above 10
        elif stat > 10:
            stat_range = range(11, stat, 2)
            count += len(stat_range)
            return count

#Subtract 1 from the modifier for every odd number below 10.
        elif stat < 10:
            stat_range = range(11, stat, -2)
            count -= len(stat_range)
            return count


# Used to determine skill proficiency. If you are already proficient, then it
# does not add the bonus again
    def skill_prof(skill,bonus, stat):
        if skill == (stat+bonus):
            print(f'You are already proficient with {skill}')
            return False
        else:
            skill == (stat+bonus)
            return



# Used to display skill scores.
# If you are proficient in a skill, put a (*) before it.
# If you have expertise because of the Rogue feature, put an E before that as well
# Otherwise, just put the modifier.
    def show_prof(skill, bonus, stat):
        if skill == (stat+bonus):
            vals = f"(*) {skill}"
            return vals
        elif skill == (stat + bonus + bonus):
            vals = f"(E)(*) {skill}"
            return vals
        else:
            return skill

#Determines the stat bonuses the different races give.
class RaceStats:
    def __init__(self, race, speed, size, stat, language, bonus, skill, base, dict, dice):
        self.race = race
        self.speed = speed
        self.size = size
        self.stat = stat
        self.language = language
        self.bonus = bonus
        self.skill = skill
        self.base = base
        self.dict = dict
        self.dice = dice

#Prints the race name, speed, size, and language.
    def racial_choice(race, speed, size):
        print(f'Race: {race}')
        print(f'Speed: {speed} feet')
        print(f'Your size is: {size}')



#Method for calculating the stat bonuses
    def stat_bonus(stat, bonus):
        return (stat + bonus)

# If an entry is already present in a dictionary, pass. Otherwise, proceed normally
    def pass_function(dict,skill):
        if dict:
            pass
        else:
            dict.append(skill)

# If a specific entry is already present in a dictionary, pass. Otherwise, proceed normally
    def pass_repeat_function(dict,skill):
        if skill in dict:
            pass
        else:
            dict.append(skill)

# Used to display Hit Dice. If there are none, then do not display them
# Tabbed for ease of reading in case more are ever added.
    def hit_dice_display(dict,stat):
        if dict > 0:
            return print(f'Hit Dice: {dict}{stat}')

# Select the stat you want, from 8-15.
    def point_buy_selection(stat):
        while True:
            choice = int(input(f"{stat} Selection, please input the number you want (from 8-15): "))
            if choice >=8 and choice <=15:
                return choice
            else:
                print("Choice must be an integer between 8-15")
                continue

# Point Buy stat selection, where you have 27 points to distribute between the stats, which can be from 8-15 for all of them. The stat and cost are: 8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:7, 15:9.
    def point_buy_cost(stat,base):
        if stat == 8:
            base = base-0
            return base

        elif stat == 9:
            base = base-1
            return base

        elif stat == 10:
            base = base-2
            return base

        elif stat == 11:
            base = base-3
            return base

        elif stat == 12:
            base = base-4
            return base

        elif stat == 13:
            base = base-5
            return base

        elif stat == 14:
            base = base-7
            return base

        elif stat == 15:
            base = base-9
            return base

# Method for determining Medium Armor Class. The Dexterity Modifier can only be a maximum of 2.
    def med_armor(stat):
        if stat > 2:
            stat = 2
            return stat
        else:
            return stat

# Determines and displays the Spell Spell Attack (Proficiency Bonus + Stat Modifier)
    def spell_attack(bonus, stat):
        return (bonus+stat)

# Determines and displays the Spell Save DC (8 + Proficiency Bonus + Stat Modifier) 
    def spell_save(bonus,stat):
        return (8+bonus+stat)

