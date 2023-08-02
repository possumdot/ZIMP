"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from DevCards.DevCard import DevCard


class SodaCard(DevCard):
    def __init__(self):
        super().__init__()
        self.card_item = "SodaCan"
        self.nine_description = "Candybar in your pocket"
        self.nine_item = None
        self.nine_zombies = None
        self.nine_health_change = 1
        self.ten_description = "A can of soda sits on the ground enticingly, it doesn't look suspicious"
        self.ten_item = "SodaCan"
        self.ten_zombies = None
        self.ten_health_change = None
        self.eleven_description = "4 zombies block your exit"
        self.eleven_item = None
        self.eleven_zombies = 4
        self.eleven_health_change = None
