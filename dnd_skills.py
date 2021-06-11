#!/usr/bin/python3
import dnd_dict, dnd_class

skills_dict = {
    'acrobatics':[],
    'animal_handling':[],
    'arcana':[],
    'athletics':[],
    'deception':[],
    'history':[],
    'insight':[],
    'intimidation':[],
    'investigation':[],
    'medicine':[],
    'nature':[],
    'perception':[],
    'performance':[],
    'persuasion':[],
    'religion':[],
    'sleight_of_hand':[],
    'stealth':[],
    'survival':[]
}
# The Proficiency Bonus that will be used for every skill

prof_bonus = 2

def set_skill():
    skills_dict['acrobatics']=dnd_dict.character_dict['Stats']['dexterity']['mod']
    skills_dict['animal_handling']=dnd_dict.character_dict['Stats']['wisdom']['mod']
    skills_dict['arcana']=dnd_dict.character_dict['Stats']['intelligence']['mod']
    skills_dict['athletics']=dnd_dict.character_dict['Stats']['strength']['mod']
    skills_dict['deception']=dnd_dict.character_dict['Stats']['charisma']['mod']
    skills_dict['history']=dnd_dict.character_dict['Stats']['intelligence']['mod']
    skills_dict['insight']=dnd_dict.character_dict['Stats']['wisdom']['mod']
    skills_dict['intimidation']=dnd_dict.character_dict['Stats']['charisma']['mod']
    skills_dict['investigation']=dnd_dict.character_dict['Stats']['intelligence']['mod']
    skills_dict['medicine']=dnd_dict.character_dict['Stats']['wisdom']['mod']
    skills_dict['nature']=dnd_dict.character_dict['Stats']['intelligence']['mod']
    skills_dict['perception']=dnd_dict.character_dict['Stats']['wisdom']['mod']
    skills_dict['performance']=dnd_dict.character_dict['Stats']['charisma']['mod']
    skills_dict['persuasion']=dnd_dict.character_dict['Stats']['charisma']['mod']
    skills_dict['religion']=dnd_dict.character_dict['Stats']['intelligence']['mod']
    skills_dict['sleight_of_hand']=dnd_dict.character_dict['Stats']['dexterity']['mod']
    skills_dict['stealth']=dnd_dict.character_dict['Stats']['dexterity']['mod']
    skills_dict['survival']=dnd_dict.character_dict['Stats']['wisdom']['mod']

# Used to determine skill proficiency.
# If the skill already equals the stat modifier, then add the proficiency modifier to it. Otherwise, go back to the start of the loop.

def acrobatics_prof():
    while True:
        if skills_dict['acrobatics']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
            acr_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
            updated_acr = dnd_class.RaceStats.stat_bonus(acr_mod,prof_bonus)
            skills_dict['acrobatics']=updated_acr
            break
        elif skills_dict['acrobatics']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
            break


def animal_handling_prof():
    while True:
        if skills_dict['animal_handling']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
            anm_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
            updated_anm = dnd_class.RaceStats.stat_bonus(anm_mod,prof_bonus)
            skills_dict['animal_handling']=updated_anm
            break
        elif skills_dict['animal_handling']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
            break

def arcana_prof():
    while True:
        if skills_dict['arcana']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
            arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
            updated_arc = dnd_class.RaceStats.stat_bonus(arc_mod,prof_bonus)
            skills_dict['arcana']=updated_arc
            break
        elif skills_dict['arcana']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
            break

def athletics_prof():
    while True:
        if skills_dict['athletics']==dnd_dict.character_dict['Stats']['strength']['mod']:
            ath_mod = dnd_dict.character_dict['Stats']['strength']['mod']
            updated_ath = dnd_class.RaceStats.stat_bonus(ath_mod,prof_bonus)
            skills_dict['athletics']=updated_ath
            break
        elif skills_dict['athletics']>dnd_dict.character_dict['Stats']['strength']['mod']:
            break

def deception_prof():
    while True:
        if skills_dict['deception']==dnd_dict.character_dict['Stats']['charisma']['mod']:
            dec_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
            updated_dec = dnd_class.RaceStats.stat_bonus(dec_mod,prof_bonus)
            skills_dict['deception']=updated_dec
            break
        elif skills_dict['deception']>dnd_dict.character_dict['Stats']['charisma']['mod']:
            break

def history_prof():
    while True:
        if skills_dict['history']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
            his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
            updated_his = dnd_class.RaceStats.stat_bonus(his_mod,prof_bonus)
            skills_dict['history']=updated_his
            break
        elif skills_dict['history']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
            break

