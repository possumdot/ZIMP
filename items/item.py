import json

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

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __repr__(self):
        return self.__str__()

    # based on https://changsin.medium.com/how-to-serialize-a-class-object-to-json-in-python-849697a0cd3
    def __iter__(self):
        yield from {
            "name": self.name,
            "description": self.description,
            "attack_modifier": self.attack_modifier,
            "health_modifier": self.health_modifier,
            "combineable": self.combineable,
            "combineable_items": self.combineable_items,
            "has_uses": self.has_uses,
            "uses_remaining": self.uses_remaining,
            "expires_on_use": self.expires_on_use
        }.items()
