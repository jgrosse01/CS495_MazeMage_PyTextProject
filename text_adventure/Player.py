inventory = []
spells = []
health = 100
mana = 50


class Player:

    def __init__(self, hp = 100, mp = 50):
        global health, mana
        health = hp
        mana = mp

    def addToInventory(item):
        inventory.append(item)
