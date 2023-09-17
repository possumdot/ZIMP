from tiles.tile import Tile


class SittingArea(Tile):

    def __init__(self):
        self.name = "Sitting Area"
        self.indoor = False
        self.effect = False
        self.exits = {
            "n": False,
            "e": True,
            "w": True,
            "s": True
        }
