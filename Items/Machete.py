from Items.Item import Item


class Machete(Item):
    def __init__(self):
        self.name = "Machete"
        self.description = "Adds 2 to your attack score when used in combat"
        self.attack_modifier = 2
        self.health_modifier = 0
        self.combineable = False
        self.combineable_items = []
        self.has_uses = False
        self.uses_remaining = None
        self.expires_on_use = False
