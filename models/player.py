import json


class Player:

    def __init__(self, health: int, items: dict, has_totem: bool, x:int, y: int):
        self.health = health
        self.attack = 1
        self.items = items
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
            "has_totem": self.has_totem
        }.items()

    def get_attack(self, weapon=None) -> int:
        if weapon is None:
            return self.attack
        elif weapon in self.items:
            return self.attack + self.items[weapon].attack

    def add_item(self, item, item_slot=None) -> str:
        if item_slot is None and len(self.items) < 2:
            self.items[item]
            return f"You picked up {item}"
        elif item_slot is None and len(self.items) >= 2:
            return "You can't carry more than two items"
        else:
            self.items[item_slot] = item
            return f"You now have {item}"

    def has_item(self, item) -> bool:
        if item in self.items:
            return True
        else:
            return False

