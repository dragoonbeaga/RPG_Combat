import random
import dice
import os

# Character

def Amiri():
    stats = {'hp': 22, 'hp_now': 22, 'str':{'val': 18, 'mod': 4}, 'dex':{'val': 14, 'mod':2}, 'con':{'val':14,'mod':2},
             'int':{'val': 10, 'mod':0},'wis':{'val':10, 'mod':0}, 'cha':{'val':12, 'mod':1}}
    weapon = {}
    attack_roll = dice.roll('1d20t')
    print(attack_roll)
    if attack_roll + stats['str']['mod'] >= 15:
        print("we did it")
Amiri()