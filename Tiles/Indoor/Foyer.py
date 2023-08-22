from Tiles.Tile import Tile


# the player always starts in this room
class Foyer(Tile):

    def __init__(self):
        self.name = "Foyer"
        self.effect = False
        self.exits = {
            "n": True,
            "e": False,
            "w": False,
            "s": False
        }
