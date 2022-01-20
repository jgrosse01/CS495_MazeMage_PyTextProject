from Spell import *
# NYI


# class to subdivide spells into fire spells to organize and assure cast-ability
class FireSpell(Spell):
    def __init__(self, spell_damage, mana_cost, spell_name, spell_desc):
        Spell.__init__(self, "fire", spell_damage, mana_cost, spell_name, spell_desc)
