from Tiles.Tile import Tile


# Three of these exist in the base game
class Graveyard(Tile):

    def __init__(self):
        self.name = "Graveyard"
        self.indoor = False
        # Can choose to resolve a second Dev card to bury the totem and win the game
        self.effect = "graveyard"
        self.exits = {
            "n": False,
            "e": True,
            "w": False,
            "s": True
        }
