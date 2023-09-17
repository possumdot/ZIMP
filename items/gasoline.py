from items.item import Item


class Gasoline(Item):
    def __init__(self):
        self.name = "Gasoline"
        self.description = ("Combine with Candle to kill all Zombies on one tile without taking damage.\n"
                            "Combine with Chainsaw to give two more Chainsaw uses.\n"
                            "One time use.")
        self.attack_modifier = 0
        self.health_modifier = 0
        self.combineable = True
        self.combineable_items = ["candle", "chainsaw"]
        self.has_uses = True
        self.uses_remaining = 1
        self.expires_on_use = True
