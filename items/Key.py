# NOT YET IMPLEMENTED
class Key:
    def __init__(self, key_color, door_number):
        self.color = key_color
        self.number = door_number

    def check_color(self, compare_color):
        return compare_color == self.color

    def check_number(self, compare_number):
        return compare_number == self.number
