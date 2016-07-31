map = []


def create_world(x, y, option):
    for a in range(0, y):
        map.append([])
        for b in range(0, x):
            if option == "":
                map[a].append('x')
            elif option == "Wall":
                map[a].append('W')
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

events = {}


def create_event():
    e_name = input("Event name? ")
    e_x = int(input("Event X coord? "))
    while e_x > (len(map[0]) - 1):
        print("Please try a different number within: %d" % (len(map[0]) - 1))
        e_x = int(input())
    e_y = int(input("Event Y coord? "))
    while e_y > (len(map) - 1):
        print("Please try a different number within: %d" % (len(map) - 1))
        e_y = int(input())
    e_t = input("What type of Event? ")
    events[e_name] = {'name': e_name, 'xcoord': e_x, 'ycoord': e_y, 'etype': e_t}
    print(events)


def check_events():
    for a in events:
            xcoord = events[a]['xcoord']
            ycoord = events[a]['ycoord']
            etype = events[a]['etype']
            if map[ycoord][xcoord] != etype:
                if map[ycoord][xcoord] != "P":
                    map[ycoord][xcoord] = etype
    show_map()

# class WorldMap:
#    def __init__(self):
#        for a in range(10):
#             for b in range(10):
#                 map.append([(a + 1), (b + 1)])
#    pass
