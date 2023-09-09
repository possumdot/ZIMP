import json


class GameInfo:
    def __init__(self):
        self.player = None
        self.time = 2100
        self.dev_card_deck = []
        self.indoor_tile_deck = []
        self.outdoor_tile_deck = []
        self.current_tiles = {}
        self.current_turn = 0
        self.game_turn_state = None
        self.zombie_count = 0
        self.item_on_ground = None

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __repr__(self):
        return self.__str__()

    # based on https://changsin.medium.com/how-to-serialize-a-class-object-to-json-in-python-849697a0cd3
    def __iter__(self):
        yield from {
            "player": self.player,
            "time": self.time,
            "dev_card_deck": self.dev_card_deck,
            "indoor_tile_deck": self.indoor_tile_deck,
            "outdoor_tile_deck": self.outdoor_tile_deck,
            "current_tiles": self.current_tiles,
            "current_turn": self.current_turn,
            "game_turn_state": self.game_turn_state,
            "zombie_count": self.zombie_count,
            "item_on_ground": self.item_on_ground
        }.items()
