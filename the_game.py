import json
import pickle
import random
from cmd import Cmd
import os

import devcards.dev_card
from items.item import Item
from player import Player
from devcards.candle_card import CandleCard
from devcards.chainsaw_card import ChainsawCard
from devcards.gasoline_card import GasolineCard
from devcards.golf_club_card import GolfClubCard
from devcards.grisly_femur_card import GrislyFemurCard
from devcards.machete_card import MacheteCard
from devcards.board_with_nails_card import BoardWithNailsCard
from devcards.oil_card import OilCard
from devcards.can_of_soda_card import CanOfSodaCard
from tiles.indoor.bathroom import Bathroom
from tiles.indoor.bedroom import Bedroom
from tiles.indoor.dining_room import DiningRoom
from tiles.indoor.evil_temple import EvilTemple
from tiles.indoor.family_room import FamilyRoom
from tiles.indoor.foyer import Foyer
from tiles.indoor.kitchen import Kitchen
from tiles.indoor.storage import Storage
from tiles.outdoor.garage import Garage
from tiles.outdoor.garden import Garden
from tiles.outdoor.graveyard import Graveyard
from tiles.outdoor.sitting_area import SittingArea
from tiles.outdoor.yard import Yard
from items.candle import Candle
from items.chainsaw import Chainsaw
from items.board_with_nails import BoardWithNails
from items.gasoline import Gasoline
from items.golf_club import GolfClub
from items.grisly_femur import GrislyFemur
from items.machete import Machete
from items.oil import Oil
from items.can_of_soda import CanOfSoda
from database import Database
from game_info import GameInfo


