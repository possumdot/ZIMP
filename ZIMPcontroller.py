from cmd import Cmd


class ZIMPcontroller(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "

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
