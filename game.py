from deck import Deck
from player import Player


class Game(object):
    def __init__(self, players):
        self.state = 'Ongoing'
        self.rule_book = None
        self.draw_deck = Deck(prefilled=True)
        self.discard_deck = Deck()
        self.players = players
        self.history = []
        self.play_order = []
        self.turn = []

        self.deal(self.players)




    def deal(self, players):
        for player in players:
            player.hand = self.draw_deck.draw(5)
