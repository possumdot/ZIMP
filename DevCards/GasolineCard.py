"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""
from DevCards.DevCard import DevCard


class GasolineCard(DevCard):
    def __init__(self):
        super().__init__()
        self.card_item = "Gasoline"
        self.nine_description = "4 zombies shamble about"
        self.nine_item = None
        self.nine_zombies = 4
        self.nine_health_change = None
        self.ten_description = "You sense your impending doom"
        self.ten_item = None
        self.ten_zombies = None
        self.ten_health_change = -1
        self.eleven_description = "A canister of gasoline sits invitingly on the floor"
        self.eleven_item = "Gasoline"
        self.eleven_zombies = None
        self.eleven_health_change = None
