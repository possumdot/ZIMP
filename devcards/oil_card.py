"""
devcards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each devcards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from devcards.dev_card import DevCard
from items.oil import Oil


class OilCard(DevCard):
    def __init__(self):
        super().__init__()
        self.card_item = Oil()
        self.nine_info = {"action": "event",
                          "description": "You try hard not to wet yourself",
                          "zombies": None,
                          "health_change": 0}
        self.ten_info = {"action": "item",
                         "description": "An Item lays on the ground before you",
                         "zombies": None,
                         "health_change": 0}
        self.eleven_info = {"action": "zombies",
                            "description": "You see 6 zombies start to approach you",
                            "zombies": 6,
                            "health_change": 0}
