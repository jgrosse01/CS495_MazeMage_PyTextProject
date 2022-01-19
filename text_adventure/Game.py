playerClasses = ["fire", "ice", "lightning"]    # ICE AND LIGHTNING NOT YET IMPLEMENTED
classImplemented = [True, False, False]         # for easy checking and loading regarding unimplemented classes of mage

availableRooms = []
GameMap = [9][9]
# Location in the map by grid coordinates
playerLocation = (0,0)
# Cardinal Direction facing, 0 = N, 1 = E, 2 = S, 3 = W
playerOrientation = 1

helpString = ""
textArt = ""


# forces input to be lower case, ease of use by the programmer
def getInput(string):
    var = input(string).lower()
    return var


# actually interprets actions and such
def processInput(string):
    pass


# displays the current hp and mp as well as the room status
def displayStatus():
    pass


def loadHelpString():
    pass


def loadTextArt():
    pass


if __name__ == '__main__':
    global helpString, GameMap, playerClasses, classImplemented
