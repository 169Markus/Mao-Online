class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @property
    def get_value(self):
        return self.value

    @property
    def get_suit(self):
        return self.suit
