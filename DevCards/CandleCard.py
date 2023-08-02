"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from DevCards.DevCard import DevCard


class CandleCard(DevCard):
    def __init__(self):
        super().__init__()
        self.card_item = "Candle"
        self.nine_description = "Your body shivers involuntarily"
        self.nine_item = None
        self.nine_zombies = None
        self.nine_health_change = None
        self.ten_description = "You feel a spark of hope"
        self.ten_item = None
        self.ten_zombies = None
        self.ten_health_change = 1
        self.eleven_description = "4 zombies look up from their card game"
        self.eleven_item = None
        self.eleven_zombies = 4
        self.eleven_health_change = None