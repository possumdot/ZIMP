"""
devcards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each devcards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from devcards.dev_card import DevCard
from items.grisly_femur import GrislyFemur


class GrislyFemurCard(DevCard):
    def __init__(self):
        super().__init__()
        self.card_item = GrislyFemur()
        self.nine_info = {"action": "item",
                          "description": "An Item lies on the ground",
                          "zombies": None,
                          "health_change": 0}
        self.ten_info = {"action": "zombies",
                         "description": "5 zombies surprise you",
                         "zombies": 5,
                         "health_change": 0}
        self.eleven_info = {"action": "event",
                            "description": "Your soul isn't wanted here",
                            "zombies": None,
                            "health_change": -1}