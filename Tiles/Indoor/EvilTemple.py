from Tiles.Tile import Tile


class EvilTemple(Tile):

    def __init__(self):
        self.name = "Evil Temple"
        # Can choose to resolve a second Dev card to find the totem
        self.effect = True
        self.exits = {
            "n": False,
            "e": True,
            "w": True,
            "s": False
        }
