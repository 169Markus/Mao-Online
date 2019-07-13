from random import shuffle
from card import Card


class Deck(object):
    def __init__(self):
        self.cards = []
        self.size = 0

    def shuffle(self):
        shuffle(self.cards)

    def add(self, card: Card):
        self.cards.append(card)
        self.size += 1

    def draw(self):
        if self.size >= 1:
            self.size -= 1
            return self.cards.pop()
        else:
            return None

    def remove(self, card: Card):
        self.cards.remove(card)
