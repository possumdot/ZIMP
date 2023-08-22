from Tiles.Tile import Tile


class Storage(Tile):

    def __init__(self):
        self.name = "Storage"
        self.effect = True
        self.exits = {
            "n": True,
            "e": False,
            "w": True,
            "s": False
        }
