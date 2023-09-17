from items.item import Item


class CanOfSoda(Item):
    def __init__(self):
        self.name = "Can Of Soda"
        self.description = "Add 2 to health points on use"
        self.attack_modifier = 0
        self.health_modifier = 2
        self.combineable = False
        self.combineable_items = []
        self.has_uses = True
        self.uses_remaining = 1
        self.expires_on_use = True
