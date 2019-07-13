from deck import Deck
import random


class Game(object):
    def __init__(self, players):
        self.over = False
        self.rule_book = None
        self.draw_deck = Deck(prefilled=True)
        self.discard_deck = Deck()
        self.players = players
        self.num_players = len(players)
        self.history = []
        self.play_order = []
        self.whose_turn = random.randint(self.num_players)
        self.next_turn = lambda x: (x + 1) % len(players)  # can be overridden by rules

        self.deal()

    def deal(self):
        for player in self.players:
            player.hand = self.draw_deck.draw(5)

    def turn(self):
        pass

