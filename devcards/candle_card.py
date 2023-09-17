"""
devcards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each devcards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
import json

from devcards.dev_card import DevCard
from items.candle import Candle


class CandleCard(DevCard):
    def __init__(self):
        self.card_item = Candle()
        self.nine_info = {"action": "event",
                          "description": "Your body shivers involuntarily",
                          "zombies": None,
                          "health_change": 0}
        self.ten_info = {"action": "event",
                         "description": "You feel a spark of hope",
                         "zombies": None,
                         "health_change": 1}
        self.eleven_info = {"action": "zombies",
                            "description": "4 zombies look up from their card game",
                            "zombies": 4,
                            "health_change": 0}