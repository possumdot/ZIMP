import unittest

from DevCards.DevCard import DevCard
from Items.NailBoard import NailBoard
from TheGame import TheGame
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


class Testing(unittest.TestCase):

    def setUp(self):
        self.the_game = TheGame()

    def test_setup_game_sets_current_turn_to_1(self):
        self.the_game.setup_game()
        self.assertEqual(self.the_game.current_turn, 1)

    def test_setup_game_creates_a_player_object(self):
        self.the_game.setup_game()
        self.assertIsInstance(self.the_game.player, Player)

    def test_setup_game_creates_a_foyer_tile_in_dictionary(self):
        self.the_game.setup_game()
        self.assertIsInstance(self.the_game.current_tiles[(10,10)], Foyer)

    def test_setup_game_moves_the_player_to_correct_coords(self):
        self.the_game.setup_game()
        self.assertEqual(self.the_game.get_player_x(), 10)
        self.assertEqual(self.the_game.get_player_y(), 10)

    def test_setup_game_creates_indoor_tile_deck(self):
        self.the_game.setup_game()
        test_deck = (Bathroom,
                     Bedroom,
                     DiningRoom,
                     EvilTemple,
                     FamilyRoom,
                     Kitchen,
                     Storage
                     )
        for indoor_tile in self.the_game.indoor_tile_deck:
            self.assertIsInstance(indoor_tile, test_deck)

    def test_setup_game_creates_outdoor_tile_deck(self):
        self.the_game.setup_game()
        test_deck = (Garage,
                     Garden,
                     Graveyard,
                     SittingArea,
                     Yard
                     )
        for outdoor_tile in self.the_game.outdoor_tile_deck:
            self.assertIsInstance(outdoor_tile, test_deck)
        self.assertEqual(len(self.the_game.outdoor_tile_deck), 7)

    def test_setup_game_creates_dev_card_deck(self):
        self.the_game.setup_game()
        test_deck = (CandleCard,
                     ChainsawCard,
                     GasolineCard,
                     GolfClubCard,
                     GrislyFemurCard,
                     MacheteCard,
                     NailBoardCard,
                     OilCard,
                     SodaCard
                     )
        for dev_card in self.the_game.dev_card_deck:
            self.assertIsInstance(dev_card, test_deck)

    def test_setup_game_dev_card_deck_has_correct_amount_of_card(self):
        self.the_game.setup_game()
        self.assertEqual(len(self.the_game.dev_card_deck), 7)

    def test_do_move_north_move_player_north(self):
        self.the_game.do_start("")
        dining_room = DiningRoom()
        self.the_game.current_tiles = {(10,10): dining_room}
        self.the_game.do_move("north")
        self.assertEqual(self.the_game.get_player_y(), 9)

    def test_do_move_south_move_player_south(self):
        self.the_game.do_start("")
        dining_room = DiningRoom()
        self.the_game.current_tiles = {(10, 10): dining_room}
        self.the_game.do_move("south")
        self.assertEqual(self.the_game.get_player_y(), 11)

    def test_do_move_north_move_player_east(self):
        self.the_game.do_start("")
        dining_room = DiningRoom()
        self.the_game.current_tiles = {(10, 10): dining_room}
        self.the_game.do_move("east")
        self.assertEqual(self.the_game.get_player_x(), 11)

    def test_do_move_north_move_player_west(self):
        self.the_game.do_start("")
        dining_room = DiningRoom()
        self.the_game.current_tiles = {(10, 10): dining_room}
        self.the_game.do_move("west")
        self.assertEqual(self.the_game.get_player_x(), 9)

    def test_check_valid_move_doesnt_accept_bad_argument(self):
        self.the_game.do_start("")
        dining_room = DiningRoom()
        self.the_game.current_tiles = {(10, 10): dining_room}
        self.assertEqual(self.the_game.check_valid_move("weast"), None)

    def test_check_valid_move_creates_new_tile_on_move_to_empty_location(self):
        self.the_game.do_start("")
        self.the_game.setup_game()
        self.the_game.check_valid_move("n")
        self.assertEqual(len(self.the_game.current_tiles), 2)

    def test_check_valid_move_does_not_create_new_tile_on_move_to_existing_location(self):
        self.the_game.do_start("")
        self.the_game.setup_game()
        dining_room = DiningRoom()
        self.the_game.current_tiles = {(10,10): dining_room, (10,9): dining_room}
        self.the_game.check_valid_move("n")
        self.the_game.check_valid_move("s")
        self.assertEqual(len(self.the_game.current_tiles), 2)

    def test_draw_dev_card_returns_a_card(self):
        self.the_game.setup_game()
        self.assertIsInstance(self.the_game.draw_dev_card(), DevCard)

    def test_draw_dev_card_removes_a_card_from_the_deck(self):
        self.the_game.setup_game()
        self.the_game.draw_dev_card()
        self.assertEqual(len(self.the_game.dev_card_deck), 6)

    def test_move_player_throws_exception_if_direction_is_wrong(self):
        self.the_game.move_player("x")
        self.assertRaises(ValueError)

    def test_get_dev_card_info_throws_exception_if_dev_card_is_wrong(self):
        self.the_game.get_dev_card_info(None)
        self.assertRaises(AttributeError)

    def test_get_dev_card_info_returns_correct_info_nine(self):
        gas_card = GasolineCard()
        expected_result = {"action": "zombies",
                          "description": "4 zombies shamble about",
                          "zombies": 4,
                          "health_change": 0}
        test_result = self.the_game.get_dev_card_info(gas_card)
        self.assertEqual(test_result, expected_result)

    def test_get_dev_card_info_returns_correct_info_ten(self):
        gas_card = GasolineCard()
        self.the_game.time = 2200
        expected_result = {"action": "event",
                         "description": "You sense your impending doom",
                         "zombies": None,
                         "health_change": -1}
        test_result = self.the_game.get_dev_card_info(gas_card)
        self.assertEqual(test_result, expected_result)

    def test_get_dev_card_info_returns_correct_info_eleven(self):
        gas_card = GasolineCard()
        self.the_game.time = 2300
        expected_result = {"action": "item",
                            "description": "You see an Item on the ground",
                            "zombies": None,
                            "health_change": 0}
        test_result = self.the_game.get_dev_card_info(gas_card)
        self.assertEqual(test_result, expected_result)

    def test_get_dev_card_info_throws_exception_if_dev_card_is_wrong(self):
        self.the_game.get_dev_card_info(None)
        self.assertRaises(AttributeError)

    def test_dev_card_event_action_changes_health_positively(self):
        self.the_game.setup_game()
        test_dev_card = {"description": "test", "health_change": 10}
        self.the_game.dev_card_event_action(test_dev_card)
        self.assertEqual(self.the_game.player.health, 16)

    def test_dev_card_event_action_changes_health_negatively(self):
        self.the_game.setup_game()
        test_dev_card = {"description": "test", "health_change": -2}
        self.the_game.dev_card_event_action(test_dev_card)
        self.assertEqual(self.the_game.player.health, 4)

    def test_dev_card_event_action_no_health_change_is_no_health_change(self):
        self.the_game.setup_game()
        test_dev_card = {"description": "test", "health_change": 0}
        self.the_game.dev_card_event_action(test_dev_card)
        self.assertEqual(self.the_game.player.health, 6)

    def test_dev_card_zombies_action_sets_game_state_to_zombies(self):
        self.the_game.setup_game()
        test_card = {"description": "test", "zombies": 3}
        self.the_game.dev_card_zombies_action(test_card)
        self.assertEqual(self.the_game.game_turn_state, "zombies")

    def test_dev_card_zombies_action_sets_zombies_to_correct_amount(self):
        self.the_game.setup_game()
        test_card = {"description": "test", "zombies": 3}
        self.the_game.dev_card_zombies_action(test_card)
        self.assertEqual(self.the_game.zombie_count, 3)

    def test_do_fight_subtracts_correct_amount_of_health_unarmed(self):
        self.the_game.setup_game()
        self.the_game.game_turn_state = "zombies"
        self.the_game.zombie_count = 3
        self.the_game.do_fight("")
        self.assertEqual(self.the_game.player.health, 4)

    def test_do_fight_subtracts_correct_amount_of_health_with_weapon(self):
        self.the_game.setup_game()
        self.the_game.game_turn_state = "zombies"
        self.the_game.zombie_count = 3
        test_weapon = NailBoard()
        self.the_game.player.items["item1"] = test_weapon
        self.the_game.do_fight("NailBoard")
        self.assertEqual(self.the_game.player.health, 4)

    def test_resolve_conflict_limits_damage_taken(self):
        self.the_game.setup_game()
        self.the_game.zombie_count = 10
        self.the_game.resolve_combat()
        self.assertEqual(self.the_game.player.health, 2)

    def test_resolve_conflict_sets_zombies_to_zero(self):
        self.the_game.setup_game()
        self.the_game.zombie_count = 10
        self.the_game.resolve_combat()
        self.assertEqual(self.the_game.zombie_count, 0)

    def test_resolve_conflict_changes_game_turn_state_to_free(self):
        self.the_game.setup_game()
        self.the_game.zombie_count = 10
        self.the_game.resolve_combat()
        self.assertEqual(self.the_game.game_turn_state, "free")

if __name__ == '__main__':
    unittest.main()
