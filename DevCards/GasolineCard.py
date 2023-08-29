"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from DevCards.DevCard import DevCard
from Items.Gasoline import Gasoline


class GasolineCard(DevCard):
    def __init__(self):
        self.card_item = Gasoline()
        self.nine_info = {"action": "zombies",
                          "description": "4 zombies shamble about",
                          "zombies": 4,
                          "health_change": 0}
        self.ten_info = {"action": "event",
                         "description": "You sense your impending doom",
                         "zombies": None,
                         "health_change": -1}
        self.eleven_info = {"action": "item",
                            "description": "You see an Item on the ground",
                            "zombies": None,
                            "health_change": 0}
