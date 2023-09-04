class Player:

    def __init__(self, health=6, items=[None, None], has_totem=False):
        self.health = health
        self.attack = 1
        self.items = items
        self.has_totem = has_totem

    def get_attack(self, weapon=None) -> int:
        if weapon is None:
            return self.attack
        elif weapon in self.items:
            return self.attack + self.items[weapon].attack

    def add_item(self, item, item_slot=None) -> str:
        if item_slot is None and len(self.items) < 2:
            self.items.append(item)
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
