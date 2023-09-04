class Tile:

    def __init__(self):
        self.name = None
        self.effect = False
        self.exits = {
            "n": False,
            "e": False,
            "w": False,
            "s": False
        }

    # rotates the tile 90 degrees clockwise
    def rotate(self):
        n = self.exits["n"]
        e = self.exits["e"]
        w = self.exits["w"]
        s = self.exits["s"]
        self.exits["n"] = w
        self.exits["e"] = n
        self.exits["w"] = s
        self.exits["s"] = e