def insight_prof():
    while True:
        if skills_dict['insight']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
            ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
            updated_ins = dnd_class.RaceStats.stat_bonus(ins_mod,prof_bonus)
            skills_dict['insight']=updated_ins
            break
        elif skills_dict['insight']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
            break

def intimidation_prof():
    while True:
        if skills_dict['intimidation']==dnd_dict.character_dict['Stats']['charisma']['mod']:
            itd_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
            updated_itd = dnd_class.RaceStats.stat_bonus(itd_mod,prof_bonus)
            skills_dict['intimidation']=updated_itd
            break
        elif skills_dict['intimidation']>dnd_dict.character_dict['Stats']['charisma']['mod']:
            break

def investigation_prof():
    while True:
        if skills_dict['investigation']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
            inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
            updated_inv = dnd_class.RaceStats.stat_bonus(inv_mod,prof_bonus)
            skills_dict['investigation']=updated_inv
            break
        elif skills_dict['investigation']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
            break

def medicine_prof():
    while True:
        if skills_dict['medicine']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
            med_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
            updated_med = dnd_class.RaceStats.stat_bonus(med_mod,prof_bonus)
            skills_dict['medicine']=updated_med
            break
        elif skills_dict['medicine']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
            break

def nature_prof():
    while True:
        if skills_dict['nature']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
            nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
            updated_nat = dnd_class.RaceStats.stat_bonus(nat_mod,prof_bonus)
            skills_dict['nature']=updated_nat
            break
        elif skills_dict['nature']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
            break

def perception_prof():
    while True:
        if skills_dict['perception']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
            prc_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
            updated_prc = dnd_class.RaceStats.stat_bonus(prc_mod,prof_bonus)
            skills_dict['perception']=updated_prc
            break
        elif skills_dict['perception']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
            break

def performance_prof():
    while True:
        if skills_dict['performance']==dnd_dict.character_dict['Stats']['charisma']['mod']:
            prf_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
            updated_prf = dnd_class.RaceStats.stat_bonus(prf_mod,prof_bonus)
            skills_dict['performance']=updated_prf
            break
        elif skills_dict['performance']>dnd_dict.character_dict['Stats']['charisma']['mod']:
            break

def persuasion_prof():
    while True:
        if skills_dict['persuasion']==dnd_dict.character_dict['Stats']['charisma']['mod']:
            per_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
            updated_per = dnd_class.RaceStats.stat_bonus(per_mod,prof_bonus)
            skills_dict['persuasion']=updated_per
            break
        elif skills_dict['persuasion']>dnd_dict.character_dict['Stats']['charisma']['mod']:
            break

def religion_prof():
    while True:
        if skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
            rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
            updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,prof_bonus)
            skills_dict['religion']=updated_rel
            break
        elif skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
            break

def sleight_of_hand_prof():
    while True:
        if skills_dict['sleight_of_hand']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
            soh_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
            updated_soh = dnd_class.RaceStats.stat_bonus(soh_mod,prof_bonus)
            skills_dict['sleight_of_hand']=updated_soh
            break
        elif skills_dict['sleight_of_hand']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
            break

def stealth_prof():
    while True:
        if skills_dict['stealth']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
            stl_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
            updated_stl = dnd_class.RaceStats.stat_bonus(stl_mod,prof_bonus)
            skills_dict['stealth']=updated_stl
            break
        elif skills_dict['stealth']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
            break

def survival_prof():
    while True:
        if skills_dict['survival']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
            sur_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
            updated_sur = dnd_class.RaceStats.stat_bonus(sur_mod,prof_bonus)
            skills_dict['survival']=updated_sur
            break
        elif skills_dict['survival']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
            break


