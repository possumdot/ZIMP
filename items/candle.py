from items.item import Item


class Candle(Item):
    def __init__(self):
        self.name = "Candle"
        self.description = "Combine with Oil or Gasoline to kill all Zombies on a Tile without taking damage"
        self.attack_modifier = 0
        self.health_modifier = 0
        self.combineable = True
        self.combineable_items = ["oil", "gasoline"]
        self.has_uses = True
        self.uses_remaining = 1
        self.expires_on_use = True
