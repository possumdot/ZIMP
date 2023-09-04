class Item:
    def __init__(self):
        self.name = None
        self.description = None
        self.attack_modifier = 0
        self.health_modifier = 0
        self.combineable = None
        self.combineable_items = []
        self.has_uses = None
        self.uses_remaining = None
        self.expires_on_use = None
