import json
from cmd import Cmd

from models.devcard import DevCard
from models.item import Item
from models.player import Player
from models.tile import Tile


class ZIMPcontroller(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "

    def do_test(self, args):
        tile = Tile()
        new_item = Item(name="Chainsaw", description="Chainsaw does chainsaw", attack_modifier=3, health_modifier=0,
                        combineable=False, combineable_items=[], has_uses=True, uses_remaining=3, expires_on_use=False)
        new_dev_card = DevCard(new_item, {"action": "zombies", "description": "nine desc", "zombies": 3, "health_change": None},
                               {"action": "item", "description": "ten desc", "zombies": None, "health_change": None},
                               {"action": "event", "description": "eleven desc", "zombies": None, "health_change": 1})
        #file = open("testdev.file", "x")
        #file.write(str(new_dev_card))
        #file.close()
        file = open("testdev.file", "r")
        file_contents = json.load(file)
        new_dev_card = DevCard()
        print(new_dev_card)
        for key, value in file_contents.items():
            setattr(new_dev_card, key, value)
        print(new_dev_card)

    def do_start(self, args):
        pass

    def do_restart(self, args):
        pass

    def do_quit(self, args):
        pass

    def do_load(self, args):
        pass

    def do_save(self, args):
        pass

    def do_rules(self, args):
        pass

    def do_move(self, args):
        pass

    # might not be needed considering a room might fit just fine
    def do_rotate(self, args):
        pass

    def do_fight(self, args):
        pass

    def do_cower(self, args):
        pass

    def do_use(self, args):
        """uses an item if you have it on your character"""
        pass

    def do_pickup(self, args):
        """picks an item off the ground and replaces it with the item in the arg, could also be item slot"""
        pass

    def do_burytotem(self, args):
        pass
