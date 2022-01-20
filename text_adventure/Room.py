from enemies.Skeleton import *
from enemies.Specter import *
from enemies.Atronach import *
# NYI

# NEED LISTS OF POTENTIAL ITEMS AND SPELLS TO RANDOMLY PULL FROM FOR GENERATION


# a room class to better manage the maze map
class Room:
    def __init__(self, dev_number, title, num_skeletons, num_specters, num_atronachs, num_items, num_spells,
                 key, can_exit, description):
        self.can_exit = False
        self.number = dev_number
        self.title = title
        self.enemies = []
        self.items = []
        self.spells = []
        self.description = description
        # separate generation methods because random picking for items and spells was a bit much to put in a constructor
        self.generate_enemies(num_skeletons, num_specters, num_atronachs)
        self.generate_items(num_items, key)
        self.generate_spells(num_spells)
        # two stage check for redundancy
        if dev_number == 2 and can_exit == 1:
            self.can_exit = True

    # generates enemies and changes description based on enemy counts passed
    def generate_enemies(self, num_skele, num_spec, num_atro):
        for i in range(num_skele):
            self.enemies.append(Skeleton())
        for i in range(num_spec):
            self.enemies.append(Specter())
        for i in range(num_atro):
            self.enemies.append(Atronach())

        if num_skele > 0:
            self.description = self.description + f"\nThere are {num_skele} skeletons in this room."
        if num_spec > 0:
            self.description = self.description + f"\nThere are {num_spec} specters in this room."
        if num_atro > 0:
            self.description = self.description + f"\nThere are {num_atro} atronachs in this room."
        pass

    # generates items and changes description based on item counts NYI
    def generate_items(self, num_items, key):
        pass

    # generate spells and changes description based on spell counts NYI
    def generate_spells(self, num_spells):
        pass

    # determines whether the player can exit from a room
    def is_exit(self):
        return self.can_exit
