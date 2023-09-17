from items.item import Item


class Chainsaw(Item):
    def __init__(self):
        self.name = "Chainsaw"
        self.uses_remaining = 2
        self.description = f"Adds 3 to your attack score when used in combat. Starts with 2 uses"
        self.attack_modifier = 0
        self.health_modifier = 0
        self.combineable = True
        self.combineable_items = ["gasoline"]
        self.has_uses = True
        self.expires_on_use = False
