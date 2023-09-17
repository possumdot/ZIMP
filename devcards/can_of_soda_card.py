"""
devcards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each devcards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from devcards.dev_card import DevCard
from items.can_of_soda import CanOfSoda


class CanOfSodaCard(DevCard):
    def __init__(self):
        super().__init__()
        self.card_item = CanOfSoda()
        self.nine_info = {"action": "event",
                          "description": "Candybar in your pocket",
                          "zombies": None,
                          "health_change": 1}
        self.ten_info = {"action": "item",
                         "description": "You see an Item",
                         "zombies": None,
                         "health_change": 0}
        self.eleven_info = {"action": "zombies",
                            "description": "4 zombies block your exit",
                            "zombies": 4,
                            "health_change": 0}
