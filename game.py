import map
import monsters
import player
import ui
import movement

newgame = True
start = True
p = player.Player()
m = monsters
move = movement
u = ui
player_status = ""


if newgame:
    print("Welcome to the world")
    p.name = input("What is your name? ")
    print("Are you ready %s? " % p.name)
    newgame = False
    map.create_world(10, 10, "")
    map.show_map()
    print(len(map.map))
    print(len(map.map[0]))
    # player.Backpack.add_monster(m.sample_monster2.name, m.sample_monster2.level,
    #                            m.sample_monster2.attack,
    #                            m.sample_monster2.defense,
    #                            m.sample_monster2.mtype,
    #                            m.sample_monster2.abilities,
    #                            m.sample_monster2.item)
    # print("You have gained the starter %s" % m.sample_monster2.name)
    # print(p.currentMonster)
    while start:
        moving = input("What would you like to do? ")
        if moving == "done":
            start = False
        elif moving == "event":
            map.create_event()
        else:
            movement.move_player(moving,
                                 move.playery,
                                 move.playerx)
            map.check_events()
            if player_status == "battleing":
                pass
