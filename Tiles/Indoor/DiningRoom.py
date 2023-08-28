from Tiles.Tile import Tile


class DiningRoom(Tile):

    def __init__(self):
        self.name = "Dining Room"
        self.indoor = True
        # This is the only tile that can go outside
        self.effect = True
        self.exits = {
            "n": True,
            "e": True,
            "w": True,
            "s": True
        }
