"""
DevCards have effects that change depending on the in game time
Each DevCard has one item associated with them
Each DevCards ALWAYS has a description and potentially an item OR a number of zombies OR either a positive or negative
change to the players health
"""


class DevCard:
    def __init__(self):
        self.card_item = "NailBoard"
        self.nine_description = "A board with nails sticks out of the ground, you're pretty sure you can remove it"
        self.nine_item = "NailBoard"
        self.nine_zombies = None
        self.nine_health_change = None
        self.ten_description = "4 zombies mill about zombiely"
        self.ten_item = None
        self.ten_zombies = 4
        self.ten_health_change = None
        self.eleven_description = "Something icky in your mouth"
        self.eleven_item = None
        self.eleven_zombies = None
        self.eleven_health_change = -1
