# class to manage player
class Player:
    def __init__(self, mage_type, hp=100, mp=50, mp_regen=2):
        self.max_health = hp
        self.max_mana = mp
        self.health = hp
        self.mana = mp
        self.health_regen = 4
        self.mana_regen = mp_regen
        self.inventory = []
        self.spells = []
        self.mage_type = mage_type
        self.escaped = False

    # adds a single item to the inventory
    def add_to_inventory(self, item):
        self.inventory.append(item)

    # removes a single item from the inventory and applies the item's affect to the player
    def use_item(self, item):
        pass

    # used to remove health when damage is taken
    def damage_player(self, amount):
        self.health = self.health - amount

    # used to increase health by the heal command
    def heal_player(self):
        self.mana = self.mana - 25
        self.health = self.health + min(self.max_health-self.health, 10)

    # used to increase health and mana by the standard regeneration
    def regen_player(self):
        # restore either the regular mana regen or whatever is left between the current and the max
        self.mana = self.mana + min(self.max_mana-self.mana, self.mana_regen)
        # restore either the regular hp regen or whatever is left between the current and the max
        self.health = self.health + min(self.max_health-self.health, self.health_regen)

    # increment max health (like when you get an hp potion)
    def inc_max_hp(self, amount):
        self.max_health = self.max_health + amount

    # increment max mana and mana regen (like when you get an mp potion)
    # regen increases at 2/25 the rate of the maximum
    def inc_max_mana(self, amount):
        self.max_mana = self.max_mana + amount
        self.mana_regen = self.mana_regen + (2/25)*amount

    # lists all items the player has in their inventory
    def list_items(self):
        print(self.inventory[0].get_name())
        for i in range(1, len(self.inventory)):
            print(f", {self.inventory[i].get_name()}")
        print("\n")

    # lists all the spells the player has in their spellbook
    def list_spells(self):
        print(self.spells[0].get_name())
        for i in range(1, len(self.spells)):
            print(f", {self.spells[i].get_name()}")
        print("\n")

    # gives the number of items in the player inventory
    def get_inventory_size(self):
        return len(self.inventory)

    # gives the number of spells in the player spellbook
    def get_spellbook_size(self):
        return len(self.spells)

    # gives the string which reflects the type of mage the player is
    def get_mage_type(self):
        return self.mage_type

    # gives the current health of the mage
    def get_hp(self):
        return self.health

    # gives max hp of the mage
    def get_max_hp(self):
        return self.max_health

    # gives the current mana of the mage
    def get_mana(self):
        return self.mana

    # checks if the player is alive (health above zero)
    def is_alive(self):
        return self.health > 0

    # sets the win condition to true
    def escape(self):
        self.escaped = True

    # checks the win condition
    def did_escape(self):
        return self.escaped

    # prints the hp/max_hp and the mana/max_mana of the mage
    def print_stats(self):
        print(f"HP: {self.health}/{self.max_health} MP: {self.mana}/{self.max_mana}\n")
