from items.item import Item


class GrislyFemur(Item):
    def __init__(self):
        self.name = "Grisly Femur"
        self.description = "Adds 1 to attack score on attack"
        self.attack_modifier = 1
        self.health_modifier = 0
        self.combineable = False
        self.combineable_items = []
        self.has_uses = False
        self.uses_remaining = None
        self.expires_on_use = False
