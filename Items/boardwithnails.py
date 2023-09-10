from Items.Item import Item


class BoardWithNails(Item):
    def __init__(self):
        self.name = "Board With Nails"
        self.description = "Adds 1 to your attack score when attacking with this item"
        self.attack_modifier = 1
        self.health_modifier = 0
        self.combineable = False
        self.combineable_items = []
        self.has_uses = False
        self.uses_remaining = None
        self.expires_on_use = False
