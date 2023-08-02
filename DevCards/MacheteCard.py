from DevCards.DevCard import DevCard


class CardMachete(DevCard):

    def __init__(self):
        super().__init__()
        self.card_item = "Machete"
        self.nine_description = "You notice 4 zombies shuffling about"
        self.nine_item = None
        self.nine_zombies = 4
        self.nine_health_change = None
        self.ten_description = "A bat poops in your eye. You lose 1 health"
        self.ten_item = None
        self.ten_zombies = None
        self.ten_health_change = -1
        self.eleven_description = "6 zombies turn around and stare at you"
        self.eleven_item = None
        self.eleven_zombies = 6
        self.eleven_health_change = None
