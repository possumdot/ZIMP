import json
import pickle
import random
from cmd import Cmd
import os

from Player import Player
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
from database import Database


class TheGame(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.player = None
        self.prompt = ">>> "
        self.time = 2100
        self.dev_card_deck = []
        self.dev_card_deck_strings = []
        self.indoor_tile_deck = []
        self.indoor_tile_deck_strings = []
        self.outdoor_tile_deck = []
        self.outdoor_tile_deck_strings = []
        self.current_tiles = {}
        self.current_turn = 0
        self.game_turn_state = None
        self.zombie_count = 0
        self.item_on_ground = None

    def do_start(self, args):
        """Starts the game, only usable if the game hasn't already started."""
        try:
            if self.is_command_valid("start"):
                self.setup_game()
                self.game_turn_state = "free"
            else:
                raise ValueError
        except ValueError:
            print("The game is currently in progress. Please type RESTART to start the game again")
            pass

    def do_restart(self, args):
        """Restarts a game in progress"""
        try:
            if self.is_command_valid("restart"):
                confirm_restart = input("Are you sure you want to restart? Y/N\n"
                                        "").lower()[0]
                if confirm_restart == "y":
                    self.setup_game()
                elif confirm_restart == "n":
                    pass
                else:
                    print("You didn't type YES or No. The game will resume")
            else:
                raise ValueError
        except ValueError:
            print("The game hasn't started yet, please type START to start the game or LOAD [filename] to load a saved"
                  " game")
            pass

    def setup_game(self):
        print("Welcome to Zombie in my Pocket. Type Help to view your available commands."
              "\n You're standing in the foyer of a house. There a door to the North of you.")
        self.current_turn = 1
        self.player = Player()
        # place the Foyer card on the table
        foyer_tile = Foyer()
        self.current_tiles[(10, 10)] = foyer_tile
        self.player.move(10, 10)
        # shuffle Outdoor and Indoor tiles into separate decks
        self.indoor_tile_deck = self.get_indoor_tile_deck()
        self.outdoor_tile_deck = self.get_outdoor_tile_deck()
        # shuffle the Dev cards and discard the top 2 cards
        self.dev_card_deck = self.get_dev_card_deck()
        self.shuffle_dev_card_deck()

    def do_move(self, args):
        """move [direction]
        Enter a direction to move in, N E W S or North East West South. Case doesn\'t matter."""
        try:
            if self.is_command_valid("move"):
                args = self.parse_args(args)
                self.check_valid_move(args[0])
                self.update_prompt()
            elif self.game_turn_state == "zombies":
                print("You can't move right now, there are zombies to fight")
        except:
            print("Something has gone wrong in the do_move method")

    def check_valid_move(self, direction):
        if direction == "":
            direction = input("Please enter a direction (NEWS or North East West South)")
        direction = direction.lower()
        valid_directions = ["n", "north", "e", "east", "w", "west", "s", "south"]
        if direction in valid_directions:
            # check the tile_dictionary for x,y coordinates as tuple,
            coords = (self.get_player_x(), self.get_player_y())
            # assign the tile object to a variable
            current_tile = self.current_tiles[coords]
            # check the objects exit in direction you want to move
            if current_tile.exits[direction[0][0]]:
                # if true then move character
                self.move_player(direction[0][0])
                # check if tile already exists in dictionary
                if (self.get_player_x(), self.get_player_y()) not in self.current_tiles:
                    self.add_new_tile_card(coords)
                self.resolve_dev_card()
            else:
                print("There is no exit here")

    def move_player(self, direction):
        try:
            match direction:
                case "n":
                    self.player.move(self.get_player_x(), self.get_player_y() - 1)
                case "e":
                    self.player.move(self.get_player_x() + 1, self.get_player_y())
                case "w":
                    self.player.move(self.get_player_x() - 1, self.get_player_y())
                case "s":
                    self.player.move(self.get_player_x(), self.get_player_y() + 1)
        except ValueError:
            print("Something has gone wrong in the move player method")

    def get_player_x(self):
        return self.player.x

    def get_player_y(self):
        return self.player.y

    def get_dev_card_deck(self):
        candle_card = CandleCard()
        chainsaw_card = ChainsawCard()
        gasoline_card = GasolineCard()
        golfclub_card = GolfClubCard()
        grislyfemur_card = GrislyFemurCard()
        machete_card = MacheteCard()
        nailboard_card = NailBoardCard()
        oil_card = OilCard()
        soda_card = SodaCard()
        return [candle_card, chainsaw_card, gasoline_card, golfclub_card, grislyfemur_card, machete_card,
                nailboard_card, oil_card, soda_card]

    def shuffle_dev_card_deck(self):
        """Removes 2 random cards from the deck"""
        for i in [1, 2]:
            _ = self.draw_dev_card()

    def get_indoor_tile_deck(self):
        bathroom_tile = Bathroom()
        bedroom_tile = Bedroom()
        dining_room_tile = DiningRoom()
        evil_temple_tile = EvilTemple()
        family_room_tile = FamilyRoom()
        kitchen_tile = Kitchen()
        storage = Storage()
        return [bathroom_tile, bedroom_tile, dining_room_tile, evil_temple_tile, family_room_tile, kitchen_tile,
                storage]

    def get_outdoor_tile_deck(self):
        garage_tile = Garage()
        garden_tile = Garden()
        graveyard_tile = Graveyard()
        sitting_area_tile = SittingArea()
        yard1_tile = Yard()
        yard2_tile = Yard()
        yard3_tile = Yard()
        return [garage_tile, garden_tile, graveyard_tile, sitting_area_tile, yard1_tile, yard2_tile, yard3_tile]

    # returns a card and removes it from the active deck, if no more cards exists, time passes
    def draw_dev_card(self):
        if len(self.dev_card_deck) == 0:
            self.dev_card_deck = self.get_dev_card_deck()
            self.shuffle_dev_card_deck()
            self.time_passes()
        result = random.randint(0, len(self.dev_card_deck) - 1)
        return self.dev_card_deck.pop(result)

    def do_load(self, args):
        """
        load [source] [savename]
        [source] is either [file] or [database]
        [savename] is the name of the saved game or filename
        """
        args = self.parse_args(args)
        source = args[0]
        if source == "":
            source = input("Where do you want to load your save from? file/database ").lower()
        if len(args) == 1:
            savename = input("What is the name of the save file? ")
        else:
            savename = args[1]

    #            self.load_from_file(savename)
    #        if source == "file":
    #        elif source == "database":
    #            self.load_from_database(savename)

    #    def load_from_file(self, filename):

    #    def load_from_database(self, savename):

    def do_save(self, args):
        """
        save [source] [savename]
        [source] is either [file] or [database]
        [savename] is the name of the saved game or filename
        """
        args = self.parse_args(args)
        source = args[0]
        destination = args[0]
        if source == "":
            source = input("Where do you want to load your save from? file/database ").lower()
        if len(args) == 1:
            savename = input("What is the name of the save file? ")
        else:
            savename = args[1]
        if destination == "file":
            self.save_to_file(savename)

    def save_to_file(self, savename):
        print("saving")
        json_data = {"player": json.dumps(self.player.get_json_elements()),
                     "time": self.time,
                     "dev_card_deck": self.dev_card_deck,
                     "indoor_tile_deck": self.indoor_tile_deck,
                     "outdoor_tile_deck": self.outdoor_tile_deck,
                     "current_tiles": self.current_tiles,
                     "current_turn": self.current_turn,
                     "game_state_turn": self.game_turn_state,
                     "zombie_count": self.zombie_count,
                     "item_on_ground": self.item_on_ground,
                     }
        with open(savename, "x") as file:
            json.dump(json_data, file)

    def resolve_dev_card(self):
        dev_card_action = self.get_dev_card_info(self.draw_dev_card())
        try:
            match dev_card_action["action"]:
                case "event":
                    self.dev_card_event_action(dev_card_action)
                case "zombies":
                    self.dev_card_zombies_action(dev_card_action)
                case "item":
                    # draws another dev card to find the item
                    self.dev_card_item_action(self.draw_dev_card())
        except ValueError:
            print("Something has gone wrong with the resolve_dev_card method")

    # Get the info dict from the DevCard relating to the current in-game time
    def get_dev_card_info(self, dev_card):
        try:
            match self.time:
                case 2100:
                    return dev_card.nine_info
                case 2200:
                    return dev_card.ten_info
                case 2300:
                    return dev_card.eleven_info
        except AttributeError:
            print("Something has gone wrong in get_dev_card_info")

#    def do_database(self, args):
#        database = Database()
#        database.create_tables()
#        item_to_add = pickle.dumps(ChainsawCard())
#        print(type(item_to_add))
#        database.add_item_to_table(["Chainsaw", item_to_add])
#        print(pickle.loads(database.get_item_from_table(["Chainsaw"])[1]))

    def dev_card_event_action(self, dev_card_action):
        try:
            print(dev_card_action["description"])
            if dev_card_action["health_change"] > 0:
                print(f"You gain {dev_card_action['health_change']} health")
                self.player.heal(dev_card_action["health_change"])
            elif dev_card_action["health_change"] < 0:
                print(f"You lose {dev_card_action['health_change']} health")
                self.player.heal(dev_card_action["health_change"])
            else:
                print("Nothing else happens")
        except AttributeError:
            print("Something has gone wrong with the dev card event action")

    def dev_card_zombies_action(self, dev_card_action):
        try:
            print(dev_card_action["description"])
            print("You can stand and FIGHT or RUN")
            self.game_turn_state = "zombies"
            self.zombie_count = dev_card_action["zombies"]
        except KeyError:
            print("No Key found in dev card zombies action method")

    def do_fight(self, args):
        """Fight [item1] [item2]
        Only usable if there are zombies to fight. [item1] and [item2] are optional.
        [item1] is the weapon you want your character to use.
        [item2] is an item that can combine with [item1] for a special combat effect."""
        if self.is_command_valid("fight"):
            args = self.parse_args(args)
            if len(args) == 1 and args[0] != '':
                if args[0] == "item1" or args[0] == "item2" or args[0] in self.player.get_items():
                    print(f"You attack with {self.player.items[args[0]]}")
                    self.resolve_combat(self.player.items[args[0]])
            else:
                self.resolve_combat()
        else:
            print("There is nothing to fight")

    def resolve_combat(self, item=None):
        # calculating damage to apply to player
        if item is not None:
            damage = self.zombie_count - (self.player.get_attack() + item.attack_modifier)
        else:
            damage = self.zombie_count - self.player.get_attack()

        if damage >= 4:
            self.player.take_damage(4)
            print(f"You fight off the zombies and take 4 damage")
        elif damage <= 0:
            print("You fight off the zombies and take no damage")
        else:
            self.player.take_damage(damage)
            print(f"You fight off the zombies and take {damage} damage")
        self.zombie_count = 0
        self.game_turn_state = "free"
        self.update_prompt()

    def dev_card_item_action(self, dev_card):
        print(f"There is a {dev_card.card_item.name} lying on the ground")
        self.item_on_ground = dev_card.card_item

    def do_pickup(self, args):
        """pickup [itemslot]
        Picks up the item off the ground and places it into the item slot specified.
        Valid item slots are [item1] or [item2].
        If the current slot isn't empty, swaps the item in that slot with the one on the ground."""
        args = self.parse_args(args)
        if self.is_command_valid("pickup"):
            if self.item_on_ground is not None and args[0] in ["item1", "item2"]:
                self.swap_item(args[0])
            self.update_prompt()

    def swap_item(self, itemslot):
        item_on_ground = self.item_on_ground
        player_item = self.player.items[itemslot]
        self.item_on_ground = player_item
        self.player.items[itemslot] = item_on_ground

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

    def add_new_tile_card(self, coords):
        is_indoor_card = None
        new_card = None
        if self.current_tiles[coords].indoor:
            new_card = self.draw_indoor_tile_card()
        else:
            new_card = self.draw_outdoor_tile_card()
        # need to be able to rotate once placed
        self.current_tiles[(self.get_player_x(), self.get_player_y())] = new_card

    #    needs to be implemented
    #    def rotate_new_card(self, ):

    def parse_args(self, args):
        """This is sorta clunky but for every command that usually requires an argument, this splits the arguments given
        into a list that can be used by each command."""
        if args == "":
            return [""]
        else:
            return args.lower().split()

    def update_prompt(self):
        self.prompt = self.prompt_builder()

    def prompt_builder(self):
        self.get_map()
        the_string = (f"Health: {self.player.get_health()} \n"
                      f"Item1: {self.player.get_item1()} \n"
                      f"Item2: {self.player.get_item2()} \n")
        if self.zombie_count > 0:
            the_string = the_string + f"Zombies: {self.zombie_count} \n"
        if self.item_on_ground is not None:
            the_string = the_string + f"Item on Ground: {self.item_on_ground.name} \n"
        the_string = the_string + ">>>"
        return the_string

    def is_command_valid(self, command):
        os.system('cls')
        if self.game_turn_state is not None:
            match command:
                case "start":
                    if self.game_turn_state is None:
                        return True
                    else:
                        return False
                case "fight":
                    if self.game_turn_state == "zombies":
                        return True
                    else:
                        return False
                case "run":
                    if self.game_turn_state == "zombies":
                        return True
                    else:
                        return False
                case "cower":
                    pass
                case "move":
                    if self.game_turn_state == "free":
                        return True
                    else:
                        return False
                case "restart":
                    if self.game_turn_state is None:
                        return False
                    else:
                        return True
                case "pickup":
                    if self.game_turn_state == "free":
                        return True
                    else:
                        return False
                case _:
                    pass
                    # throw exception
        elif self.game_turn_state is None and command == "start":
            return True
        else:
            print("The game hasn't started yet.\n"
                  "Please type Start to start a new game, or Load [filename] to load a game from file")
            return False

    def get_map(self):
        map_dict = {}
        x_coord = self.player.x
        y_coord = self.player.y
        count = 0
        line_1 = ""
        line_2 = ""
        line_3 = ""
        for y in range(y_coord - 2, y_coord + 3):
            count += 1
            line_1 = ""
            line_2 = ""
            line_3 = ""
            for x in range(x_coord - 2, x_coord + 3):
                if self.current_tiles.get((x, y)) is None:
                    line_1 = line_1 + "   "
                    line_2 = line_2 + "   "
                    line_3 = line_3 + "   "
                else:
                    north_exit = " "
                    east_exit = " "
                    west_exit = " "
                    south_exit = " "
                    player_present = " "
                    if not self.current_tiles[x, y].exits["n"]:
                        north_exit = "━"
                    if not self.current_tiles[x, y].exits["e"]:
                        east_exit = "┃"
                    if not self.current_tiles[x, y].exits["w"]:
                        west_exit = "┃"
                    if not self.current_tiles[x, y].exits["s"]:
                        south_exit = "━"
                    if self.get_player_x() == x and self.get_player_y() == y:
                        player_present = "X"
                    line_1 = line_1 + f"┏{north_exit}┓"
                    line_2 = line_2 + f"{west_exit}{player_present}{east_exit}"
                    line_3 = line_3 + f"┗{south_exit}┛"
            print(line_1)
            print(line_2)
            print(line_3)
