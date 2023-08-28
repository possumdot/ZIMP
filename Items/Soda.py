from Items.Item import Item


class Soda(Item):
    def __init__(self):
        self.name = "Can of Soda"
        self.description = "Add 2 to health points on use"
        self.attack_modifier = 0
        self.health_modifier = 2
        self.combineable = False
        self.combineable_items = []
        self.has_uses = True
        self.uses_remaining = 1
        self.expires_on_use = True
