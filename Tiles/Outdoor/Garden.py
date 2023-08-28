from Tiles.Tile import Tile


class Garden(Tile):

    def __init__(self):
        self.name = "Garden"
        self.indoor = False
        # +1  Health if turn ends here
        self.effect = True
        self.exits = {
            "n": False,
            "e": True,
            "w": True,
            "s": True
        }