#Selecting all skills
def skill_choice():
    while True:
        choice1 = input("Select the skill you want proficiency in:\n1) Acrobatics\n2) Animal Handling\n3) Arcana\n4) Athletics\n5) Deception\n6) History\n7) Insight\n8) Intimidation\n9) Investigation\n10) Medicine\n11) Nature\n12) Perception\n13) Performance\n14) Persuasion\n15) Religion\n16) Sleight of Hand\n17) Stealth\n18) Survival\nEnter your Selection: ")
        if choice1=='1':
            if skills_dict['acrobatics']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                acr_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                updated_acr = dnd_class.RaceStats.stat_bonus(acr_mod, prof_bonus)
                skills_dict['acrobatics'] = updated_acr
                break
            elif skills_dict['acrobatics']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                print("Already proficient")
                continue
 
 
        elif choice1=='2':
            if skills_dict['animal_handling']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                anm_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                updated_anm = dnd_class.RaceStats.stat_bonus(anm_mod,prof_bonus)
                skills_dict['animal_handling'] = updated_anm
                break
            elif skills_dict['animal_handling']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='3':
            if skills_dict['arcana']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                arc_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_arc = dnd_class.RaceStats.stat_bonus(arc_mod,prof_bonus)
                skills_dict['arcana']=updated_arc
                break
            elif skills_dict['arcana']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='4':
            if skills_dict['athletics']==dnd_dict.character_dict['Stats']['strength']['mod']:
                ath_mod = dnd_dict.character_dict['Stats']['strength']['mod']
                updated_ath = dnd_class.RaceStats.stat_bonus(ath_mod,prof_bonus)
                skills_dict['athletics']=updated_ath
                break
            elif skills_dict['athletics']>dnd_dict.character_dict['Stats']['strength']['mod']:
                print("Already proficient")
                continue
 
 
        elif choice1=='5':
            if skills_dict['deception']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                dec_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                updated_dec = dnd_class.RaceStats.stat_bonus(dec_mod,prof_bonus)
                skills_dict['deception']=updated_dec
                break
            elif skills_dict['deception']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='6':
            if skills_dict['history']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                his_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_his = dnd_class.RaceStats.stat_bonus(his_mod,prof_bonus)
                skills_dict['history']=updated_his
                break
            elif skills_dict['history']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='7':
            if skills_dict['insight']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                updated_ins = dnd_class.RaceStats.stat_bonus(ins_mod,prof_bonus)
                skills_dict['insight']=updated_ins
                break
            elif skills_dict['insight']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='8':
            if skills_dict['intimidation']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                itd_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                updated_itd = dnd_class.RaceStats.stat_bonus(itd_mod,prof_bonus)
                skills_dict['intimidation']=updated_itd
                break
            elif skills_dict['intimidation']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='9':
            if skills_dict['investigation']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_inv = dnd_class.RaceStats.stat_bonus(inv_mod,prof_bonus)
                skills_dict['investigation']=updated_inv
                break
            elif skills_dict['investigation']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='10':
            if skills_dict['medicine']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                med_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                updated_med = dnd_class.RaceStats.stat_bonus(med_mod,prof_bonus)
                skills_dict['medicine']=updated_med
                break
            elif skills_dict['medicine']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='11':
            if skills_dict['nature']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                nat_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_nat = dnd_class.RaceStats.stat_bonus(nat_mod,prof_bonus)
                skills_dict['nature']=updated_nat
                break
            elif skills_dict['nature']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='12':
            if skills_dict['perception']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                prc_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                updated_prc = dnd_class.RaceStats.stat_bonus(prc_mod,prof_bonus)
                skills_dict['perception']=updated_prc
                break
            elif skills_dict['perception']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='13':
            if skills_dict['performance']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                prf_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                updated_prf = dnd_class.RaceStats.stat_bonus(prf_mod,prof_bonus)
                skills_dict['performance']=updated_prf
                break
            elif skills_dict['performance']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='14':
            if skills_dict['persuasion']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                per_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                updated_per = dnd_class.RaceStats.stat_bonus(per_mod,prof_bonus)
                skills_dict['persuasion']=updated_per
                break
            elif skills_dict['persuasion']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='15':
            if skills_dict['religion']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                rel_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_rel = dnd_class.RaceStats.stat_bonus(rel_mod,prof_bonus)
                skills_dict['religion']=updated_rel
                break
            elif skills_dict['religion']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='16':
            if skills_dict['sleight_of_hand']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                soh_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                updated_soh = dnd_class.RaceStats.stat_bonus(soh_mod,prof_bonus)
                skills_dict['sleight_of_hand']=updated_soh
                break
            elif skills_dict['sleight_of_hand']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='17':
            if skills_dict['stealth']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                stl_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                updated_stl = dnd_class.RaceStats.stat_bonus(stl_mod,prof_bonus)
                skills_dict['stealth']=updated_stl
                break
            elif skills_dict['stealth']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                print("Already proficient")
                continue

        elif choice1=='18':
            if skills_dict['survival']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                sur_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                updated_sur = dnd_class.RaceStats.stat_bonus(sur_mod,prof_bonus)
                skills_dict['survival']=updated_sur
                break
            elif skills_dict['survival']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                print("Already proficient")
                continue

        else:
            print("Invalid Selection")
            continue


