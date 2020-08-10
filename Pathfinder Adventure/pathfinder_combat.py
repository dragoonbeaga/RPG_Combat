import dice

# Character

def Amiri():
    global stats
    global weapon
    global rage
    rage = False
    stats = {'hp': 35, 'hp_now': 35, 'str':{'val': 18, 'mod': 4}, 'dex':{'val': 14, 'mod':2}, 'con':{'val':14,'mod':2},
             'int':{'val': 10, 'mod':0},'wis':{'val':10, 'mod':0}, 'cha':{'val':12, 'mod':1}, 'ac': 18 }
    weapon = {'LBS_Mod': 6, 'LBS_Damage': '1d8t', 'LBS_Damage_Mod': 4, 'LBS_Rage_Damage': 10}

def wolf1():
    global wolf1_stats
    global wolf1_attack
    global move1
    move1 = [1]
    wolf1_stats = {'hp': 8, 'str': 1, 'dex': 2, 'con': 0, 'int': -4, 'wis': 1, 'cha': -2, 'ac': 15}
    wolf1_attack = {'jaws': {'val': 6,'mod': wolf1_stats['dex'], 'damage': '1d6t', 'd_mod': 1}}

def wolf2():
    global wolf2_stats
    global wolf2_attack
    global move2
    move2 = [1]
    wolf2_stats = {'hp': 8, 'str': 1, 'dex': 2, 'con': 0, 'int': -4, 'wis': 1, 'cha': -2, 'ac': 15}
    wolf2_attack = {'jaws': {'val': 6,'mod': wolf1_stats['dex'], 'damage': '1d6t', 'd_mod': 1}}

def Caustic_Wolf():
    global caustic_stats
    global caustic_attack
    global move3
    move3 = [0]
    caustic_stats = {'hp': 30, 'str': 2, 'dex': 4, 'con': 2, 'int': -4, 'wis': 2, 'cha': 2, 'ac': 18}
    caustic_attack = {'jaws': {'val': 11,'mod': caustic_stats['str'], 'damage': '1d6t', 'd_mod': 2}}



def attack():
    attack_roll = dice.roll('1d20t')
    return attack_roll


def story_intro():
    input(f"Press Enter to Continue through text: ")
    print("It has been three days since you left Elidir, climbing into the back of one of Bort Bargith’s wagons bound for the faraway Andoran capital of Almas.", end='')
    input(f"")
    print(" ")
    print("The smiling caravan master cut your travel cost to only a handful of coppers,so long as you promised to protect the wagons should any trouble arise.", end='')
    input(f"")
    print(" ")
    print("Fortunately, your journey through the hinterlands of Isger has been quiet, even if the ride itself has been far from comfortable", end='')
    input(f"")
    print(" ")
    print("As you broke camp this morning, Bort announced you should arrive at the town of Etran’s Folly by nightfall, and he promised a comfortable bed for the night as a reward for a long day’s travel.", end='')
    input(f"")
    print(" ")
    print("The caravan’s teamsters shared a chuckle between them, trading knowing glances and subtle nods, but soon enough you are on the road again, the wagon bouncing and creaking along the uneven trail.", end='')
    input(f"")
    player()

def player():
    print(" ")
    print("You are Human Barbarian. Your Name is Amiri. In Combat you can rage to gain 3 extra hit points and do 6 extra damage.", end='')
    input(f"")
    wolves_attack()

def wolves_attack():
    print(" ")
    print("“Up ahead is Plaguestone,” Keldaran shouts from the front of the wagon.", end='')
    input(f"")
    print(" ")
    print("No sooner does the call fade from his lips than it is overshadowed by a series of long, mournful howls emanating from the woods to either side of the caravan.", end='')
    print(" ")
    print("You get out of the wagon and see two wolves come up behind your wagon about 15 feet away", end='')
    print(" ")
    combat_player()


