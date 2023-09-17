from tiles.tile import Tile


class Garden(Tile):

    def __init__(self):
        self.name = "Garden"
        self.indoor = False
        # +1  Health if turn ends here
        self.effect = "heal"
        self.exits = {
            "n": False,
            "e": True,
            "w": True,
            "s": True
        }
