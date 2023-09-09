import json


class Item:
    def __init__(self, name: str,
                 description: str,
                 attack_modifier: int,
                 health_modifier: int,
                 combineable: bool,
                 combineable_items: list,
                 has_uses: bool,
                 uses_remaining: int,
                 expires_on_use: bool):
        self.name = name
        self.description = description
        self.attack_modifier = attack_modifier
        self.health_modifier = health_modifier
        self.combineable = combineable
        self.combineable_items = combineable_items
        self.has_uses = has_uses
        self.uses_remaining = uses_remaining
        self.expires_on_use = expires_on_use

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
