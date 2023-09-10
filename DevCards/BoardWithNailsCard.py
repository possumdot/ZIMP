"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from DevCards.DevCard import DevCard
from Items.boardwithnails import BoardWithNails


class BoardWithNailsCard(DevCard):
    def __init__(self):
        super().__init__()
        self.card_item = BoardWithNails()
        self.nine_info = {"action": "item",
                          "description": "You see an Item on the ground",
                          "zombies": None,
                          "health_change": 0}
        self.ten_info = {"action": "zombies",
                         "description": "4 zombies mill about zombiely",
                         "zombies": 4,
                         "health_change": 0}
        self.eleven_info = {"action": "event",
                            "description": "Something icky in your mouth",
                            "zombies": None,
                            "health_change": -1}
