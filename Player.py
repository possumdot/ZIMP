"""
Players have a starting health of 6 and a starting attack of 1
Players can only hold 2 items at a time
"""


class Player:
    def __init__(self):
        self.health = 6
        self.attack = 1
        self.item_1 = None
        self.item_2 = None

    def heal(self, amount):
        self.health += amount

    def take_damage(self, amount):
        self.health -= amount

    def drop_item(self, item_slot):
        match item_slot:
            case 1:
                self.item_1 = None
            case 2:
                self.item_2 = None

    def give_item(self, item, item_slot):
        match item_slot:
            case 1:
                self.item_1 = item
            case 2:
                self.item_2 = item

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_item_slot_1(self):
        return self.item_1

    def get_item_slot_2(self):
        return self.item_2
