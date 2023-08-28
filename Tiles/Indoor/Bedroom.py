from Tiles.Tile import Tile


class Bedroom(Tile):

    def __init__(self):
        self.name = "Bedroom"
        self.indoor = True
        self.effect = False
        self.exits = {
            "n": True,
            "e": False,
            "w": True,
            "s": False
        }
