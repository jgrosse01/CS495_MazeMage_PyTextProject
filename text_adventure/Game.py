from LoadAssist import *

playerClasses = ["fire", "ice", "lightning"]    # ICE AND LIGHTNING NOT YET IMPLEMENTED
classImplemented = [True, False, False]         # for easy checking and loading regarding unimplemented classes of mage

firstEnterRoom = True

availableRooms = []
GameMap = []
# Location in the map by grid coordinates
playerLocation = (0, 0)
# Cardinal Direction facing, 0 = N, 1 = E, 2 = S, 3 = W
playerOrientation = 1

global currentRoom
global roomEnemies

global helpString
global textArt


# forces input to be lower case, ease of use by the programmer
def get_input(string):
    var = input(string).lower()
    return var


# actually interprets actions and such
def process_input(string):
    pass


# displays the current hp and mp as well as the room status
def display_status():
    pass


def load_rooms():
    # load from rooms file into available rooms
    pass


# do something with dictionaries, each room will be a dictionary
def generate_map():
    load_rooms()
    # load from the available rooms to generate the map
    pass


def load_help_string():
    # load help menu from a file into a temporary string and return it
    temp_string = ""
    file = open("../data/Help.txt")
    lines = file.readlines()
    for line in lines:
        temp_string = temp_string + line
    return temp_string


def load_text_art():
    # load text art from file into a temporary string and return it
    temp_string = ""
    file = open("../data/TextArt.txt")
    lines = file.readlines()
    for line in lines:
        temp_string = temp_string + line
    return temp_string


# act for the enemies in the current room
def do_enemies():
    pass


if __name__ == '__main__':
    # loading necessary information
    textArt = load_text_art()
    helpString = load_help_string()
    generate_map()

    print(textArt)
    input()

    while True:
        if firstEnterRoom:
            display_status()
        user_input = get_input("What would you like to do?\n")
        process_input(user_input)
        do_enemies()



