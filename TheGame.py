import random

import Player
from DevCards.CandleCard import CandleCard
from DevCards.ChainsawCard import ChainsawCard
from DevCards.GasolineCard import GasolineCard
from DevCards.GolfClubCard import GolfClubCard
from DevCards.GrislyFemurCard import GrislyFemurCard
from DevCards.MacheteCard import MacheteCard
from DevCards.NailBoardCard import NailBoardCard
from DevCards.OilCard import OilCard
from DevCards.SodaCard import SodaCard
from Tiles.Indoor.Bathroom import Bathroom
from Tiles.Indoor.Bedroom import Bedroom
from Tiles.Indoor.DiningRoom import DiningRoom
from Tiles.Indoor.EvilTemple import EvilTemple
from Tiles.Indoor.FamilyRoom import FamilyRoom
from Tiles.Indoor.Foyer import Foyer
from Tiles.Indoor.Kitchen import Kitchen
from Tiles.Indoor.Storage import Storage
from Tiles.Outdoor.Garage import Garage
from Tiles.Outdoor.Garden import Garden
from Tiles.Outdoor.Graveyard import Graveyard
from Tiles.Outdoor.SittingArea import SittingArea
from Tiles.Outdoor.Yard import Yard


class TheGame:
    def __init__(self):
        self.time = 2100
        self.dev_card_deck = self.get_dev_card_deck()
        self.indoor_tile_deck = self.get_indoor_tile_deck()
        self.outdoor_tile_deck = self.get_outdoor_tile_deck()
        self.current_tiles = {}

    def add_player(self):
        player = Player

    def game_loop(self):
        # Start player at x = 10, y = 10 in the Lobby
        # 1. Choose an exit door into a new room or a room that already existed
        # 2. If a new room, draw and place an indoor tile,
        self.first_move()
        game_command = self.get_game_command()
        while game_command[0].lower() != "exit":
            # if time is 2400, game time has run out and the player loses
            if self.time != 2400:
                match game_command[0].lower():
                    case "move":
                        self.move(game_command[1])
                        break
                    case _:
                        print(f"{game_command[0]} is not a valid command, please enter a valid command."
                              f" Type Help for a list")
                game_command = self.get_game_command()
            else:
                game_command = input("Your time has run out and the zombies win, type Replay to start again, Stats to"
                                     "view your stats or Exit to close the game")

    def get_game_command(self):
        game_command = input(">>>")
        return game_command.split()

    def move(self, direction=None):
        if direction is None:
            direction = input("Please enter a direction (NEWS or North East West South)")
        # Direction name doesn't actually matter, only the first letter ^[n|north|e|east|w|west|s|south]$
        direction = direction.lower()
        valid_directions = ["n", "north", "e", "east", "w", "west", "s", "south"]
        if direction in valid_directions:
            print(direction)

    #            self.move_character(direction[0])

    #    def move_character(self, direction):

    def get_dev_card_deck(self):
        candle_card = CandleCard
        chainsaw_card = ChainsawCard
        gasoline_card = GasolineCard
        golfclub_card = GolfClubCard
        grislyfemur_card = GrislyFemurCard
        machete_card = MacheteCard
        nailboard_card = NailBoardCard
        oil_card = OilCard
        soda_card = SodaCard
        return [candle_card, chainsaw_card, gasoline_card, golfclub_card, grislyfemur_card, machete_card,
                nailboard_card, oil_card, soda_card]

    def get_indoor_tile_deck(self):
        bathroom_tile = Bathroom
        bedroom_tile = Bedroom
        dining_room_tile = DiningRoom
        evil_temple_tile = EvilTemple
        family_room_tile = FamilyRoom
        kitchen_tile = Kitchen
        storage = Storage
        return [bathroom_tile, bedroom_tile, dining_room_tile, evil_temple_tile, family_room_tile, kitchen_tile,
                storage]

    def get_outdoor_tile_deck(self):
        garage_tile = Garage
        garden_tile = Garden
        graveyard_tile = Graveyard
        sitting_area_tile = SittingArea
        yard1_tile = Yard
        yard2_tile = Yard
        yard3_tile = Yard
        return [garage_tile, garden_tile, graveyard_tile, sitting_area_tile, yard1_tile, yard2_tile, yard3_tile]

    # returns a card and removes it from the active deck, if no more cards exists, time passes
    def draw_dev_card(self):
        if len(self.dev_card_deck) > 0:
            result = random.randint(0, len(self.dev_card_deck) - 1)
            return self.dev_card_deck.pop(result)
        else:
            self.time_passes()

    # returns a card from the indoor tile deck and removes it from the deck, returns false if no more cards exist
    def draw_indoor_tile_card(self):
        if len(self.indoor_tile_deck) > 0:
            result = random.randint(0, len(self.indoor_tile_deck) - 1)
            return self.indoor_tile_deck.pop(result)
        else:
            return False

    # returns a card from the outdoor tile deck and removes it from the deck, returns false if no more cards exist
    def draw_outdoor_tile_card(self):
        if len(self.outdoor_tile_deck) > 0:
            result = random.randint(0, len(self.outdoor_tile_deck) - 1)
            return self.outdoor_tile_deck.pop(result)
        else:
            return False

    # changes the time
    def time_passes(self):
        self.time = self.time + 100

    def first_move(self):
        print("Welcome to Zombie in my Pocket. Type Help to view your available commands."
              "\n You're standing in the foyer of a house. There a door to the North of you.")
        foyer_tile = Foyer()
        self.current_tiles[foyer_tile] = [10, 10]
