# Define two classes.
# 1. Colors -- provide the ability to use colors inside Terminal.
# 2. Person -- to be used to build player characters.

import random
from classes.magic import Spell
import pprint


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic,items):
        self.name = name
        self.max_hp = hp                # Max Heal points
        self.hp = hp                    # Heal points
        self.max_mp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def chooseAction(self):
        i = 1
        print("\n" + Bcolors.BOLD + self.name + Bcolors.ENDC)
        print(Bcolors.OKBLUE + Bcolors.BOLD + "    ACTIONS" + Bcolors.ENDC)
        for action in self.actions:
            print("        " + str(i) + ".", action)
            i = i + 1

    def chooseMagic(self):
        i = 1
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "    Magic" + Bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(Cost:", str(spell.cost) + ")")
            i = i + 1

    def chooseItem(self):
        i = 1
        print("\n" + "    " + Bcolors.OKGREEN + Bcolors.BOLD + "    Items" + Bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name + ":", item["item"].description, " (x " + str(item["quantity"]) + ")")
            i = i + 1

    def chooseTarget(self, enemies):
        i = 1
        print("\n" + Bcolors.FAIL + Bcolors.BOLD + "    TARGET" + Bcolors.ENDC)
        for enemy in enemies:
            if enemy.getHp() != 0:
                print("        " + str(i) + "." + enemy.name)
                i = i + 1
        choice = int(input("    Choose Target: ")) - 1
        return choice

    def getHp(self):
        return self.hp

    def getMaxHp(self):
        return self.max_hp

    def getMp(self):
        return self.mp

    def getMaxMp(self):
        return self.max_mp

    def heal(self, dmg):
        self.hp = self.hp + dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def genAtkDamage(self):
        return random.randrange(self.atkl, self.atkh)

    def takeDamage(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def reduceMp(self, cost):
        self.mp = self.mp - cost

    def getStats(self):
        hp_bar = ""
        hp_bar_ticks = ((self.hp / self.max_hp) * 100) / 4

        mp_bar = ""
        mp_bar_ticks = ((self.mp / self.max_mp) * 100) / 10

        while hp_bar_ticks > 0:
            hp_bar = hp_bar + "█"
            hp_bar_ticks = hp_bar_ticks - 1

        while len(hp_bar) < 25:
            hp_bar = hp_bar + " "

        while mp_bar_ticks > 0:
            mp_bar = mp_bar + "█"
            mp_bar_ticks = mp_bar_ticks - 1

        while len(mp_bar) < 10:
            mp_bar = mp_bar + " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp = current_hp + " "
                decreased = decreased - 1

            current_hp = current_hp + hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp = current_mp + " "
                decreased = decreased - 1

            current_mp = current_mp + mp_string
        else:
            current_mp = mp_string

        print("                       _________________________                __________ ")
        print(Bcolors.BOLD + self.name + "      " +
              current_hp + " |" + Bcolors.OKGREEN + hp_bar + Bcolors.ENDC + Bcolors.BOLD + "|      " +
              current_mp + " |" + Bcolors.OKBLUE + mp_bar + Bcolors.ENDC + "|")

    def getEnemyStats(self):
        hp_bar = ""
        hp_bar_ticks = ((self.hp / self.max_hp) * 100) / 2

        while hp_bar_ticks > 0:
            hp_bar = hp_bar + "█"
            hp_bar_ticks = hp_bar_ticks - 1

        while len(hp_bar) < 50:
            hp_bar = hp_bar + " "

        mp_bar = ""
        mp_bar_ticks = ((self.mp / self.max_mp) * 100) / 10

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp = current_hp + " "
                decreased = decreased - 1

            current_hp = current_hp + hp_string
        else:
            current_hp = hp_string

        print("                       __________________________________________________ ")
        print(Bcolors.BOLD + self.name + "    " +
              current_hp + " |" + Bcolors.FAIL + hp_bar + Bcolors.ENDC + Bcolors.BOLD + "|")

    def chooseEnemySpell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.genSpellDamage()
        pct_hp = self.hp / self.max_hp * 100

        if self.mp < spell.cost or spell.type == "white" and pct_hp > 50:
            self.chooseEnemySpell()
            return spell, magic_dmg
        else:
            return spell, magic_dmg
