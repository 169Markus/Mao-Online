from game import Game
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

    def __init__(self, legality, effects):
        self.legality = legality
        self.effects = effects


class RuleBook(object):
    """Stores all rules"""

    def __init__(self):
        self.rules: List[Rule] = []

        # Rule of least precedence must always return true or false
        def can_draw(play: Play, game: Game):
            return play.drawn > 0

        def same_suit(play: Play, game: Game):
            if play.cards[0].suit == game.discard_deck.top.suit:
                return True

        def same_value(play: Play, game: Game):
            if play.cards[0].value == game.discard_deck.top.value:
                return True

        def one_card(play: Play, game: Game):
            if len(play.cards) > 1:
                return False

        def in_turn(play: Play, game: Game):
            if play.player != game.players[game.whose_turn]:
                return False


        def reverse_play(play: Play, game: Game):
            if play.cards[0].value == 'Q':
                game.turn_increment *= -1

        def skip(play: Play, game: Game):
            if play.cards[0].value == '8':
                game.whose_turn = game.next_turn(game.whose_turn)

        def draw_two_thanks(play: Play, game: Game):
            if play.cards[0].value == '7':
                pass
                # require "have a nice day" on current player,
                # draw two and "thank you" on next player


        self.add_rule(Rule(same_suit, None))
        self.add_rule(Rule(same_value, None))
        self.add_rule(Rule(one_card, None))
        self.add_rule(Rule(None, reverse_play))
        self.add_rule(Rule(None, skip))
        self.add_rule(Rule(None, draw_two_thanks))

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def check_play(self, play: Play, game: Game):  # Checks if play is legal
        i = len(self.rules) - 1
        while self.rules[i].legality(play, game) is None:
            i -= 1
        return self.rules[i].legality(play, game)
        # The starting rule of least precedence will never be `None`
