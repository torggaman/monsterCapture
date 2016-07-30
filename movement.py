import map
import monsters

m = map.map

playerx = 0
playery = 0


def move_player(direction, y, x):
    global playerx
    global playery
    if direction == "up":
        if y < 1:
            print("Can not go that way")
        else:
            m[y][x] = 'x'
            m[(y - 1)][x] = 'P'
            playerx = x
            playery = (y - 1)
    elif direction == "down":
        m[y][x] = 'x'
        m[(y + 1)][x] = 'P'
        playerx = x
        playery = (y + 1)
    elif direction == "left":
        if x < 1:
            print("Can not go that way")
        else:
            m[y][x] = 'x'
            m[y][(x - 1)] = 'P'
            playerx = (x - 1)
            playery = y
    elif direction == "right":
        m[y][x] = 'x'
        m[y][(x + 1)] = 'P'
        playerx = (x + 1)
        playery = y
    map.show_map()


def check_event():
    monsters.random_encounter()

