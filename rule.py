from deck import Deck
from game import Game
from card import Card
from play import Play
from typing import List


class Rule(object):
    """
    A `Rule` consists of three parts:

        * a check of legality [ex. can play any 9 after any 6];
        * a global effect [ex. reversing turn order]; and
        * an effect on a sequence of players [ex. next player draws two cards].


    Most often, only one or two of the three parts will be implemented.

    The effects are always triggered by 'playing a card'--in particular,
    ending your turn after playing a card, or playing a card out of turn.
    """

    def __init__(self, legality, global_effect, player_effects):
        self.legality = legality
        self.global_effect = global_effect
        self.player_effects = player_effects


class RuleBook(object):
    """Stores all rules"""

    def __init__(self):
        self.rules: List[Rule] = []

        # Rule of least precedence must include true and false cases
        def same_suit(play: Play, game: Game):
            return play.cards[0].suit == game.discard_deck.top.suit

        def same_value(play: Play, game: Game):
            if play.cards[0].value == game.discard_deck.top.value:
                return True

        def one_card(play: Play, game: Game):
            if len(play.cards) > 1:
                return False

        def reverse_play(play: Play, game: Game):
            if play.cards[0].value == 'Q':


        def skip(play: Play, game: Game):
            if play.cards[0].value == '8':


        def draw_two_thanks(play: Play, game: Game):
            if play.cards[0].value == '7':
                # require "have a nice day" on current player,
                # draw two and "thank you" on next player


        self.add_rule(Rule(same_suit, None, None))
        self.add_rule(Rule(same_value, None, None))
        self.add_rule(Rule(one_card, None, None))
        self.add_rule(Rule(None, reverse_play, None))
        self.add_rule(Rule(None, None, skip))
        self.add_rule(Rule(None, None, draw_two_thanks))

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def check_played_card(self, play: Play, game: Game):  # Checks if played card is legal
        i = len(self.rules) - 1
        while self.rules[i].legality(play, game) is None:
            i -= 1
        return self.rules[i].legality(play, game)
        # we'd better not have an index out of bounds, or else the starting rules are broken
