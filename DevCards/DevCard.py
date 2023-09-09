"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
import json


class DevCard:
    def __init__(self):
        self.item = None
        self.nine_info = {"action": "",
                          "description": "",
                          "zombies": None,
                          "health_change": None}
        self.ten_info = {"action": "",
                         "description": "",
                         "zombies": None,
                         "health_change": None}
        self.eleven_info = {"action": "",
                            "description": "",
                            "zombies": None,
                            "health_change": None}

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __repr__(self):
        return self.__str__()

    # based on https://changsin.medium.com/how-to-serialize-a-class-object-to-json-in-python-849697a0cd3
    def __iter__(self):
        yield from {
            "item": self.item,
            "nine_info": self.nine_info,
            "ten_info": self.nine_info,
            "eleven_info": self.nine_info
        }.items()
