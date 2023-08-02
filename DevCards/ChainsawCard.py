"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from DevCards.DevCard import DevCard


class ChainsawCard(DevCard):
    def __init__(self):
        super().__init__()
        self.card_item = "Chainsaw"
        self.nine_description = "3 zombies are hanging around"
        self.nine_item = None
        self.nine_zombies = 3
        self.nine_health_change = None
        self.ten_description = "You hear terrible screams"
        self.ten_item = None
        self.ten_zombies = None
        self.ten_health_change = None
        self.eleven_description = "5 zombies. 5 OF THEM."
        self.eleven_item = None
        self.eleven_zombies = 5
        self.eleven_health_change = None
