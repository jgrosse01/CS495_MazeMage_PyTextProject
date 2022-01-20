# NYI
from LoadAssist import *
from Player import *
import time

# commands which are exempt from player regen and enemy movement
exemptCommands = ["help", "repeat", "stats", "list", "describe"]
# boolean to update regen and enemies
canUpdate = True

playerClasses = ["fire", "ice", "lightning"]    # ICE AND LIGHTNING NOT YET IMPLEMENTED
classImplemented = [True, False, False]         # for easy checking and loading regarding unimplemented classes of mage
# spell dictionary to reference descriptions by name
spellDict = {}

# boolean to track if the player is entering a new room, set to false after the
# first print of the description and set to true whenever moving to another room
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
global win
global game_over


# forces input to be lower case, ease of use by the programmer
def get_input(string):
    var = input(string).lower()
    return var


# actually interprets actions and such
def process_input(string):
    temp_string = string
    if len(temp_string) != 0:
        # respond to help input
        if temp_string == "help":
            print(helpString)
        # respond to repeat input
        elif temp_string == "repeat":
            print("Feature not yet implemented\n")
        # respond to stats input
        elif temp_string == "stats":
            player.print_stats()
        # respond to list input
        elif temp_string.split()[0] == "list":
            # check to make sure there is another word to access
            if len(temp_string.split()) > 1:
                # list inventory
                if temp_string.split()[1] == "inventory":
                    if player.get_inventory_size() == 0:
                        print("Your inventory is empty.\n")
                    else:
                        player.list_items()
                # list spells
                elif temp_string.split()[1] == "spells":
                    if player.get_spellbook_size() == 0:
                        print("You have no spells in your spellbook! "
                              "\nThere is a starter spell on the ground in the spawn room.\n")
                    else:
                        player.list_spells()
                else:
                    print("Please select a container.\n")
            else:
                print("Please either specify your magic bag (inventory) or spellbook (spells).\n")
        # respond to acquire input
        elif temp_string.split()[0] == "acquire":
            print("Feature not yet implemented\n")
        # respond to turn input
        elif temp_string.split()[0] == "turn":
            print("Feature not yet implemented\n")
        # respond to move input
        elif temp_string.split()[0] == "move":
            print("Feature not yet implemented\n")
        # respond to cast input
        elif temp_string.split()[0] == "cast":
            print("Feature not yet implemented\n")
        # respond to heal input
        elif temp_string == "heal":
            max_hp = player.get_max_hp()
            hp = player.get_hp()
            mana = player.get_mana()
            if hp < max_hp and mana >= 25:
                player.heal_player()
                print("You have been healed.\n")
            elif hp >= max_hp:
                print("You are not hurt.\n")
            else:
                print("You do not have enough mana to heal.\n")
        # respond to describe input
        elif temp_string.split()[0] == "describe":
            # if they specify one word with the command
            if len(temp_string.split()) == 2:
                if spellDict[temp_string.split()[1]] is None:
                    print("That spell does not exist in this realm of the ethereal plane.\n")
                else:
                    # done for aesthetic reasons to get a capital first letter of the spell
                    print(f"{temp_string.split()[1][0:1].upper()}{temp_string.split()[1][1:]}. "
                          f"{spellDict[temp_string.split()[1]]}\n")
            # if there is more than one word with the command it is invalid
            elif len(temp_string.split()) > 2:
                print("Spell names are written as one word.\n")
            # otherwise, the command is invalid because it does not have a spell attached to it and is just the keyword
            else:
                print("Please select a spell to describe.\n")
        # respond to use input
        elif temp_string.split()[0] == "use":
            print("Feature not yet implemented\n")
        # respond to escape input
        elif temp_string == "escape":
            print("You can't escape because I haven't implemented that yet! Mwahaha!\n")
        # respond to exit input
        elif temp_string == "exit":
            print("Exiting Game")
            time.sleep(2)
            exit(0)
        else:
            # invalid characters typed (not one of the determined commands
            print("Please issue a valid command. Type \"help\" for details.")
    else:
        # nothing typed (input something)
        print("Please input something... I didn't think anybody would type... well... NOTHING!")
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


# load help menu from a file into a temporary string and return it
def load_help_string():
    temp_string = ""
    file = open("../data/Help.txt")
    lines = file.readlines()
    for line in lines:
        temp_string = temp_string + line
    return temp_string


# load text art from file into a temporary string and return it
def load_text_art():
    temp_string = ""
    file = open("../data/TextArt.txt")
    lines = file.readlines()
    for line in lines:
        temp_string = temp_string + line
    return temp_string


# load win art from file into a string to return
def load_win():
    temp_string = ""
    file = open("../data/Win.txt")
    lines = file.readlines()
    for line in lines:
        temp_string = temp_string + line
    return temp_string


# load game over art from file into a string to return
def load_game_over():
    temp_string = ""
    file = open("../data/GameOver.txt")
    lines = file.readlines()
    for line in lines:
        temp_string = temp_string + line
    return temp_string


# load the spell descriptions into a dictionary keyed by name
def load_spell_desc_dict():
    file = open("../data/SpellData.txt")
    lines = file.readlines()
    for line in lines:
        temp = line.split(';')
        # if the first character in a line is a hashtag, this is a comment and the line will be skipped
        if temp[0][0:1] == "#":
            # skip to next loop iteration
            pass
        # if it is not a comment then load the description into the dictionary keyed by name
        spellDict[temp[3].lower()] = temp[4]


# act for the enemies in the current room
def do_enemies():
    pass


# Game loop found in main method
if __name__ == '__main__':
    # true loop to bring back the main menu every time the game is ended
    while True:
        # loading necessary information for the game/demo/whatever this is when the due date comes
        textArt = load_text_art()
        win = load_win()
        game_over = load_game_over()
        helpString = load_help_string()
        load_spell_desc_dict()
        # generate_map()  # NYI

        # Begin game (MAIN DISPLAY)
        print(textArt)

        # creates the player as a new fire mage (no purpose yet, other types not implemented)
        player = Player(playerClasses[0])

        # Input waits for enter key
        input()

        # game loop
        while player.is_alive():
            # display room description upon first entering a room
            if firstEnterRoom:
                display_status()
            # get input from user and print extra spaces
            user_input = get_input("What would you like to do?\n\n")
            print("\n")
            # delegating processing of input to another... long... method
            process_input(user_input)
            print("\n")

            # if the user did a non-update command, set flag to false
            if user_input in exemptCommands:
                canUpdate = False
            # if the game can update, regen and make enemies move/attack
            if canUpdate:
                player.regen_player()
                do_enemies()
            # if the update status was false, return it to true
            canUpdate = True

            if player.did_escape():
                print(win)
                break
        # if player dies print game over, wait, and print lots of new lines to go back to the menu
        print(game_over)
        time.sleep(5)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
