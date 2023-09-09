import json


class Tile:

    def __init__(self):
        self.name = None
        self.effect = False
        self.indoor = None
        self.exits = {
            "n": False,
            "e": False,
            "w": False,
            "s": False
        }
        # a transition_exit is only if the room has exit that leads from inside to outside or vice versa
        self.transitional_exit = {
            "n": False,
            "e": False,
            "w": False,
            "s": False
        }

    #
    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __repr__(self):
        return self.__str__()

    # based on https://changsin.medium.com/how-to-serialize-a-class-object-to-json-in-python-849697a0cd3
    def __iter__(self):
        yield from {
            "name": self.name,
            "is_inside": self.indoor,
            "effect": self.effect,
            "exits": self.exits,
            "transition_exit": self.transitional_exit
        }.items()

    # rotates the tile 90 degrees clockwise
    def rotate(self):
        n = self.exits["n"]
        e = self.exits["e"]
        w = self.exits["w"]
        s = self.exits["s"]
        self.exits["n"] = w
        self.exits["e"] = n
        self.exits["w"] = s
        self.exits["s"] = e
