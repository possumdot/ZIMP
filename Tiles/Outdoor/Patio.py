from Tiles.Tile import Tile


class Patio(Tile):

    def __init__(self):
        self.name = "Patio"
        self.indoor = False
        # This is the only tile that can go inside
        self.effect = "patio"
        self.outdoor_exit = "n"
        self.exits = {
            "n": True,
            "e": True,
            "w": False,
            "s": True
        }