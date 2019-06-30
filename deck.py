class deck():
    def __init__(self, type):
        self.cards = []
        self.type = type


class draw_deck(deck):
    def __init__(self):
        self.size = 52

class play_deck(deck):
    def __init__(self):
        self.size = 0
