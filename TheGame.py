import random
from cmd import Cmd

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


class TheGame(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.player = None
        self.prompt = ">>> "
        self.time = 2100
        self.dev_card_deck = []
        self.indoor_tile_deck = []
        self.outdoor_tile_deck = []
        self.current_tiles = {}
        self.current_turn = 0
        self.game_state = None
        self.zombie_count = 0
        self.item_on_ground = None

    # def game_loop(self):
    #    # Start player at x = 10, y = 10 in the Lobby
    #    # 1. Choose an exit door into a new room or a room that already existed
    #    # 2. If a new room, draw and place an indoor tile,
    #    self.first_move()
    #    game_command = self.get_game_command()
    #    while game_command[0].lower() != "exit":
    #        # if time is 2400, game time has run out and the player loses
    #        if self.time != 2400:
    #            match game_command[0].lower():
    #                case "move":
    #                    break
    #                case _:
    #                    print(f"{game_command[0]} is not a valid command, please enter a valid command."
    #                          f" Type Help for a list")
    #        else:
    #            game_command = input("Your time has run out and the zombies win, type Replay to start again, Stats to"
    #                                 "view your stats or Exit to close the game")

    def do_start(self, args):
        """Starts the game, only usable if the game hasn't already started."""
        if self.is_command_valid("start"):
            self.setup_game()
            self.game_state = "free"
        else:
            print("The game is currently in progress. Please type RESTART to start the game again")

    def do_restart(self, args):
        """Restarts a game in progress"""
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
            print("The game hasn't started yet, please type START to start the game or LOAD [filename] to load a saved"
                  " game")

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
        if self.is_command_valid("move"):
            args = self.parse_args(args)
            self.check_valid_move(args[0])
            self.update_prompt()
        else:
            if self.game_state() == "zombies":
                print("You can't move right now, there are zombies to fight")
            elif self.game_state() is None:
                print("The game hasn't started yet.\n"
                      "Please type Start to start a new game, or Load [filename] to load a game from file")

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
        match direction:
            case "n":
                self.player.move(self.get_player_x(), self.get_player_y() - 1)
            case "e":
                self.player.move(self.get_player_x() + 1, self.get_player_y())
            case "w":
                self.player.move(self.get_player_x() - 1, self.get_player_y())
            case "s":
                self.player.move(self.get_player_x(), self.get_player_y() + 1)

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
        if len(self.dev_card_deck) > 0:
            result = random.randint(0, len(self.dev_card_deck) - 1)
            return self.dev_card_deck.pop(result)
        else:
            self.get_dev_card_deck()
            self.shuffle_dev_card_deck()
            self.time_passes()

    def resolve_dev_card(self):
        dev_card_action = self.get_dev_card_info(self.draw_dev_card())
        match dev_card_action["action"]:
            case "event":
                self.dev_card_event_action(dev_card_action)
            case "zombies":
                self.dev_card_zombies_action(dev_card_action)
            case "item":
                self.dev_card_item_action(self.draw_dev_card())
            case _:
                print("Something has gone wrong with the action")

    # Get the info dict from the DevCard relating to the current in-game time
    def get_dev_card_info(self, dev_card):
        match self.time:
            case 2100:
                return dev_card.nine_info
            case 2200:
                return dev_card.ten_info
            case 2300:
                return dev_card.eleven_info
            case _:
                return "Something has gone wrong with the time"

    def dev_card_event_action(self, dev_card_action):
        print(dev_card_action["description"])
        if dev_card_action["health_change"] > 0:
            print(f"You gain {dev_card_action['health_change']} health")
            self.player.heal(dev_card_action["health_change"])
        elif dev_card_action["health_change"] < 0:
            print(f"You lose {dev_card_action['health_change']} health")
            self.player.heal(dev_card_action["health_change"])
        else:
            print("Nothing else happens")

    def dev_card_zombies_action(self, dev_card_action):
        print(dev_card_action["description"])
        print("You can stand and FIGHT or RUN")
        self.game_state = "zombies"
        self.zombie_count = dev_card_action["zombies"]

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
        self.game_state = "free"
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
            return args.split()

    def update_prompt(self):
        self.prompt = (f"Health: {self.player.get_health()} \n"
                       f"Item1: {self.player.get_item1()} \n"
                       f"Item2: {self.player.get_item2()} \n"
                       f">>> ")

    def is_command_valid(self, command):
        match command:
            case "start":
                if self.game_state is None:
                    return True
                else:
                    return False
            case "fight":
                if self.game_state == "zombies":
                    return True
                else:
                    return False
            case "run":
                if self.game_state == "zombies":
                    return True
                else:
                    return False
            case "cower":
                pass
            case "move":
                if self.game_state == "free":
                    return True
                else:
                    return False
            case "restart":
                if self.game_state is None:
                    return False
                else:
                    return True
            case "pickup":
                if self.game_state == "free":
                    return True
                else:
                    return False
            case _:
                print("The game hasn't started yet.\n"
                      "Please type Start to start a new game, or Load [filename] to load a game from file")
