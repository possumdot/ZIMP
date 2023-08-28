"""
Players have a starting health of 6 and a starting attack of 1
Players can only hold 2 items at a time
"""


class Player:
    def __init__(self):
        self.health = 6
        self.attack = 1
        self.items = {"item1": None, "item2": None}
        self.x = None
        self.y = None

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

    def get_items(self):
        return self.items.values()

    def get_item1(self):
        if self.items["item1"] is None:
            return "Nothing"
        else:
            return self.item_string_builder("item1")

    def get_item2(self):
        if self.items["item2"] is None:
            return "Nothing"
        else:
            return self.item_string_builder("item2")

    def item_string_builder(self, item):
        if self.items[item].has_uses:
            return f"{self.items[item].name} Uses remaining: {self.items[item].uses_remaining}"
        else:
            return f"{self.items[item].name}"

    def move(self, x, y):
        self.x = x
        self.y = y

    def take_damage(self, damage):
        self.health -= damage
