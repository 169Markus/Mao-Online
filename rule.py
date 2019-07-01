class rule_book():
    '''keep track of all the rules'''
    def __init__(self):
        self.rules = []


class rule():
    def __init__(self):
        self.id = 0

    def make_play_legal(self):
        pass

    def make_play_illegal(self):
        pass

    def effect(self):
        pass

    def play_order(self):
        pass

    def penalty(self):
        pass