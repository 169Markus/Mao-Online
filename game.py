from deck import Deck
from player import Player
from typing import List
import random


class Game(object):
    def __init__(self, players: List[Player]):
        self.over = False
        self.rule_book = None
        self.draw_deck = Deck(prefilled=True)
        self.discard_deck = Deck()
        self.players = players
        self.num_players = players.__len__()
        self.history = []
        self.play_order = []
        self.whose_turn = random.randrange(self.num_players)
        self.next_turn = lambda x: (x + 1) % self.num_players  # can be overridden by rules

        self.deal()

    def deal(self):
        for player in self.players:
            player.hand = self.draw_deck.draw(5)

    def turn(self):
        print("It's %s's turn!" % self.players[self.whose_turn].username)
        # possible mandatory actions first






        self.whose_turn = self.next_turn(self.whose_turn)