def combat_player():
    action_list = ["Draw Weapon", "Rage", "Move to wolf on the left", "Move to the wolf on the right", "Attack"]
    actions = 0
    hidden = 0
    global rage
    rage == False
    print("You get 3 actions per turn choose wisely.")
    print(f"1.{action_list[0]}\n2.{action_list[1]}\n3.{action_list[2]}\n4.{action_list[3]}")
    while actions < 3:
        choice = str(input(f"Please enter your choice:"))
        if choice == "1":
            hidden += 1
            actions += 1
            if hidden == 1:
                print(f"Actions taken: {actions}")
                print(f"You draw your large bastard sword and get ready to attack.\n")
                print(f"2.{action_list[1]}\n3.{action_list[2]}\n4.{action_list[3]}")
            elif hidden == 3:
                print(f"Actions taken: {actions}")
                print(f"You draw your large bastard sword and get ready to attack.\n")
                print(f"3.{action_list[2]}\n4.{action_list[3]}")
            elif hidden == 4:
                hidden += 2
                print(f"Actions taken: {actions}")
                print(f"You draw your large bastard sword and get ready to attack.\n")
                print(f"2.{action_list[1]}\n5.{action_list[4]}")
            elif hidden == 5:
                print(f"Actions taken: {actions}")
                print(f"You draw your weapon and get ready to attack.\n")
                print(f"2.{action_list[1]}\n6.{action_list[4]}\n")
            elif hidden == 6:
                print(f"Actions taken: {actions}")
                print(f"You draw your weapon and get ready to attack.\nBut You couldn't draw your weapon fast enough to"
                      f"defend against the wolf's lunge\n")
                move1[0] -= 1
                wolf1_combat()
            elif hidden == 7:
                print(f"Actions taken: {actions}")
                print(f"You draw your weapon and get ready to attack.\nBut You couldn't draw your weapon fast enough to"
                      f"defend against the wolf's lunge\n")
                move2[0] -= 1
                wolf2_combat()
        elif choice == "2":
            actions += 1
            hidden += 2
            rage = True
            if hidden == 2:
                print(f"Actions taken: {actions}")
                print("A red mist surrounds you as you give into your rage\n")
                print(f"1.{action_list[0]}\n3.{action_list[2]}\n4.{action_list[3]}")
            elif hidden == 3:
                print(f"Actions taken: {actions}")
                print("A red mist surrounds you as you give into your rage\n")
                print(f"3.{action_list[2]}\n4.{action_list[3]}")
            elif hidden == 5:
                print(f"Actions taken: {actions}")
                print("A red mist surrounds you as you give into your rage\n")
                print(f"1.{action_list[0]}")
            elif hidden == 6:
                print(f"Actions taken: {actions}")
                print("A red mist surrounds you as you give into your rage\n")
                print(f"1.{action_list[0]}")
            elif hidden == 7:
                print(f"Actions taken: {actions}")
                print("As the red mist surrounds you and you give into your rage, the wolf in front of you lunges"
                      "for an attack.\n")
                move1[0] -= 1
                wolf1_combat()
            elif hidden == 8:
                print(f"Actions taken: {actions}")
                print("A red mist surrounds you as you give into your rage.\n")
                move2[0] -= 1
                wolf2_combat()
        elif choice == "3":
            actions += 1
            hidden += 3
            if hidden == 3:
                print(f"Actions taken: {actions}")
                print("You charge to the wolf on the left without your sword drawn, facing it down.\n")
                print(f"1.{action_list[0]}\n2.{action_list[1]}")
            elif hidden == 4:
                hidden += 2
                print(f"Actions taken: {actions}")
                print("You charge to the wolf on the left and get ready to attack it.\n")
                print(f"2.{action_list[1]}\n5.{action_list[4]}")
            elif hidden == 5:
                print(f"Actions taken: {actions}")
                print("You charge to the wolf on the left full of rage but unarmed.\n")
                print(f"1.{action_list[0]}\n")
            elif hidden == 6:
                print(f"Actions taken: {actions}")
                print("You charge to the wolf on the left full of rage and get ready to attack it.\n")
                move1[0] -= 1
                wolf1_combat()
        elif choice == "4":
            actions += 1
            hidden += 4
            if hidden == 4:
                print(f"Actions taken: {actions}")
                print("You charge to the wolf on the right without your sword drawn, facing it down\n")
                print(f"1.{action_list[0]}\n2.{action_list[1]}")
            elif hidden == 5:
                hidden += 2
                print(f"Actions taken: {actions}")
                print("You charge to the wolf on the right and get ready to attack it.\n")
                print(f"2.{action_list[1]}\n6.{action_list[4]}")
            elif hidden == 6:
                print(f"Actions taken: {actions}")
                print("You charge to the wolf on the right full of rage but unarmed.\n")
                print(f"1.{action_list[0]}\n")
            elif hidden == 7:
                print(f"Actions taken: {actions}")
                print("You charge to the wolf on the right and get ready to attack it.\n")
                move2[0] -= 1
                wolf2_combat()
        elif choice == "5":
            actions += 1
            move1[0] -= 1
            wolf1_death()
        elif choice == "6":
            actions += 1
            move2[0] -= 1
            wolf2_death()
        else:
            print("That isn't a valid input")


def wolf1_death():
    attack_roll = attack()
    attack_roll += weapon['LBS_Mod']
    attack_roll += stats['str']['mod']
    if attack_roll >= wolf1_stats['ac']:
        damage = 0
        damage += dice.roll(weapon['LBS_Damage'])
        damage += weapon['LBS_Rage_Damage']
        wolf1_stats['hp'] -= damage
        if wolf1_stats['hp'] <= 0:
            str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "                        "covering you.\n"))
            Caustic_Combat()
        elif wolf1_stats['hp'] >= 4:
            str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                    " he still stands growling at you.\n"))
        elif wolf1_stats['hp'] < 4:
            str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                        " stands his ground growing at you.\n"))
    else:
        print("You swing your sword but it jumps out of the way.\n")
    wolf1_combat()

def wolf1_death2():
    attack_roll = attack()
    attack_roll += weapon['LBS_Mod']
    attack_roll += stats['str']['mod']
    if penalty == 1:
        if attack_roll >= wolf1_stats['ac']:
            if rage:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Rage_Damage']
                wolf1_stats['hp'] -= damage
                if wolf1_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                            "covering you.\n"))
                elif wolf1_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                            " he still stands growling at you.\n"))
                elif wolf1_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                            " stands his ground growing at you.\n"))
            else:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Damage_Mod']
                wolf1_stats['hp'] -= damage
                if wolf1_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif wolf1_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif wolf1_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
        else:
            print("You swing your sword but it jumps out of the way.\n")
    elif penalty == 2:
        attack_roll -= 5
        if attack_roll >= wolf1_stats['ac']:
            if rage:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Rage_Damage']
                wolf1_stats['hp'] -= damage
                if wolf1_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                            "covering you.\n"))
                elif wolf1_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                            " he still stands growling at you.\n"))
                elif wolf1_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                            " stands his ground growing at you.\n"))
            else:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Damage_Mod']
                wolf1_stats['hp'] -= damage
                if wolf1_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif wolf1_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif wolf1_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
        else:
            print("You swing your sword but it jumps out of the way.\n")
    elif penalty == 3:
        attack_roll -= 10
        if attack_roll >= wolf1_stats['ac']:
            if rage:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Rage_Damage']
                wolf1_stats['hp'] -= damage
                if wolf1_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                            "covering you.\n"))
                elif wolf1_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                            " he still stands growling at you.\n"))
                elif wolf1_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                            " stands his ground growing at you.\n"))
            else:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Damage_Mod']
                wolf1_stats['hp'] -= damage
                if wolf1_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif wolf1_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif wolf1_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
        else:
            print("You swing your sword but it jumps out of the way.\n")
def wolf2_death():
    attack_roll = attack()
    attack_roll += weapon['LBS_Mod']
    attack_roll += stats['str']['mod']
    if attack_roll >= wolf1_stats['ac']:
        damage = 0
        damage += dice.roll(weapon['LBS_Damage'])
        damage += weapon['LBS_Damage_Mod']
        wolf2_stats['hp'] -= damage
        if wolf2_stats['hp'] <= 0:
            str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                    "covering you.\n"))
            Caustic_Combat()
        elif wolf2_stats['hp'] >= 4:
            str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                    " he still stands growling at you.\n"))
        elif wolf2_stats['hp'] < 4:
            str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                    " stands his ground growling at you.\n"))
    else:
        print("You swing your sword but it jumps out of the way.\n")
    wolf2_combat()