class TheGame(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.game_info = GameInfo()
        self.prompt = ">>> "

    def do_start(self, args):
        """Starts the game, only usable if the game hasn't already started."""
        try:
            if self.is_command_valid("start"):
                self.setup_game()
                self.game_info.game_turn_state = "free"
            else:
                raise ValueError
        except ValueError:
            print("The game is currently in progress. Please type RESTART to start the game again")
            pass

    def do_restart(self, args):
        """Restarts a game in progress, only works if the gam has started"""
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
        """ Set's up a new game with all default values, places everything in to the game_info object
        """
        print("Welcome to Zombie in my Pocket. Type Help to view your available commands."
              "\n You're standing in the foyer of a house. There a door to the North of you.")
        self.game_info = GameInfo()
        self.game_info.current_turn = 1
        self.game_info.player = Player(6, False, 10, 10)
        # place the Foyer card on the table
        foyer_tile = Foyer()
        self.game_info.current_tiles["10 10"] = foyer_tile
        self.game_info.player.move(10, 10)
        # shuffle outdoor and indoor tiles into separate decks
        self.game_info.indoor_tile_deck = self.get_indoor_tile_deck()
        self.game_info.outdoor_tile_deck = self.get_outdoor_tile_deck()
        # shuffle the Dev cards and discard the top 2 cards
        self.game_info.dev_card_deck = self.get_dev_card_deck()
        self.shuffle_dev_card_deck()
        self.game_info.game_turn_state = "free"
        self.update_prompt()

    def do_move(self, args):
        """move [direction]
        Enter a direction to move in, N E W S or North East West South. Case doesn't matter."""
        if self.is_command_valid("move"):
            args = self.parse_args(args)
            self.check_valid_move(args[0])
            self.update_prompt()
        elif self.game_info.game_turn_state == "zombies":
            print("You can't move right now, there are zombies to fight")

    def check_valid_move(self, direction):
        """ Takes a direction as an argument, if no direction is given, prompts the user for a direction.
            Direction is then checked to see if it's valid and if it is, passes the direction on to the move method
        """
        if direction == "":
            direction = input("Please enter a direction (NEWS or North East West South)")
        direction = direction.lower()
        valid_directions = ["n", "north", "e", "east", "w", "west", "s", "south"]
        if direction in valid_directions:
            # check the tile_dictionary for x,y coordinates as tuple,
            coords = f"{self.get_player_x()} {self.get_player_y()}"
            # assign the tile object to a variable
            current_tile = self.game_info.current_tiles[coords]
            # check the objects exit in direction you want to move
            if current_tile.exits[direction[0][0]]:
                # if true then move character
                self.move_player(direction[0][0])
                # check if tile already exists in dictionary
                if (self.get_player_x(), self.get_player_y()) not in self.game_info.current_tiles:
                    self.add_new_tile_card(coords)
                self.resolve_dev_card()
            else:
                print("There is no exit here")

    def move_player(self, direction):
        """ Takes a direction as an argument and attempts to move the player to the new coordinates
        """
        try:
            match direction:
                case "n":
                    self.game_info.player.move(self.get_player_x(), self.get_player_y() - 1)
                case "e":
                    self.game_info.player.move(self.get_player_x() + 1, self.get_player_y())
                case "w":
                    self.game_info.player.move(self.get_player_x() - 1, self.get_player_y())
                case "s":
                    self.game_info.player.move(self.get_player_x(), self.get_player_y() + 1)
        except ValueError:
            print("Something has gone wrong in the move player method")

    def get_player_x(self):
        return self.game_info.player.x

    def get_player_y(self):
        return self.game_info.player.y

    def get_dev_card_deck(self):
        """ Creates instances of the dev_card objects and then places them all in a list
            that the game can then pull from later
        """
        candle_card = CandleCard()
        chainsaw_card = ChainsawCard()
        gasoline_card = GasolineCard()
        golfclub_card = GolfClubCard()
        grislyfemur_card = GrislyFemurCard()
        machete_card = MacheteCard()
        nailboard_card = BoardWithNailsCard()
        oil_card = OilCard()
        soda_card = CanOfSodaCard()
        return [candle_card, chainsaw_card, gasoline_card, golfclub_card, grislyfemur_card, machete_card,
                nailboard_card, oil_card, soda_card]

    def shuffle_dev_card_deck(self):
        """Removes 2 random cards from the deck"""
        for i in [1, 2]:
            _ = self.draw_dev_card()

    def get_indoor_tile_deck(self):
        """ Creates instances of all the Tile objects that belong inside then places them all
            in a list that the game can then pull from later
        """
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
        """ Creates instances of all the Tile objects that belong outside then places them all
            in a list that the game can then pull from later
        """
        garage_tile = Garage()
        garden_tile = Garden()
        graveyard_tile = Graveyard()
        sitting_area_tile = SittingArea()
        yard1_tile = Yard()
        yard2_tile = Yard()
        yard3_tile = Yard()
        return [garage_tile, garden_tile, graveyard_tile, sitting_area_tile, yard1_tile, yard2_tile, yard3_tile]

    def draw_dev_card(self):
        """ Returns a card and removes it from the active deck, if no more cards exists, time passes
        """
        if len(self.game_info.dev_card_deck) == 0:
            self.game_info.dev_card_deck = self.get_dev_card_deck()
            self.shuffle_dev_card_deck()
            self.time_passes()
        result = random.randint(0, len(self.game_info.dev_card_deck) - 1)
        return self.game_info.dev_card_deck.pop(result)

    def do_load(self, args):
        """
        load [source] [savename]
        [source] is either [file] or [database]
        [savename] is the name of the saved game or filename
        """
        args = self.parse_args(args)
        source = args[0]
        try:
            if source == "":
                source = input("Where do you want to load your save from? file/database ").lower()
                if source not in ["file", "database"]:
                    raise ValueError("You need to enter either file or database. Please try again")
            if len(args) == 1:
                save_name = input("What is the name of the save file? ")
            elif len(args) == 2:
                save_name = args[1]
            if source == "file":
                self.save_to_file(save_name)
            if source == "database":
                self.load_from_database(save_name)
        except ValueError as error:
            print(error)
        except FileNotFoundError:
            print("The file name you specified does not exist")

    def load_from_file(self, filename):
        """ Takes a file save name that exists and then reads the file contents as json.
            It then reads through all lines and handles keys in different ways, dynamically rebuilding the game into
            the saved state
        """
        try:
            file = open(filename, "r")
            file_contents = json.load(file)
            print("loading from file...")
            self.game_info = GameInfo()
            for key, value in file_contents.items():
                match key:
                    case "player":
                        self.game_info.player = Player(value["health"],
                                                       value["has_totem"],
                                                       value["x"],
                                                       value["y"]
                                                       )
                        self.game_info.player.items = value["items"]
                    case "dev_card_deck":
                        for card in file_contents[key]:
                            new_card = globals()[f'{card["card_item"]["name"].replace(" ", "")}Card']()
                            self.game_info.dev_card_deck.append(new_card)
                    case "indoor_tile_deck":
                        for tile in file_contents[key]:
                            new_tile = globals()[f'{tile["name"].replace(" ", "")}']()
                            self.game_info.indoor_tile_deck.append(new_tile)
                    case "outdoor_tile_deck":
                        for tile in file_contents[key]:
                            new_tile = globals()[f'{tile["name"].replace(" ", "")}']()
                            self.game_info.outdoor_tile_deck.append(new_tile)
                    case "current_tiles":
                        for key, value in file_contents[key].items():
                            new_tile = globals()[f'{value["name"].replace(" ", "")}']()
                            self.game_info.current_tiles[key] = new_tile
                    case "item_on_ground":
                        if value is not None:
                            the_item = globals()[f'{value["name"].replace(" ", "")}']()
                            self.game_info.item_on_ground = the_item
                    case _:
                        setattr(self.game_info, key, value)
        except Exception:
            print("The file has corrupted, please start a new game")
        self.update_prompt()

    def load_from_database(self, save_name):
        """ Takes a save name which is a key in the database and then unpickles the returned value from the database
        """
        database = Database()
        print("loading from database...")
        self.game_info = pickle.loads(database.get_save_game_from_table(save_name)[0][0])
        self.update_prompt()

    def do_save(self, args):
        """
        save [destination] [savename]
        [destination] is either [file] or [database]
        [savename] is the name of the saved game or filename
        """
        args = self.parse_args(args)
        destination = args[0]
        try:
            if destination == "":
                destination = input("Where do you want to save your file to? file/database ").lower()
                if destination not in ["file", "database"]:
                    raise ValueError("You need to enter either file or database. Please try again")
            if len(args) == 1:
                save_name = input("What is the name of the save file? ")
            elif len(args) == 2:
                save_name = args[1]
            if destination == "file":
                self.save_to_file(save_name)
            if destination == "database":
                self.save_to_database(save_name)
        except ValueError as error:
            print(error)

    def save_to_file(self, save_name):
        """ Saves a jsonified version of the game_info object to a file with save_name as the filename
        """
        try:
            print("saving")
            with open(save_name, "x") as file:
                file.write(str(self.game_info))
        except FileExistsError:
            print("This file already exists, please try again with a different name")

    def save_to_database(self, save_name):
        """ Saves a pickled copy of the game_info object to a database with save_name as the key
        """
        database = Database()
        database.create_tables()
        save_game_to_add = pickle.dumps(self.game_info)
        save_name = save_name
        save_info = (save_name, save_game_to_add)
        database.add_save_game_to_table(save_info)

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
        """ Returns a dictionary of actions from a dev_card that correspond to the ingame time
        """
        try:
            match self.game_info.time:
                case 2100:
                    return dev_card.nine_info
                case 2200:
                    return dev_card.ten_info
                case 2300:
                    return dev_card.eleven_info
        except AttributeError:
            print("Something has gone wrong in get_dev_card_info")

    def dev_card_event_action(self, dev_card_action):
        """ Gets called if the dev_cards action is an event
                 Applies a health change to the player based on what the card has at the time
        """
        try:
            print(dev_card_action["description"])
            if dev_card_action["health_change"] > 0:
                print(f"You gain {dev_card_action['health_change']} health")
                self.game_info.player.heal(dev_card_action["health_change"])
            elif dev_card_action["health_change"] < 0:
                print(f"You lose {dev_card_action['health_change']} health")
                self.game_info.player.heal(dev_card_action["health_change"])
            else:
                print("Nothing else happens")
        except AttributeError:
            print("Something has gone wrong with the dev card event action")

    def dev_card_zombies_action(self, dev_card_action):
        """ Gets called if the dev_cards action is a zombies event
            Let's the player know there are zombies to fight and sets the count from the card into the game_info object
        """
        try:
            print(dev_card_action["description"])
            print("You can stand and FIGHT or RUN")
            self.game_info.game_turn_state = "zombies"
            self.game_info.zombie_count = dev_card_action["zombies"]
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
                if args[0] == "item1" or args[0] == "item2" or args[0] in self.game_info.player.items:
                    print(f"You attack with {self.game_info.player.items[args[0]]}")
                    self.resolve_combat(self.game_info.player.items[args[0]])
            else:
                self.resolve_combat()
        else:
            print("There is nothing to fight")

    def resolve_combat(self, item=None):
        """ Resolves the combat between the player and the amount of zombies in the room.
            Can take an item as an argument and will use the attack_modifier of that weapon if given
        """
        if item is not None:
            damage = self.game_info.zombie_count - (self.game_info.player.attack + item.attack_modifier)
        else:
            damage = self.game_info.zombie_count - self.game_info.player.attack

        if damage >= 4:
            self.game_info.player.take_damage(4)
            print(f"You fight off the zombies and take 4 damage")
        elif damage <= 0:
            print("You fight off the zombies and take no damage")
        else:
            self.game_info.player.take_damage(damage)
            print(f"You fight off the zombies and take {damage} damage")
        self.game_info.zombie_count = 0
        self.game_info.game_turn_state = "free"
        self.update_prompt()

    def dev_card_item_action(self, dev_card):
        """ Gets called if the dev_cards action is an item
            Places the item on the ground and gives the player the option to pick it up
        """
        print(f"There is a {dev_card.card_item.name} lying on the ground")
        self.game_info.item_on_ground = dev_card.card_item

    def do_pickup(self, args):
        """pickup [itemslot]
        Picks up the item off the ground and places it into the item slot specified.
        Valid item slots are [item1] or [item2].
        If the current slot isn't empty, swaps the item in that slot with the one on the ground."""
        args = self.parse_args(args)
        if self.is_command_valid("pickup"):
            if self.game_info.item_on_ground is not None and args[0] in ["item1", "item2"]:
                self.swap_item(args[0])
            self.update_prompt()

    def swap_item(self, itemslot):
        """ Swaps an item that's on the ground with a spcified one in the players item slots
        """
        item_on_ground = self.game_info.item_on_ground
        player_item = self.game_info.player.items[itemslot]
        self.game_info.item_on_ground = player_item
        self.game_info.player.items[itemslot] = item_on_ground

    def draw_indoor_tile_card(self):
        """  returns a card from the indoor tile deck and removes it from the deck, returns false if no more cards exist
        """
        if len(self.game_info.indoor_tile_deck) > 0:
            result = random.randint(0, len(self.game_info.indoor_tile_deck) - 1)
            return self.game_info.indoor_tile_deck.pop(result)
        else:
            return False

    def draw_outdoor_tile_card(self):
        """ returns a card from the outdoor tile deck and removes it from the deck, returns false if no more cards exist
        """
        if len(self.game_info.outdoor_tile_deck) > 0:
            result = random.randint(0, len(self.game_info.outdoor_tile_deck) - 1)
            return self.game_info.outdoor_tile_deck.pop(result)
        else:
            return False

    def time_passes(self):
        """ changes the time by an hour
        """
        self.game_info.time = self.game_info.time + 100

    def add_new_tile_card(self, coords):
        new_card = None
        if self.game_info.current_tiles[coords].indoor:
            new_card = self.draw_indoor_tile_card()
        else:
            new_card = self.draw_outdoor_tile_card()
        # need to be able to rotate once placed
        self.game_info.current_tiles[f"{self.get_player_x()} {self.get_player_y()}"] = new_card

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
        """ Updates the cmd prompt to show the map and current player stats
        """
        self.prompt = self.prompt_builder()

    def prompt_builder(self):
        """ Builds the prompt for the player with conditionals in place for zombies and items on the ground
        """
        self.get_map()
        the_string = (f"Health: {self.game_info.player.health} \n"
                      f"Item1: {self.game_info.player.get_item1()} \n"
                      f"Item2: {self.game_info.player.get_item2()} \n")
        if self.game_info.zombie_count > 0:
            the_string = the_string + f"Zombies: {self.game_info.zombie_count} \n"
        if self.game_info.item_on_ground is not None:
            the_string = the_string + f"Item on Ground: {self.game_info.item_on_ground.name} \n"
        the_string = the_string + ">>>"
        return the_string

    def is_command_valid(self, command):
        """ Checks to see if a command is valid based on the current game state
        """
        # clears the cmd but only if open through Windows cmd prompt
        os.system('cls')
        if self.game_info.game_turn_state is not None:
            match command:
                case "start":
                    if self.game_info.game_turn_state is None:
                        return True
                    else:
                        return False
                case "fight":
                    if self.game_info.game_turn_state == "zombies":
                        return True
                    else:
                        return False
                case "run":
                    if self.game_info.game_turn_state == "zombies":
                        return True
                    else:
                        return False
                case "cower":
                    pass
                case "move":
                    if self.game_info.game_turn_state == "free":
                        return True
                    else:
                        return False
                case "restart":
                    if self.game_info.game_turn_state is None:
                        return False
                    else:
                        return True
                case "pickup":
                    if self.game_info.game_turn_state == "free":
                        return True
                    else:
                        return False
                case _:
                    pass
                    # throw exception
        elif self.game_info.game_turn_state is None and command == "start":
            return True
        else:
            print("The game hasn't started yet.\n"
                  "Please type Start to start a new game, or Load [filename] to load a game from file")
            return False

    def get_map(self):
        """ Builds a 3 x 3 unicode map with the player in the middle of the rooms currently placed.
            Shows doors and walls. Does not currently work correctly with outdoor tiles
        """
        x_coord = self.game_info.player.x
        y_coord = self.game_info.player.y
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
                if self.game_info.current_tiles.get(f"{x} {y}") is None:
                    line_1 = line_1 + "   "
                    line_2 = line_2 + "   "
                    line_3 = line_3 + "   "
                else:
                    north_exit = " "
                    east_exit = " "
                    west_exit = " "
                    south_exit = " "
                    player_present = " "
                    if not self.game_info.current_tiles[f"{x} {y}"].exits["n"]:
                        north_exit = "━"
                    if not self.game_info.current_tiles[f"{x} {y}"].exits["e"]:
                        east_exit = "┃"
                    if not self.game_info.current_tiles[f"{x} {y}"].exits["w"]:
                        west_exit = "┃"
                    if not self.game_info.current_tiles[f"{x} {y}"].exits["s"]:
                        south_exit = "━"
                    if self.get_player_x() == x and self.get_player_y() == y:
                        player_present = "X"
                    line_1 = line_1 + f"┏{north_exit}┓"
                    line_2 = line_2 + f"{west_exit}{player_present}{east_exit}"
                    line_3 = line_3 + f"┗{south_exit}┛"
            print(line_1)
            print(line_2)
            print(line_3)