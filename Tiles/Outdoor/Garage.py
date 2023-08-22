from Tiles.Tile import Tile


class Garage(Tile):

    def __init__(self):
        self.name = "Garage"
        self.effect = False
        self.exits = {
            "n": False,
            "e": False,
            "w": True,
            "s": True
        }
