from card import Card
from deck import Deck


def create_standard(jokers=False):
    """create all the cards in a standard deck"""
    vals = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['♠', '♡', '♢', '♣']

    deck = Deck()
    for v in vals:
        for s in suits:
            deck.add(Card(v, s))

    if jokers:
        deck.add(Card('BJ', 'J'))
        deck.add(Card('RJ', 'J'))

    deck.shuffle()
    return deck
