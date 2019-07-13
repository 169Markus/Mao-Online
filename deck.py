from random import shuffle
from card import Card


class Deck(object):
    def __init__(self, standard=True):
        self.cards = []
        self.size = 0

        if standard:
            self.create_standard()

    def shuffle(self):
        shuffle(self.cards)

    def add(self, card: Card):
        self.cards.append(card)
        self.size += 1

    def draw(self, num=1):
        """
        Draws as many cards as you can, up to `num`.

        :param num: the number of cards to draw
        :return: a list of `num` (or fewer!) cards, to a minimum of zero.
        """
        drawn_cards = []

        for i in range(min(num, self.size)):
            drawn_cards.append(self.cards.pop())

        return drawn_cards

    def remove(self, card: Card):
        self.cards.remove(card)


    def create_standard(self, jokers=False):
        """create all the cards in a standard deck"""
        vals = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['♠', '♡', '♢', '♣']

        for v in vals:
            for s in suits:
                self.add(Card(v, s))

        if jokers:
            self.add(Card('BJ', 'J'))
            self.add(Card('RJ', 'J'))

        self.shuffle()
