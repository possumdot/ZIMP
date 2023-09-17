"""
Players have a starting health of 6 and a starting attack of 1
Players can only hold 2 items at a time
"""
import json


class Player:
    def __init__(self, health: int, has_totem: bool, x: int, y: int, item1=None, item2=None):
        self.health = health
        self.attack = 1
        self.items = {"item1": item1,
                      "item2": item2}
        self.has_totem = has_totem
        self.x = x
        self.y = y

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __repr__(self):
        return self.__str__()

    # based on https://changsin.medium.com/how-to-serialize-a-class-object-to-json-in-python-849697a0cd3
    def __iter__(self):
        yield from {
            "health": self.health,
            "attack": self.attack,
            "items": self.items,
            "has_totem": self.has_totem,
            "x": self.x,
            "y": self.y
        }.items()

    def heal(self, amount):
        """ Applies a given value of healing to the player, negative and positive values are handled as you would expect
        """
        self.health += amount

    def drop_item(self, item_slot):
        """ Sets a given itemslot to None as the item has been dropped
        """
        match item_slot:
            case 1:
                self.items["item1"] = None
            case 2:
                self.items["item2"] = None

    def give_item(self, item, item_slot):
        """ Gives the player an item and places it in a given item slot
        """
        match item_slot:
            case 1:
                self.items["item1"] = item
            case 2:
                self.items["item2"] = item

    def get_item1(self):
        """ Returns a string representing the state of the item in item slot 1
        """
        if self.items["item1"] is None:
            return "Nothing"
        else:
            return self.item_string_builder("item1")

    def get_item2(self):
        """ Returns a string representing the state of the item in item slot 2
        """
        if self.items["item2"] is None:
            return "Nothing"
        else:
            return self.item_string_builder("item2")

    def item_string_builder(self, item_slot):
        """ Returns a string representing the state of the item in a given item slot
        """
        if self.items[item_slot].has_uses:
            return f"{self.items[item_slot].name} Uses remaining: {self.items[item_slot].uses_remaining}"
        else:
            return f"{self.items[item_slot].name}"

    def move(self, x, y):
        """ Moves the player to the given x y coordinates"""
        self.x = x
        self.y = y

    def take_damage(self, damage):
        """ Inflicts a given amount of damage on the player
        """
        self.health -= damage