"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from DevCards.DevCard import DevCard
from Items.Chainsaw import Chainsaw


class ChainsawCard(DevCard):
    def __init__(self):
        self.card_item = Chainsaw()
        self.nine_info = {"action": "zombies",
                          "description": "3 zombies are hanging around",
                          "zombies": 3,
                          "health_change": 0}
        self.ten_info = {"action": "event",
                         "description": "You hear terrible screams",
                         "zombies": None,
                         "health_change": 0}
        self.eleven_info = {"action": "zombies",
                            "description": "5 zombies. 5 OF THEM.",
                            "zombies": 5,
                            "health_change": 0}
