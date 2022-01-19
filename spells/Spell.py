sType = None
damage = -1
cost = -1
name = None


# Takes a String for school of spell, an int for damage the spell does, an int for mana cost, and a string for name.
class Spell:
    def __init__(self, spellType, spellDamage, manaCost, spellName):
        global sType, damage, cost, name
        sType = spellType
        damage = spellDamage
        cost = manaCost
        name = spellName

    def canCast(self, mageType):
        return mageType == sType

    def getName(self):
        return name
