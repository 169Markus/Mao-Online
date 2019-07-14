from deck import Deck
from game import Game
from card import Card
from play import Play
from typing import List


class Rule(object):
    def __init__(self, legality, get_effect, message="Invalid play", penalty=1):
        self.legality = legality
        self.get_effect = get_effect
        self.message = message
        self.penalty = penalty

    def card_obeys_rule(self, play: Play, game: Game):
        return self.legality(play, game)


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

        self.add_rule(Rule(same_suit, None, message="Bad Card"))
        self.add_rule(Rule(same_value, None, message="Bad Card"))
        self.add_rule(Rule(one_card, None))

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def check_played_card(self, card, game):  # Checks if played card is legal
        i = len(self.rules) - 1
        while self.rules[i].card_obeys_rule(card, game) is None:
            i -= 1
        return self.rules[i].card_obeys_rule(card, game)
        # we'd better not have an index out of bounds, or else the starting rules are broken