# Double the proficiency for a stat that already has proficiency
def expertise():
    while True:
        choice = input("Select the skill you want proficiency in:\n1) Acrobatics\n2) Animal Handling\n3) Arcana\n4) Athletics\n5) Deception\n6) History\n7) Insight\n8) Intimidation\n9) Investigation\n10) Medicine\n11) Nature\n12) Perception\n13) Performance\n14) Persuasion\n15) Religion\n16) Sleight of Hand\n17) Stealth\n18) Survival\nEnter your Selection: ")

        if choice=='1':
            if skills_dict['acrobatics']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['dexterity']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['acrobatics'],prof_bonus)
                skills_dict['acrobatics']=new_skill
                break
            elif skills_dict['acrobatics']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['dexterity']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue
 
        elif choice=='2':
            if skills_dict['animal_handling']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['animal_handling'],prof_bonus)
                skills_dict['animal_handling']=new_skill
                break
            elif skills_dict['animal_handling']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='3':
            if skills_dict['arcana']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['arcana'],prof_bonus)
                skills_dict['arcana']=new_skill
                break
            elif skills_dict['arcana']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='4':
            if skills_dict['athletics']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['strength']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['athletics'],prof_bonus)
                skills_dict['athletics']=new_skill
                break
            elif skills_dict['athletics']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['strength']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='5':
            if skills_dict['deception']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['charisma']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['deception'],prof_bonus)
                skills_dict['deception']=new_skill
                break
            elif skills_dict['deception']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['charisma']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='6':
            if skills_dict['history']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['history'],prof_bonus)
                skills_dict['history']=new_skill
                break
            elif skills_dict['history']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='7':
            if skills_dict['insight']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['insight'],prof_bonus)
                skills_dict['insight']=new_skill
                break
            elif skills_dict['insight']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='8':
            if skills_dict['intimidation']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['charisma']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['intimidation'],prof_bonus)
                skills_dict['intimidation']=new_skill
                break
            elif skills_dict['intimidation']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['charisma']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='9':
            if skills_dict['investigation']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['investigation'],prof_bonus)
                skills_dict['investigation']=new_skill
                break
            elif skills_dict['investigation']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='10':
            if skills_dict['medicine']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['medicine'],prof_bonus)
                skills_dict['medicine']=new_skill
                break
            elif skills_dict['medicine']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='11':
            if skills_dict['nature']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['nature'],prof_bonus)
                skills_dict['nature']=new_skill
                break
            elif skills_dict['nature']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='12':
            if skills_dict['perception']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['perception'],prof_bonus)
                skills_dict['perception']=new_skill
                break
            elif skills_dict['perception']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue
 
        elif choice=='13':
            if skills_dict['performance']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['charisma']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['performance'],prof_bonus)
                skills_dict['performance']=new_skill
                break
            elif skills_dict['performance']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['charisma']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='14':
            if skills_dict['persuasion']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['charisma']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['persuasion'],prof_bonus)
                skills_dict['persuasion']=new_skill
                break
            elif skills_dict['persuasion']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['charisma']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='15':
            if skills_dict['religion']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['religion'],prof_bonus)
                skills_dict['religion']=new_skill
                break
            elif skills_dict['religion']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['intelligence']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='16':
            if skills_dict['sleight_of_hand']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['dexterity']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['sleight_of_hand'],prof_bonus)
                skills_dict['sleight_of_hand']=new_skill
                break
            elif skills_dict['sleight_of_hand']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['dexterity']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='17':
            if skills_dict['stealth']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['dexterity']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['stealth'],prof_bonus)
                skills_dict['stealth']=new_skill
                break
            elif skills_dict['stealth']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['dexterity']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        elif choice=='18':
            if skills_dict['survival']==dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],prof_bonus):
                new_skill= dnd_class.RaceStats.stat_bonus(skills_dict['survival'],prof_bonus)
                skills_dict['survival']=new_skill
                break
            elif skills_dict['survival']<dnd_class.RaceStats.stat_bonus(dnd_dict.character_dict['Stats']['wisdom']['mod'],prof_bonus):
                print("You Are Not Proficient With This Skill")
                continue

        else:
            print("Invalid Selection")
            continue




