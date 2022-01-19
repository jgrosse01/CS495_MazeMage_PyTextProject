color = None
number = -1


# NOT YET IMPLEMENTED
class Key:
    def __init__(self, keyColor, doorNumber):
        global color, number
        color = keyColor
        number = doorNumber

    def checkColor(self, compareColor):
        return compareColor == color

    def checkNumber(self, compareNumber):
        return compareNumber == number
