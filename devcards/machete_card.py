from devcards.dev_card import DevCard
from items.machete import Machete


class MacheteCard(DevCard):

    def __init__(self):
        super().__init__()
        self.card_item = Machete()
        self.nine_info = {"action": "zombies",
                          "description": "You notice 4 zombies shuffling about",
                          "zombies": 4,
                          "health_change": 0}
        self.ten_info = {"action": "event",
                         "description": "A bat poops in your eye. You lose 1 health",
                         "zombies": None,
                         "health_change": -1}
        self.eleven_info = {"action": "zombies",
                            "description": "6 zombies turn around and stare at you",
                            "zombies": 6,
                            "health_change": 0}