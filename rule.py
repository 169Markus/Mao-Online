from deck import Deck
from game import Game
from card import Card


class Rule(object):
    def __init__(self, legality, effect):
        self.legality = legality
        self.effect = effect

    def card_obeys_rule(self, card, game):
        return self.legality(card, game)

    def penalty(self, player, number, message):
        pass

class RuleBook(object):
    """Stores all rules"""

    def __init__(self):
        self.rules = []

        # Rule of least precedence must include true and false cases
        def same_suit(card: Card, game: Game):
            return card.suit == game.discard_deck.top.suit

        def same_value(card: Card, game: Game):
            if card.value == game.discard_deck.top.value:
                return True

        self.add_rule(Rule(same_suit, None))
        self.add_rule(Rule(same_value, None))

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def check_played_card(self, card, game):  # Checks if played card is legal
        i = len(self.rules) - 1
        while self.rules[i].card_obeys_rule(card, game) is None:
            i -= 1
        return self.rules[i].card_obeys_rule(card, game)
        # we'd better not have an index out of bounds, or else the starting rules are broken