def wolf2_death2():
    attack_roll = attack()
    attack_roll += weapon['LBS_Mod']
    attack_roll += stats['str']['mod']
    if penalty == 1:
        if attack_roll >= wolf2_stats['ac']:
            if rage:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Rage_Damage']
                wolf2_stats['hp'] -= damage
                if wolf2_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                            "covering you.\n"))
                elif wolf2_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                            " he still stands growling at you.\n"))
                elif wolf2_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                            " stands his ground growing at you.\n"))
            else:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Damage_Mod']
                wolf2_stats['hp'] -= damage
                if wolf2_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif wolf2_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif wolf2_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
        else:
            print("You swing your sword but it jumps out of the way.\n")
    elif penalty == 2:
        attack_roll -= 5
        if attack_roll >= wolf2_stats['ac']:
            if rage:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Rage_Damage']
                wolf2_stats['hp'] -= damage
                if wolf2_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                            "covering you.\n"))
                elif wolf2_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                            " he still stands growling at you.\n"))
                elif wolf2_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                            " stands his ground growing at you.\n"))
            else:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Damage_Mod']
                wolf2_stats['hp'] -= damage
                if wolf2_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif wolf2_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif wolf2_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
        else:
            print("You swing your sword but it jumps out of the way.\n")
    elif penalty == 3:
        attack_roll -= 10
        if attack_roll >= wolf2_stats['ac']:
            if rage:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Rage_Damage']
                wolf2_stats['hp'] -= damage
                if wolf2_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                            "covering you.\n"))
                elif wolf2_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                            " he still stands growling at you.\n"))
                elif wolf2_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                            " stands his ground growing at you.\n"))
            else:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Damage_Mod']
                wolf2_stats['hp'] -= damage
                if wolf2_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif wolf2_stats['hp'] >= 4:
                    str(input("You swing your sword grazing across the wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif wolf2_stats['hp'] < 4:
                    str(input("You swing your sword cutting deep into the wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
        else:
            print("You swing your sword but it jumps out of the way.\n")
def Caustic_death():
    attack_roll = attack()
    attack_roll += weapon['LBS_Mod']
    attack_roll += stats['str']['mod']
    if penalty == 1:
        if attack_roll >= caustic_stats['ac']:
            if rage:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Rage_Damage']
                caustic_stats['hp'] -= damage
                if caustic_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif caustic_stats['hp'] >= 16:
                    str(input("You swing your sword grazing across the big wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif caustic_stats['hp'] < 15:
                    str(input("You swing your sword cutting deep into the big wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
            else:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Damage_Mod']
                caustic_stats['hp'] -= damage
                if caustic_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif caustic_stats['hp'] >= 16:
                    str(input("You swing your sword grazing across the big wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif caustic_stats['hp'] < 15:
                    str(input("You swing your sword cutting deep into the big wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
        else:
            print("You swing your sword but it jumps out of the way.\n")
    elif penalty == 2:
        attack_roll -= 5
        if attack_roll >= caustic_stats['ac']:
            if rage:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Rage_Damage']
                caustic_stats['hp'] -= damage
                if caustic_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif caustic_stats['hp'] >= 16:
                    str(input("You swing your sword grazing across the big wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif caustic_stats['hp'] < 15:
                    str(input("You swing your sword cutting deep into the big wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
            else:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Damage_Mod']
                caustic_stats['hp'] -= damage
                if caustic_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif caustic_stats['hp'] >= 16:
                    str(input("You swing your sword grazing across the big wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif caustic_stats['hp'] < 15:
                    str(input("You swing your sword cutting deep into the big wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
        else:
            print("You swing your sword but it jumps out of the way.\n")
    elif penalty == 3:
        attack_roll -= 10
        if attack_roll >= caustic_stats['ac']:
            if rage:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Rage_Damage']
                caustic_stats['hp'] -= damage
                if caustic_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif caustic_stats['hp'] >= 16:
                    str(input("You swing your sword grazing across the big wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif caustic_stats['hp'] < 15:
                    str(input("You swing your sword cutting deep into the big wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
            else:
                damage = 0
                damage += dice.roll(weapon['LBS_Damage'])
                damage += weapon['LBS_Damage_Mod']
                caustic_stats['hp'] -= damage
                if caustic_stats['hp'] <= 0:
                    str(input("You swing your sword with such strength you take its head clean off. Blood spews everywhere "
                              "covering you.\n"))
                elif caustic_stats['hp'] >= 16:
                    str(input("You swing your sword grazing across the big wolf's chest. Blood sprays out of the wound but"
                              " he still stands growling at you.\n"))
                elif caustic_stats['hp'] < 15:
                    str(input("You swing your sword cutting deep into the big wolf, he looks like he is in bad shape but he"
                              " stands his ground growing at you.\n"))
        else:
            print("You swing your sword but it jumps out of the way.\n")

def wolf1_combat():
    attacks = 0
    which_wolves[0] += 1
    if move1[0] == 0:
        while attacks < 3:
                attacks += 1
                attack_roll = attack()
                attack_roll += wolf1_attack['jaws']['val']
                attack_roll += wolf1_attack['jaws']['mod']
                if attacks == 1:
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barley move out of the way in time\n"))
                elif attacks == 2:
                    attack_roll -= 5
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
                elif attacks == 3:
                    attack_roll -= 10
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
        if stats['hp_now'] >= 1:
            wolf2_combat()
        else:
            death()
    elif move1[0] == 1 and wolf2_stats['hp'] <= 0:
        while attacks < 3:
            attacks += 1
            attack_roll = attack()
            attack_roll += wolf1_attack['jaws']['val']
            attack_roll += wolf1_attack['jaws']['mod']
            if attacks == 1:
                str(input("The wolf you tried to ignore runs up besides you and starts to growl and gets ready to lunge at"
                      " you!\n"))
            elif attacks == 2:
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 3:
                attack_roll -= 5
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
        if stats['hp_now'] >= 1:
            combat2_player()
        else:
            death()
    elif move1[0] == 1:
        while attacks < 3:
            attacks += 1
            attack_roll = attack()
            attack_roll += wolf1_attack['jaws']['val']
            attack_roll += wolf1_attack['jaws']['mod']
            if attacks == 1:
                str(input("The wolf you tried to ignore runs up besides you and starts to growl and gets ready to lunge at"
                      " you!\n"))
            elif attacks == 2:
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 3:
                attack_roll -= 5
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
        if stats['hp_now'] >= 1:
            combat2_player()
        else:
            death()
    elif move1[0] == 2:
        while attacks < 3:
                attacks += 1
                attack_roll = attack()
                attack_roll += wolf1_attack['jaws']['val']
                attack_roll += wolf1_attack['jaws']['mod']
                if attacks == 1:
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barley move out of the way in time\n"))
                elif attacks == 2:
                    attack_roll -= 5
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
                elif attacks == 3:
                    attack_roll -= 10
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
        if stats['hp_now'] >= 1:
            move2[0] += 5
            wolf2_combat()
        else:
            death()
    elif move1[0] == 3 or move1[0] == 4 or move1[0] == 5:
        while attacks < 3:
                attacks += 1
                attack_roll = attack()
                attack_roll += wolf1_attack['jaws']['val']
                attack_roll += wolf1_attack['jaws']['mod']
                if attacks == 1:
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barley move out of the way in time\n"))
                elif attacks == 2:
                    attack_roll -= 5
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
                elif attacks == 3:
                    attack_roll -= 10
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
        if stats['hp_now'] >= 1:
            combat2_player()
        else:
            death()
    print("It skipped all of it")
def wolf2_combat():
    attacks = 0
    which_wolves[0] += 2
    if move2[0] == 0:
        while attacks < 3:
                attacks += 1
                attack_roll = attack()
                attack_roll += wolf1_attack['jaws']['val']
                attack_roll += wolf1_attack['jaws']['mod']
                if attacks == 1:
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
                elif attacks == 2:
                    attack_roll -= 5
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
                elif attacks == 3:
                    attack_roll -= 10
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(wolf1_attack['jaws']['damage'])
                        damage += wolf1_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
        if stats['hp_now'] >= 1:
            wolf1_combat()
        else:
            death()
    elif move2[0] == 1 and wolf1_stats['hp'] <= 0:
        while attacks < 3:
            attacks += 1
            attack_roll = attack()
            attack_roll += wolf1_attack['jaws']['val']
            attack_roll += wolf1_attack['jaws']['mod']
            if attacks == 1:
                str(input("The wolf you tried to ignore runs up besides you and starts to growl and gets ready to lunge at"
                    " you!\n"))
            elif attacks == 2:
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 3:
                attack_roll -= 5
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
        if stats['hp_now'] >= 1:
            combat2_player()
        else:
            death()
    elif move2[0] == 1:
        while attacks < 3:
            attacks += 1
            attack_roll = attack()
            attack_roll += wolf1_attack['jaws']['val']
            attack_roll += wolf1_attack['jaws']['mod']
            if attacks == 1:
                str(input("The wolf you tried to ignore runs up besides you and starts to growl and gets ready to lunge at"
                      " you!\n"))
            elif attacks == 2:
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time \n"))
            elif attacks == 3:
                attack_roll -= 5
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
        if stats['hp_now'] >= 1:
            combat2_player()
        else:
            death()
    elif move2[0] == 2:
        while attacks < 3:
            attacks += 1
            attack_roll = attack()
            attack_roll += wolf1_attack['jaws']['val']
            attack_roll += wolf1_attack['jaws']['mod']
            if attacks == 1:
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 2:
                attack_roll -= 5
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 3:
                attack_roll -= 10
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
        if stats['hp_now'] >= 1:
            move1[0] += 5
            wolf1_combat()
        else:
            death()
    elif move2[0] == 3 or move2[0] == 4 or move2[0] == 5:
        while attacks < 3:
            attacks += 1
            attack_roll = attack()
            attack_roll += wolf1_attack['jaws']['val']
            attack_roll += wolf1_attack['jaws']['mod']
            if attacks == 1:
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 2:
                attack_roll -= 5
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 3:
                attack_roll -= 10
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(wolf1_attack['jaws']['damage'])
                    damage += wolf1_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The wolf lunges out and bites your leg dealing {damage} damage"
                                f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The wolf lunges out to bite you but you barely move out of the way in time\n"))
        if stats['hp_now'] >= 1:
            combat2_player()
        else:
            death()
def Caustic_Combat():
    attacks = 0
    which_wolves[0] += 4
    if move3[0] == 0:
        if wolf1_stats['hp'] <= 0:
            while attacks < 3:
                attacks += 1
                attack_roll = attack()
                attack_roll += caustic_attack['jaws']['val']
                attack_roll += caustic_attack['jaws']['mod']
                if attacks == 1:
                    str(input(f"As the head from the wolf in front of you hits the ground. You hear snarl and howl from the trees"
                              f" in front of you. You look up and see wolf double the size of those that you engage.\n"))
                    str(input(f"As it finish it howl it rushes toward you. Growling and snarling ready to attack.\n"))
                elif attacks == 2:
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(caustic_attack['jaws']['damage'])
                        damage += caustic_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The large wolf lunges out and bites your arm dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The large wolf lunges out to bite you but you barely move out of the way in time\n"))
                elif attacks == 3:
                    attack_roll -= 5
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(caustic_attack['jaws']['damage'])
                        damage += caustic_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The large wolf lunges back at you and bites your arm dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The large wolf lunges back at your out to bite you but you barely move out of the way "
                                  f"in time\n"))
            if stats['hp_now'] >= 1:
                wolf2_combat()
            else:
                death()
        elif wolf2_stats['hp'] <= 0:
            while attacks < 3:
                attacks += 1
                attack_roll = attack()
                attack_roll += caustic_attack['jaws']['val']
                attack_roll += caustic_attack['jaws']['mod']
                if attacks == 1:
                    str(input(f"As the head from the wolf in front of you hits the ground. You hear snarl and how from the trees"
                              f"in front of you. You look up and see wolf double the size of those that you engage.\n"))
                    str(input(f"As it finish it howl it rushes toward you. Growling and snarling ready to attack.\n"))
                elif attacks == 2:
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(caustic_attack['jaws']['damage'])
                        damage += caustic_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The large wolf lunges out and bites your arm dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The large wolf lunges out to bite you but you barely move out of the way in time\n"))
                elif attacks == 3:
                    attack_roll -= 5
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(caustic_attack['jaws']['damage'])
                        damage += caustic_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The large wolf lunges back at you and bites your arm dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The large wolf lunges back at your out to bite you but you barely move out of the way "
                                  f"in time\n"))
            if stats['hp_now'] >= 1:
                wolf1_combat()
            else:
                death()
    elif move3[0] == 1:
        while attacks < 3:
            attacks += 1
            attack_roll = attack()
            attack_roll += caustic_attack['jaws']['val']
            attack_roll += caustic_attack['jaws']['mod']
            if attacks == 1:
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(caustic_attack['jaws']['damage'])
                    damage += caustic_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The large wolf lunges out and bites your arm dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The large wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 2:
                attack_roll -= 5
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(caustic_attack['jaws']['damage'])
                    damage += caustic_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The large wolf lunges out and bites your arm dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The large wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 3:
                attack_roll -= 10
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(caustic_attack['jaws']['damage'])
                    damage += caustic_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The large wolf lunges back at you and bites your arm dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The large wolf lunges back at your out to bite you but you barely move out of the way "
                              f"in time\n"))
        if stats['hp_now'] >= 1:
            move2[0] += 3
            wolf2_combat()
        else:
            death()
    elif move3[0] == 2:
        while attacks < 3:
            attacks += 1
            attack_roll = attack()
            attack_roll += caustic_attack['jaws']['val']
            attack_roll += caustic_attack['jaws']['mod']
            if attacks == 1:
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(caustic_attack['jaws']['damage'])
                    damage += caustic_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The large wolf lunges out and bites your arm dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The large wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 2:
                attack_roll -= 5
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(caustic_attack['jaws']['damage'])
                    damage += caustic_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The large wolf lunges out and bites your arm dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The large wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 3:
                attack_roll -= 10
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(caustic_attack['jaws']['damage'])
                    damage += caustic_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The large wolf lunges back at you and bites your arm dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The large wolf lunges back at your out to bite you but you barely move out of the way "
                              f"in time\n"))
        if stats['hp_now'] >= 1:
            move1[0] += 3
            wolf1_combat()
        else:
            death()
    elif move3[0] == 3:
        while attacks < 3:
            attacks += 1
            attack_roll = attack()
            attack_roll += caustic_attack['jaws']['val']
            attack_roll += caustic_attack['jaws']['mod']
            if attacks == 1:
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(caustic_attack['jaws']['damage'])
                    damage += caustic_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The large wolf lunges out and bites your arm dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The large wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 2:
                attack_roll -= 5
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(caustic_attack['jaws']['damage'])
                    damage += caustic_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The large wolf lunges out and bites your arm dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The large wolf lunges out to bite you but you barely move out of the way in time\n"))
            elif attacks == 3:
                attack_roll -= 10
                if attack_roll >= stats['ac']:
                    damage = 0
                    damage += dice.roll(caustic_attack['jaws']['damage'])
                    damage += caustic_attack['jaws']['d_mod']
                    stats['hp_now'] -= damage
                    str(input(f"The large wolf lunges back at you and bites your arm dealing {damage} damage"
                              f" but you shake it off. You have {stats['hp_now']} health left\n"))
                else:
                    str(input(f"The large wolf lunges back at your out to bite you but you barely move out of the way "
                              f"in time\n"))
        if stats['hp_now'] >= 1:
            combat2_player()
        else:
            death()
    elif move3[0] == 4:
        if wolf1_stats['hp'] <= 0:
            while attacks < 3:
                attacks += 1
                attack_roll = attack()
                attack_roll += caustic_attack['jaws']['val']
                attack_roll += caustic_attack['jaws']['mod']
                if attacks == 1:
                    str(input(f"The wolf in the trees howls, then charges toward you. As soon as it reaches you it "
                              f"attacks\n"))
                elif attacks == 2:
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(caustic_attack['jaws']['damage'])
                        damage += caustic_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The large wolf lunges out and bites your arm dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The large wolf lunges out to bite you but you barely move out of the way in time\n"))
                elif attacks == 3:
                    attack_roll -= 5
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(caustic_attack['jaws']['damage'])
                        damage += caustic_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The large wolf lunges back at you and bites your arm dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(f"The large wolf lunges back at your out to bite you but you barely move out of the way "
                                  f"in time\n"))
            if stats['hp_now'] >= 1:
                move2[0] += 3
                wolf2_combat()
            else:
                death()
    elif move3[0] == 5:
        if wolf1_stats['hp'] <= 0:
            while attacks < 3:
                attacks += 1
                attack_roll = attack()
                attack_roll += caustic_attack['jaws']['val']
                attack_roll += caustic_attack['jaws']['mod']
                if attacks == 1:
                    str(input(f"The wolf in the trees howls, then charges toward you. As soon as it reaches you it "
                              f"attacks\n"))
                elif attacks == 2:
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(caustic_attack['jaws']['damage'])
                        damage += caustic_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The large wolf lunges out and bites your arm dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(
                            f"The large wolf lunges out to bite you but you barely move out of the way in time\n"))
                elif attacks == 3:
                    attack_roll -= 5
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(caustic_attack['jaws']['damage'])
                        damage += caustic_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The large wolf lunges back at you and bites your arm dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(
                            f"The large wolf lunges back at your out to bite you but you barely move out of the way "
                            f"in time\n"))
            if stats['hp_now'] >= 1:
                move1[0] += 3
                wolf1_combat()
            else:
                death()
    elif move3[0] == 6:
        if wolf1_stats['hp'] <= 0:
            while attacks < 3:
                attacks += 1
                attack_roll = attack()
                attack_roll += caustic_attack['jaws']['val']
                attack_roll += caustic_attack['jaws']['mod']
                if attacks == 1:
                    str(input(f"The wolf in the trees howls, then charges toward you. As soon as it reaches you it "
                              f"attacks\n"))
                elif attacks == 2:
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(caustic_attack['jaws']['damage'])
                        damage += caustic_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The large wolf lunges out and bites your arm dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(
                            f"The large wolf lunges out to bite you but you barely move out of the way in time\n"))
                elif attacks == 3:
                    attack_roll -= 5
                    if attack_roll >= stats['ac']:
                        damage = 0
                        damage += dice.roll(caustic_attack['jaws']['damage'])
                        damage += caustic_attack['jaws']['d_mod']
                        stats['hp_now'] -= damage
                        str(input(f"The large wolf lunges back at you and bites your arm dealing {damage} damage"
                                  f" but you shake it off. You have {stats['hp_now']} health left\n"))
                    else:
                        str(input(
                            f"The large wolf lunges back at your out to bite you but you barely move out of the way "
                            f"in time\n"))
            if stats['hp_now'] >=1:
                combat2_player()
            else:
                death()
def combat2_player():
    str(input(f"Your current health is {stats['hp_now']}. You can spend up to 2 action this turn to drink from an "
              f"Elixir of life to get back up to 6 health"))
    action_list = ["1.Attack the wolf in front of you.", "2.Attack the wolf that charged up.", "3.Attack the big wolf",
                   "4. Drink from the Elixir", "5.Rage"]
    global rage
    global penalty
    actions = 0
    hidden = 0
    move1[0] = 0
    move2[0] = 0
    move3[0] = 0
    penalty = 0
    print("You get another 3 actions this turn. choose wisely")
    if which_wolves[0] == 3:
        which_wolves[0] -= 3
        if rage:
            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "1":
                    hidden += 1
                    actions += 1
                    penalty += 1
                    if hidden == 1:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 2:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 3:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 6:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                  " slain approaching.\n"))
                            print(f"{action_list[3]}")
                        elif wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        elif wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 7:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 11:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 13:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 14:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 18:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 25:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                elif choice == "2":
                    hidden += 5
                    actions += 1
                    penalty += 1
                    if hidden == 5:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 10:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 15:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 6:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                        " slain approaching.\n"))
                            print(f"{action_list[3]}")
                        elif wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        elif wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 7:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 11:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      "slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 17:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 18:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 22:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 29:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                elif choice == "4":
                    hidden += 12
                    actions += 1
                    if hidden == 12:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 24:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[1]}")
                    elif hidden == 13:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 14:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 25:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move1[0] += 2
                        wolf1_combat()
                    elif hidden == 17:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 22:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 29:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 18:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                else:
                    print("That is not a valid choice")
        elif not rage:
            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "1":
                    hidden += 1
                    actions += 1
                    penalty += 1
                    if hidden == 1:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 2:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 3:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 6:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            print(f"{action_list[3]}")
                        elif wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        elif wolf2_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 7:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 11:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 13:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 14:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 18:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 25:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 27:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 28:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 32:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 39:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                elif choice == "2":
                    hidden += 5
                    actions += 1
                    penalty += 1
                    if hidden == 5:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 10:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 15:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 6:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            print(f"{action_list[3]}")
                        elif wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
                        elif wolf1_stats['hp'] <=0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 7:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 11:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 17:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 18:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 22:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 29:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 31:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 32:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 37:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 43:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                elif choice == "4":
                    hidden += 12
                    actions += 1
                    if hidden == 12:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 24:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[1]}\n{action_list[4]}")
                    elif hidden == 13:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 14:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 25:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move1[0] += 2
                        wolf1_combat()
                    elif hidden == 17:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 22:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 29:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move2[0] += 2
                            wolf2_combat()
                    elif hidden == 18:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 38:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 50:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move1[0] += 2
                        wolf1_combat()
                    elif hidden == 39:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 43:
                        if wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                elif choice == "5":
                    hidden += 26
                    actions += 1
                    rage = True
                    if hidden == 26:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 27:
                        print("A red mist surrounds you as you give into your rage\n")
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 31:
                        print("A red mist surrounds you as you give into your rage\n")
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 38:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[0]}\n{action_list[1]}\n{action_list[3]}")
                    elif hidden == 32:
                        print("A red mist surrounds you as you give into your rage\n")
                        if wolf1_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 6
                            Caustic_Combat()
                        elif wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        elif wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 39:
                        print("A red mist surrounds you as you give into your rage\n")
                        if wolf1_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 4
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                    elif hidden == 43:
                        print("A red mist surrounds you as you give into your rage\n")
                        if wolf2_stats['hp'] <= 0:
                            str(input("On the edge of the forest you see a wolf double the size that you just"
                                      " slain approaching.\n"))
                            move3[0] += 5
                            Caustic_Combat()
                        else:
                            move1[0] += 2
                            wolf1_combat()
                else:
                    print("That is not a valid choice")
    elif which_wolves[0] == 5:
        which_wolves[0] -= 5
        move3[0] += 2
        move1[0] += 1
        if not rage:
            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "1":
                    hidden += 1
                    actions += 1
                    penalty += 1
                    if hidden == 1:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 2:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 3:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 6:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        elif caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 7:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 11:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 13:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 14:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 18:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 25:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 27:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 28:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 32:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 39:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                elif choice == "3":
                    hidden += 5
                    actions += 1
                    penalty += 1
                    if hidden == 5:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 10:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 15:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 6:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
                        elif wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 7:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 11:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 17:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 18:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 22:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 29:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 31:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 32:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 37:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 43:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                elif choice == "4":
                    hidden += 12
                    actions += 1
                    if hidden == 12:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 24:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[2]}\n{action_list[4]}")
                    elif hidden == 13:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 14:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 25:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 17:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 22:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 29:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 18:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 38:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 50:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move3[0] += 0
                        Caustic_Combat()
                    elif hidden == 39:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 43:
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                elif choice == "5":
                    hidden += 26
                    actions += 1
                    rage = True
                    if hidden == 26:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 27:
                        print("A red mist surrounds you as you give into your rage\n")
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 31:
                        print("A red mist surrounds you as you give into your rage\n")
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 38:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 32:
                        print("A red mist surrounds you as you give into your rage\n")
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 39:
                        print("A red mist surrounds you as you give into your rage\n")
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 43:
                        print("A red mist surrounds you as you give into your rage\n")
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                else:
                    print("That is not a valid choice")
        if rage:
            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "1":
                    hidden += 1
                    actions += 1
                    penalty += 1
                    if hidden == 1:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 2:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 3:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 6:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        elif caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 7:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 11:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 13:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 14:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 18:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 25:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 27:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 28:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 32:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 39:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                elif choice == "3":
                    penalty += 1
                    hidden += 5
                    actions += 1
                    if hidden == 5:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 10:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 15:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 6:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        elif wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 7:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 11:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 17:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 18:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 22:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 29:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 31:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 32:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf1_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 37:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 43:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                elif choice == "4":
                    hidden += 12
                    actions += 1
                    if hidden == 12:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 24:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[2]}")
                    elif hidden == 13:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 14:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 25:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 17:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[0]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 22:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 29:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 18:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 38:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 50:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move3[0] += 0
                        Caustic_Combat()
                    elif hidden == 39:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf1_stats['hp'] <= 0:
                            move3[0] += 1
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 43:
                        if caustic_stats['hp'] <= 0:
                            move1[0] += 3
                            wolf1_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                else:
                    print("That is not a valid choice")
    elif which_wolves[0] == 6:
        which_wolves[0] -= 6
        move2[0] += 1
        move3[0] += 1
        if not rage:
            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "2":
                    penalty += 1
                    hidden += 1
                    actions += 1
                    if hidden == 1:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 2:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 3:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 6:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        elif caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 7:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 11:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 13:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 14:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 18:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 25:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 27:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 28:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 32:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 39:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                elif choice == "3":
                    penalty += 1
                    hidden += 5
                    actions += 1
                    if hidden == 5:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 10:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 15:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 6:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        elif wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 7:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 4
                            wolf2_combat()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 11:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 17:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 18:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 22:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 29:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 31:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 32:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 37:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 43:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                elif choice == "4":
                    hidden += 12
                    actions += 1
                    if hidden == 12:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 24:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}\n{action_list[2]}\n{action_list[4]}")
                    elif hidden == 13:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 14:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 25:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 17:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
                    elif hidden == 22:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 29:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 18:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 38:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 50:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move3[0] += 0
                        Caustic_Combat()
                    elif hidden == 39:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 43:
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                elif choice == "5":
                    hidden += 26
                    actions += 1
                    rage = True
                    if hidden == 26:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 27:
                        print("A red mist surrounds you as you give into your rage\n")
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 31:
                        print("A red mist surrounds you as you give into your rage\n")
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 38:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 32:
                        print("A red mist surrounds you as you give into your rage\n")
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 39:
                        print("A red mist surrounds you as you give into your rage\n")
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 43:
                        print("A red mist surrounds you as you give into your rage\n")
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                else:
                    print('That is not a valid choice')
        elif rage:
            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "2":
                    penalty += 1
                    hidden += 1
                    actions += 1
                    if hidden == 1:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 2:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 3:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 6:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        elif caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 7:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 11:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 13:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 14:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 18:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 25:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 27:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 28:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 32:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 39:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                elif choice == "3":
                    penalty += 1
                    hidden += 5
                    actions += 1
                    if hidden == 5:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 10:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 15:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 6:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        elif wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 7:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 11:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 17:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 18:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 22:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 29:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 31:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 32:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0 and wolf2_stats['hp'] <= 0:
                            win()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 37:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 43:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                elif choice == "4":
                    hidden += 12
                    actions += 1
                    if hidden == 12:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 24:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}\n{action_list[2]}")
                    elif hidden == 13:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            print(f"{action_list[2]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 14:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 25:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 17:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            print(f"{action_list[1]}\n{action_list[3]}")
                        else:
                            print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 22:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 29:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 18:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0 and caustic_stats['hp'] <= 0:
                            win()
                        elif wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        elif caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 38:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}\n{action_list[2]}\n{action_list[3]}")
                    elif hidden == 50:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move3[0] += 0
                        Caustic_Combat()
                    elif hidden == 39:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        if wolf2_stats['hp'] <= 0:
                            move3[0] += 2
                            Caustic_Combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                    elif hidden == 43:
                        if caustic_stats['hp'] <= 0:
                            move2[0] += 3
                            wolf2_combat()
                        else:
                            move3[0] += 0
                            Caustic_Combat()
                else:
                    print("That is not a valid choice")
    elif which_wolves[0] == 1:
        which_wolves[0] -= 1
        if rage:
            print(f"{action_list[0]}\n{action_list[3]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "1":
                    penalty += 1
                    hidden += 1
                    actions += 1
                    if hidden == 1:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 2:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 3:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            move1[0] += 4
                            wolf1_combat()
                    elif hidden == 6:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 7:
                        wolf1_death()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            move1[0] += 4
                            wolf1_combat()
                    elif hidden == 11:
                        wolf1_death()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            move1[0] += 4
                            wolf1_combat()
                elif choice == "4":
                    if hidden == 5:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 10:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}")
                    elif hidden == 6:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 7:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move1[0] += 4
                        wolf1_combat()
        elif not rage:
            print(f"{action_list[0]}\n{action_list[3]}\n{action_list[4]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "1":
                    penalty += 1
                    hidden += 1
                    actions += 1
                    if hidden == 1:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 2:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 3:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            move1[0] += 4
                            wolf1_combat()
                    elif hidden == 6:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 7:
                        wolf1_death()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            move1[0] += 4
                            wolf1_combat()
                    elif hidden == 11:
                        wolf1_death()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            move1[0] += 4
                            wolf1_combat()
                    elif hidden == 13:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 14:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            move1[0] += 4
                            wolf1_combat()
                    elif hidden == 18:
                        wolf1_death2()
                        if wolf1_stats['hp'] <= 0:
                            win()
                        else:
                            move1[0] += 4
                            wolf1_combat()
                elif choice == "4":
                    if hidden == 5:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[3]}{action_list[4]}")
                    elif hidden == 10:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}{action_list[4]}")
                    elif hidden == 6:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[3]}{action_list[4]}")
                    elif hidden == 7:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move1[0] += 4
                        wolf1_combat()
                    elif hidden == 17:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 18:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move1[0] += 4
                        wolf1_combat()
                elif choice == "5":
                    if hidden == 12:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 13:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 14:
                        print("A red mist surrounds you as you give into your rage\n")
                        move1[0] += 4
                        wolf1_combat()
                    elif hidden == 17:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[0]}\n{action_list[3]}")
                    elif hidden == 18:
                        print("A red mist surrounds you as you give into your rage\n")
                        move1[0] += 4
                        wolf1_combat()
                    elif hidden == 22:
                        print("A red mist surrounds you as you give into your rage\n")
                        move1[0] += 4
                        wolf1_combat()
    elif which_wolves[0] == 2:
        which_wolves[0] -= 2
        if rage:
            print(f"{action_list[1]}\n{action_list[3]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "2":
                    penalty += 1
                    hidden += 1
                    actions += 1
                    if hidden == 1:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 2:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 3:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            move2[0] += 4
                            wolf2_combat()
                    elif hidden == 6:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 7:
                        wolf2_death()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            move2[0] += 4
                            wolf2_combat()
                    elif hidden == 11:
                        wolf2_death()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            move2[0] += 4
                            wolf2_combat()
                elif choice == "4":
                    if hidden == 5:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 10:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}")
                    elif hidden == 6:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 7:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move2[0] += 4
                        wolf2_combat()
        elif not rage:
            print(f"{action_list[1]}\n{action_list[3]}\n{action_list[4]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "2":
                    penalty += 1
                    hidden += 1
                    actions += 1
                    if hidden == 1:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 2:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 3:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            move2[0] += 4
                            wolf2_combat()
                    elif hidden == 6:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 7:
                        wolf2_death()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            move2[0] += 4
                            wolf2_combat()
                    elif hidden == 11:
                        wolf2_death()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            move2[0] += 4
                            wolf2_combat()
                    elif hidden == 13:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 14:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            move2[0] += 4
                            wolf2_combat()
                    elif hidden == 18:
                        wolf2_death2()
                        if wolf2_stats['hp'] <= 0:
                            win()
                        else:
                            move2[0] += 4
                            wolf2_combat()
                elif choice == "4":
                    if hidden == 5:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}\n{action_list[3]}{action_list[4]}")
                    elif hidden == 10:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}{action_list[4]}")
                    elif hidden == 6:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}\n{action_list[3]}{action_list[4]}")
                    elif hidden == 7:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move2[0] += 4
                        wolf2_combat()
                    elif hidden == 17:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 18:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move2[0] += 4
                        wolf2_combat()
                elif choice == "5":
                    if hidden == 12:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 13:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 14:
                        print("A red mist surrounds you as you give into your rage\n")
                        move2[0] += 4
                        wolf2_combat()
                    elif hidden == 17:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[1]}\n{action_list[3]}")
                    elif hidden == 18:
                        print("A red mist surrounds you as you give into your rage\n")
                        move2[0] += 4
                        wolf2_combat()
                    elif hidden == 22:
                        print("A red mist surrounds you as you give into your rage\n")
                        move2[0] += 4
                        wolf2_combat()
    elif which_wolves[0] == 4:
        which_wolves[0] -= 4
        if rage:
            print(f"{action_list[2]}\n{action_list[3]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "3":
                    penalty += 1
                    hidden += 1
                    actions += 1
                    if hidden == 1:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 2:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 3:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            move3[0] += 3
                            Caustic_Combat()
                    elif hidden == 6:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 7:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            move3[0] += 3
                            Caustic_Combat()
                    elif hidden == 11:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            move3[0] += 3
                            Caustic_Combat()
                elif choice == "4":
                    if hidden == 5:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 10:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[2]}")
                    elif hidden == 6:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 7:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move3[0] += 3
                        Caustic_Combat()
        elif not rage:
            print(f"{action_list[2]}\n{action_list[3]}\n{action_list[4]}")
            while actions < 3:
                choice = str(input(f"Please enter your choice:"))
                if choice == "3":
                    penalty += 1
                    hidden += 1
                    actions += 1
                    if hidden == 1:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 2:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 3:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            move3[0] += 3
                            Caustic_Combat()
                    elif hidden == 6:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 7:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            move3[0] += 3
                            Caustic_Combat()
                    elif hidden == 11:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            move3[0] += 3
                            Caustic_Combat()
                    elif hidden == 13:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 14:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            move3[0] += 3
                            Caustic_Combat()
                    elif hidden == 18:
                        Caustic_death()
                        if caustic_stats['hp'] <= 0:
                            win()
                        else:
                            move3[0] += 3
                            Caustic_Combat()
                elif choice == "4":
                    if hidden == 5:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[2]}\n{action_list[3]}{action_list[4]}")
                    elif hidden == 10:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[2]}{action_list[4]}")
                    elif hidden == 6:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[2]}\n{action_list[3]}{action_list[4]}")
                    elif hidden == 7:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move3[0] += 3
                        Caustic_Combat()
                    elif hidden == 17:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 18:
                        potion = dice.roll('1d6t')
                        stats['hp_now'] += potion
                        str(input(f"You restore {potion} health. Your health is now at {stats['hp_now']}"))
                        move3[0] += 3
                        Caustic_Combat()
                elif choice == "5":
                    if hidden == 12:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 13:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 14:
                        print("A red mist surrounds you as you give into your rage\n")
                        move3[0] += 3
                        Caustic_Combat()
                    elif hidden == 17:
                        print("A red mist surrounds you as you give into your rage\n")
                        print(f"{action_list[2]}\n{action_list[3]}")
                    elif hidden == 18:
                        print("A red mist surrounds you as you give into your rage\n")
                        move3[0] += 3
                        Caustic_Combat()
                    elif hidden == 22:
                        print("A red mist surrounds you as you give into your rage\n")
                        move3[0] += 3
                        Caustic_Combat()


def win():
    print("You killed all the wolves in the area!  You win the game congrats!")
    exit()
def death():
    print("You have fallen in combat. The wolves feast on your body.")
    exit()



Amiri()
wolf1()
wolf2()
which_wolves = [0]
Caustic_Wolf()
story_intro()