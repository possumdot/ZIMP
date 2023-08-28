from Tiles.Tile import Tile


class FamilyRoom(Tile):

    def __init__(self):
        self.name = "Family Room"
        self.indoor = True
        self.effect = False
        self.exits = {
            "n": True,
            "e": True,
            "w": True,
            "s": False
        }
