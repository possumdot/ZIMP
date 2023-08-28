"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""


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
