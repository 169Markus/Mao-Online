from deck import Deck
from player import Player


class Game(object):
    def __init__(self):
        self.state = 'Ongoing'
        self.rule_book = None
        self.draw_deck = Deck()
        self.discard_deck = None
        self.players = None
        self.history = []
        self.play_order = []
        self.turn = []




    def deal(self, players):
        for player in players:
            player.hand = self.draw_deck.draw(5)
