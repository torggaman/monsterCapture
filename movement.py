import map
import monsters

wrongw = "Cannot go that way"

m = map.map

playerx = 0
playery = 0


def move_player(direction, y, x):
    global playerx
    global playery
    if check_wall(direction, y, x):
        print(wrongw)
    else:
        if direction == "up":
            if y < 1:
                print(wrongw)
            else:
                m[y][x] = 'x'
                m[(y - 1)][x] = 'P'
                playerx = x
                playery = (y - 1)
        elif direction == "down":
            if (y + 1) > len(m):
                print(wrongw)
            else:
                m[y][x] = 'x'
                m[(y + 1)][x] = 'P'
                playerx = x
                playery = (y + 1)
        elif direction == "left":
            if x < 1:
                print(wrongw)
            else:
                m[y][x] = 'x'
                m[y][(x - 1)] = 'P'
                playerx = (x - 1)
                playery = y
        elif direction == "right":
            if (x + 1) > len(m[y]):
                print(wrongw)
            else:
                m[y][x] = 'x'
                m[y][(x + 1)] = 'P'
                playerx = (x + 1)
                playery = y


def check_wall(direction, y, x):
    global m
    if direction == "down":
        if y < (len(m) - 1):
            if m[(y + 1)][x] == "W":
                return True
            else:
                return False
        else:
            return True
    elif direction == "up":
        if m[(y - 1)][x] == "W":
            return True
        else:
            return False
    elif direction == "right":
        if x < (len(m[y]) - 1):
            if m[y][(x + 1)] == "W":
                return True
            else:
                return False
        else:
            return True
    elif direction == "left":
        if m[y][(x - 1)] == "W":
            return True
        else:
            return False


def check_event():
    monsters.random_encounter()
