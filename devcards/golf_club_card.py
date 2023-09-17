"""
devcards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each devcards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from devcards.dev_card import DevCard
from items.golf_club import GolfClub

class GolfClubCard(DevCard):
    def __init__(self):
        super().__init__()
        self.card_item = GolfClub()
        self.nine_info = {"action": "event",
                          "description": "Slip on some nasty goo",
                          "zombies": None,
                          "health_change": -1}
        self.ten_info = {"action": "zombies",
                         "description": "4 zombies stare back at you",
                         "zombies": 4,
                         "health_change": 0}
        self.eleven_info = {"action": "event",
                            "description": "The smell of blood is in the air",
                            "zombies": None,
                            "health_change": 0}