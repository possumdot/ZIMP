from Tiles.Tile import Tile


class Bathroom(Tile):

    def __init__(self):
        self.name = "Bathroom"
        self.indoor = True
        self.effect = False
        self.exits = {
            "n": True,
            "e": False,
            "w": False,
            "s": False
        }
