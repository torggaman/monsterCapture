map = []


def create_world(x, y):
    for a in range(0, y):
        map.append([])
        for b in range(0, x):
            map[a].append('x')
    map[0][0] = "P"


def show_map():
    for row in map:
        print(" ".join(row))


class Event(object):
    def __init__(self, name, xcoord, ycoord, r_event):
        self.e_type = name
        self.x_coord = xcoord
        self.y_coord = ycoord
        self.event = r_event

starter = Event("Start", 0, 0, "")

# class WorldMap:
#    def __init__(self):
#        for a in range(10):
#             for b in range(10):
#                 map.append([(a + 1), (b + 1)])
#    pass
