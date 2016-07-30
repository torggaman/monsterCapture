class Player(object):
    def __init__(self):
        self.name = ""
        self.backpackSizelimit = 1
        self.currentMonster = {}


class SaveGame:
    def __init__(self):
        pass


class Shop:
    def __init__(self):
        pass


class Backpack(object):
    def __init__(self):
        self.backpackSize = self.currentMonster.length

    def add_monster(self, addname, addlevel, addhealth, addattack, adddefense, addtype, addabilities, additem):
        Player.currentMonster[addname] = {'name': addname,
                             'level': addlevel,
                             'health': addhealth, 'attack': addattack, 'defense': adddefense,
                             'mtype': addtype, 'abilities': addabilities,
                             'item': additem, 'experience': 0}
    def check_monster(self):
        print(Player.currentMonster)

###
# Inventory:
#
#
# Backpack:
#
#
# Computer:
#   store monster
#
# Menu:
#   Monsters currently equipped
#   Inventory
#   List of monster seen
#   Save
#   Key Items/ objective
# Combat:
#   Monsters fight
#
# Capture:
#
#
# Gym
#
#
# Time passing:
###
