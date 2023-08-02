"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""


class DevCard:
    def __init__(self):
        self.card_item = "GolfClub"
        self.nine_description = "Slip on some nasty goo"
        self.nine_item = None
        self.nine_zombies = None
        self.nine_health_change = -1
        self.ten_description = "4 zombies stare back at you"
        self.ten_item = None
        self.ten_zombies = 4
        self.ten_health_change = None
        self.eleven_description = "The smell of blood is in the air"
        self.eleven_item = None
        self.eleven_zombies = None
        self.eleven_health_change = None
