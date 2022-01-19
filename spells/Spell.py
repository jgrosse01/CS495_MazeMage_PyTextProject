# class to manage spells in spellbook
sType = None
damage = -1
cost = -1
name = None


def can_cast(mage_type):
    return mage_type == sType


def get_name():
    return name


# Takes a String for school of spell, an int for damage the spell does, an int for mana cost, and a string for name.
class Spell:
    def __init__(self, spell_type, spell_damage, mana_cost, spell_name):
        global sType, damage, cost, name
        sType = spell_type
        damage = spell_damage
        cost = mana_cost
        name = spell_name
