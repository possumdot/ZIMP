from items.item import Item


class Oil(Item):
    def __init__(self):
        self.name = "Oil"
        self.description = ("Throw as you Run Away to avoid taking damage.\n"
                            "Combine with Candle to kill all Zombies on one tile without taking damage.\n"
                            "One use only")
        self.attack_modifier = 0
        self.health_modifier = 0
        self.combineable = True
        self.combineable_items = ["candle"]
        self.has_uses = True
        self.uses_remaining = 1
        self.expires_on_use = True
