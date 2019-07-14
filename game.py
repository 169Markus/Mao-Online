from deck import Deck
from player import Player
from typing import List
from rule import *
import random


class Game(object):
    def __init__(self, players: List[Player]):
        self.over = False
        self.rule_book = RuleBook()
        self.draw_deck = Deck(prefilled=True)
        self.discard_deck = Deck()
        self.players: List[Player] = players
        self.num_players = len(players)
        self.history = []
        self.play_order = []
        self.whose_turn = random.randrange(self.num_players)
        self.next_turn = lambda x: (x + 1) % self.num_players  # can be overridden by rules

        self.effects = []  # temporary rules; effects on the next player (such as 7).

        self.deal()

    def deal(self):
        for player in self.players:
            player.hand = self.draw_deck.draw(5)

    def turn(self):
        current_play = Play(self.players[self.whose_turn])

        print("It's %s's turn!" % current_play.player.username)


        # 1. possible mandatory actions first
        #    i.e., check current active effects

        # 2. can draw whenever

        # 3. go through main rules of the game
        #    and see which are triggered

        # First, go through all the main rules of the game
        # (i.e., not temporary ones), and check which of
        # those rules, if any, the player's play had broken.
        # Give appropriate penalties if necessary.
        any_rules_broken = False
        for rule in self.rule_book.rules:
            if not rule.card_obeys_rule(current_play, self):
                print("PENALTY: " + rule.message)
                current_play.player.givePenalty()  # TODO: Implement this method
                any_rules_broken = True

        if any_rules_broken: return  # Restart the turn

        for rule in self.rule_book.rules:
            # get any effect this rule might activate
            rule_effect = rule.get_effect(current_play, self)

            # if there is any effect, add it to the list
            # to affect the next player.
            if rule_effect is not None:
                self.effects.append(rule_effect)


        # clear effects at the end of a turn
        # TODO: Decide if we want to support multi-turn effects
        self.effects = []

        self.whose_turn = self.next_turn(self.whose_turn)
