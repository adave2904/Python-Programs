########################################################################################################################
############################################           RPG BATTLE         ##############################################
#                       A python implementation of a text based / terminal battle game
########################################################################################################################

# Import relevant packages and classes.
from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


# Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")


# Create White Magic
cure = Spell("Cure", 25, 600, "white")
cura = Spell("Cura", 35, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")

# Select the magic for the players and the enemies.
player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, curaga]

# Create some Items.
potion = Item("Potion", "Potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "Potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "Potion", "Heals 1000 HP", 500)
elixir = Item("Elixir", "Elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item("Mega Elixir", "Elixir", "Fully restores party's HP/MP", 9999)
grenade = Item("Grenade", "Attack", "Deals 500 damage", 500)

# Select the items for a player.
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixir, "quantity": 5},
                {"item": hielixir, "quantity": 2},
                {"item": grenade, "quantity": 5}]

# Instantiate a set of players.
player1 = Person("Valos:", 3260, 130, 300, 34, player_spells, player_items)
player2 = Person("Talos:", 4160, 190, 320, 34, player_spells, player_items)
player3 = Person("Ramos:", 3090, 170, 290, 34, player_spells, player_items)

# Create a list of players.
players = [player1, player2, player3]

# Instantiate a set of enemies.
enemy1 = Person("Imp1  ", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Robot ", 18200, 1000, 525, 25, enemy_spells, [])
enemy3 = Person("Imp2  ", 1250, 130, 560, 325, enemy_spells, [])

# Create a list of enemies.
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)
while running:
    print("======================")
    print("\n\n")

    print("NAME                  HP                                      MP")

    for player in players:
        player.getStats()

    print("\n")

    for enemy in enemies:
        enemy.getEnemyStats()

    for player in players:

        # Choose Action -- Attack or Magic
        player.chooseAction()
        choice = input("    Choose Action: ")
        index = int(choice) - 1

        # If Attack is the chosen action.
        if index == 0:
            atk_dmg = player.genAtkDamage()

            enemy = player.chooseTarget(enemies)
            enemies[enemy].takeDamage(atk_dmg)

            print("Player Attacked " + enemies[enemy].name.strip() + " for", atk_dmg, "damage points.")

            if enemies[enemy].getHp() == 0:
                print("\n" + Bcolors.BOLD + enemies[enemy].name.strip() + " has died!!!" + Bcolors.ENDC)
                del enemies[enemy]

        # If Magic is the chosen action.
        elif index == 1:
            player.chooseMagic()
            magic_choice = int(input("Choose Magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.genSpellDamage()

            current_mp = player.getMp()
            if spell.cost > current_mp:
                print(Bcolors.FAIL + "\nNot Enough MP\n" + Bcolors.ENDC)
                continue

            player.reduceMp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + "heals for", str(magic_dmg), "HP" + Bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.chooseTarget(enemies)
                enemies[enemy].takeDamage(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points damage to " + enemies[enemy].name.strip() + Bcolors.ENDC)

                if enemies[enemy].getHp() == 0:
                    print("\n" + Bcolors.BOLD + enemies[enemy].name.strip() + " has died!!!" + Bcolors.ENDC)
                    del enemies[enemy]

        # If Items is the chosen action.
        elif index == 2:
            player.chooseItem()
            item_choice = int(input("Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(Bcolors.FAIL + "\n" + "None left... " + Bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] = player.items[item_choice]["quantity"] - 1

            if item.type == "Potion":
                player.heal(item.prop)
                print(Bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + Bcolors.ENDC)
            elif item.type == "Elixir":
                if item.name == "Mega Elixir":
                    for i in players:
                        i.hp = i.max_hp
                        i.mp = i.max_mp
                else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp

                print(Bcolors.OKGREEN + "\n" + item.name + " fully restores HP and MP." + Bcolors.ENDC)
            elif item.type == "Attack":
                enemy = player.chooseTarget(enemies)
                enemies[enemy].takeDamage(item.prop)
                print(Bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "point damage to " + enemies[enemy].name.strip() + Bcolors.ENDC)

                if enemies[enemy].getHp() == 0:
                    print("\n" + Bcolors.BOLD + enemies[enemy].name.strip() + " has died!!!" + Bcolors.ENDC)
                    del enemies[enemy]

        # Check if all enemies have been defeated.
        # If yes, declare the players as winners and stop the game.
        defeated_enemies = 0
        for enemy in enemies:
            if enemy.getHp() == 0:
                defeated_enemies = defeated_enemies + 1

        if defeated_enemies == 2:
            print(Bcolors.OKGREEN + "Team Players Wins" + Bcolors.ENDC)
            running = False

        # Check if all players have been defeated.
        # If yes, declare the enemies as winners and stop the game.
        defeated_players = 0
        for player in players:
            if player.getHp() == 0:
                defeated_players = defeated_players + 1

        if defeated_players == 2:
            print(Bcolors.FAIL + "Team Enemy Wins. You Lose." + Bcolors.ENDC)
            running = False

    print("\n")

# Enemy attacks.
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # Choose the player that will be attacked.
            target = random.randrange(0, 3)
            enemy_atk_dmg = enemies[0].genAtkDamage()
            players[target].takeDamage(enemy_atk_dmg)

            print(enemy.name.strip() + " attacks " + players[target].name.strip() + " for", enemy_atk_dmg, "points.")

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.chooseEnemySpell()
            enemy.reduceMp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(Bcolors.OKBLUE + spell.name + " heals " + enemy.name +
                      " for", str(magic_dmg), "HP" + Bcolors.ENDC)
            elif spell.type == "black":
                # Choose the player that will be attacked.
                target = random.randrange(0, 3)
                # Attack the player.
                players[target].takeDamage(magic_dmg)

                print(Bcolors.OKBLUE + enemy.name.strip() + "'s " + spell.name +
                      " deals", str(magic_dmg), "points damage to " + players[target].name.strip() + Bcolors.ENDC)

                if players[target].getHp() == 0:
                    print("\n" + Bcolors.BOLD + players[target].name.strip() + " has died!!!" + Bcolors.ENDC)
                    del players[pl]

            print("Enemy chose", spell.name, "and the damage is", magic_dmg, "points.")