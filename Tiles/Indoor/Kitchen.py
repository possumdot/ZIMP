from Tiles.Tile import Tile


class Kitchen(Tile):

    def __init__(self):
        self.name = "Kitchen"
        # +1  Health if turn ends here
        self.effect = True
        self.exits = {
            "n": True,
            "e": True,
            "w": True,
            "s": False
        }
