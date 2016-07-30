import random
import game


class Monster(object):
    def __init__(self, name, level, health, attack, defense, mtype, abilities, item):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        self.mtype = mtype
        self.abilities = abilities
        self.item = item
        self.experience_award = 100

    def capture_monster(self):
        pass

# If the random int is
def random_encounter():
    if random.randint(0, 100) > 80:
        game.player_status = "battle"


sample_monster = Monster("test 1", 1, 10, 1, 1, "normal", {'scratch': 1}, [])
sample_monster2 = Monster("test 2", 99, 999, 99, 99, "normal", {'scratch': 1}, [])


class Encounter():
    pass


def combat():
    while game.player_status == "battle":
        pass