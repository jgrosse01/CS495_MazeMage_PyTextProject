# Takes a String for school of spell, an int for damage the spell does,
# an int for mana cost, a name string, and a description. NYI
class Spell:
    def __init__(self, spell_type, spell_damage, mana_cost, spell_name, spell_desc):
        self.type = spell_type
        self.damage = spell_damage
        self.cost = mana_cost
        self.name = spell_name
        self.description = spell_desc

    # checks the mage's school and spell school to see if the spell may be cast
    def can_cast(self, mage_type):
        return mage_type == self.type

    # gets the name of the spell
    def get_name(self):
        return self.name

    # gets the description of the spell
    def get_desc(self):
        return self.description
