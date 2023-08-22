from Tiles.Tile import Tile


# Three of these exist in the base game
class Yard(Tile):

    def __init__(self):
        self.name = "Yard"
        self.effect = False
        self.exits = {
            "n": False,
            "e": True,
            "w": True,
            "s": True
        }
