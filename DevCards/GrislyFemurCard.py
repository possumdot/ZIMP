"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from DevCards.DevCard import DevCard


class GrislyFemurCard(DevCard):
    def __init__(self):
        super().__init__()
        self.card_item = "GrislyFemur"
        self.nine_description = "A Grisly Femur lies on the ground"
        self.nine_item = "GrislyFemur"
        self.nine_zombies = None
        self.nine_health_change = None
        self.ten_description = "5 zombies surprise you"
        self.ten_item = None
        self.ten_zombies = 5
        self.ten_health_change = None
        self.eleven_description = "Your soul isn't wanted here"
        self.eleven_item = None
        self.eleven_zombies = None
        self.eleven_health_change = -1
