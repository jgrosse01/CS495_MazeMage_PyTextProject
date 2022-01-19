# class to manage items in the inventory

name = None


def get_name():
    return name


class Item:
    def __init__(self, item_name):
        global name
        name = item_name