# Skill list for rogue. Will be repeated 4 times in the Rogue function.
def rogue_skills():
    while True:
        choice1 = input("Select the skill you want proficiency in:\n1) Acrobatics\n2) Athletics\n3) Deception\n4) Insight\n5) Intimidation\n6) Investigation\n7) Perception\n8) Performance\n9) Persuasion\n10) Sleight of Hand\n11) Stealth\nEnter your Selection: ")
        if choice1=='1':
            if skills_dict['acrobatics']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                acr_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                updated_acr = dnd_class.RaceStats.stat_bonus(acr_mod, prof_bonus)
                skills_dict['acrobatics'] = updated_acr
                break
            elif skills_dict['acrobatics']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='2':
            if skills_dict['athletics']==dnd_dict.character_dict['Stats']['strength']['mod']:
                ath_mod = dnd_dict.character_dict['Stats']['strength']['mod']
                updated_ath = dnd_class.RaceStats.stat_bonus(ath_mod,prof_bonus)
                skills_dict['athletics']=updated_ath
                break
            elif skills_dict['athletics']>dnd_dict.character_dict['Stats']['strength']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='3':
            if skills_dict['deception']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                dec_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                updated_dec = dnd_class.RaceStats.stat_bonus(dec_mod,prof_bonus)
                skills_dict['deception']=updated_dec
                break
            elif skills_dict['deception']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='4':
            if skills_dict['insight']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                ins_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                updated_ins = dnd_class.RaceStats.stat_bonus(ins_mod,prof_bonus)
                skills_dict['insight']=updated_ins
                break
            elif skills_dict['insight']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='5':
            if skills_dict['intimidation']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                itd_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                updated_itd = dnd_class.RaceStats.stat_bonus(itd_mod,prof_bonus)
                skills_dict['intimidation']=updated_itd
                break
            elif skills_dict['intimidation']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='6':
            if skills_dict['investigation']==dnd_dict.character_dict['Stats']['intelligence']['mod']:
                inv_mod = dnd_dict.character_dict['Stats']['intelligence']['mod']
                updated_inv = dnd_class.RaceStats.stat_bonus(inv_mod,prof_bonus)
                skills_dict['investigation']=updated_inv
                break
            elif skills_dict['investigation']>dnd_dict.character_dict['Stats']['intelligence']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='7':
            if skills_dict['perception']==dnd_dict.character_dict['Stats']['wisdom']['mod']:
                prc_mod = dnd_dict.character_dict['Stats']['wisdom']['mod']
                updated_prc = dnd_class.RaceStats.stat_bonus(prc_mod,prof_bonus)
                skills_dict['perception']=updated_prc
                break
            elif skills_dict['perception']>dnd_dict.character_dict['Stats']['wisdom']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='8':
            if skills_dict['performance']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                prf_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                updated_prf = dnd_class.RaceStats.stat_bonus(prf_mod,prof_bonus)
                skills_dict['performance']=updated_prf
                break
            elif skills_dict['performance']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='9':
            if skills_dict['persuasion']==dnd_dict.character_dict['Stats']['charisma']['mod']:
                per_mod = dnd_dict.character_dict['Stats']['charisma']['mod']
                updated_per = dnd_class.RaceStats.stat_bonus(per_mod,prof_bonus)
                skills_dict['persuasion']=updated_per
                break
            elif skills_dict['persuasion']>dnd_dict.character_dict['Stats']['charisma']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='10':
            if skills_dict['sleight_of_hand']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                soh_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                updated_soh = dnd_class.RaceStats.stat_bonus(soh_mod,prof_bonus)
                skills_dict['sleight_of_hand']=updated_soh
                break
            elif skills_dict['sleight_of_hand']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                print("Already proficient")
                continue
 
        elif choice1=='11':
            if skills_dict['stealth']==dnd_dict.character_dict['Stats']['dexterity']['mod']:
                stl_mod = dnd_dict.character_dict['Stats']['dexterity']['mod']
                updated_stl = dnd_class.RaceStats.stat_bonus(stl_mod,prof_bonus)
                skills_dict['stealth']=updated_stl
                break
            elif skills_dict['stealth']>dnd_dict.character_dict['Stats']['dexterity']['mod']:
                print("Already proficient")
                continue

        else:
            print("Invalid Selection")
            continue

# Run expertise 6 times.
def expertise_choice():
    i = 1
    for i in range(i,3):
        if i < 3:
            print(f'{i}/2')
            expertise()
            i +=1
            continue
        if i == 3:
            break


# Used for Half-Elf Skills
def half_elf_skills():
    x = 1
    for x in range(x,3):
        if x < 3:
            print(f'{x}/2')
            skill_choice()
            x += 1
            continue

        elif x == 3:
            break


# Used for Bard Skills
def bard_skills():
    x = 1
    for x in range(x,5):
        if x < 5:
            print(f'{x}/4')
            skill_choice()
            x += 1
            continue

        elif x == 5:
            break


def rogue_skill_choice():
    x = 1
    for x in range(x,5):
        if x < 5:
            print(f'{x}/4')
            rogue_skills()
            x += 1
            continue

        elif x == 5:
            break
