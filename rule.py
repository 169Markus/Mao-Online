class RuleBook(object):
    '''keep track of all the rules'''

    def __init__(self):
        self.rules = []

    def addrule(self, rule):
        self.rules.append(rule)





    def check_played_card(self, card, game):  # Checks if played card is legal
        i = len(self.rules) - 1
        while self.rules[i].card_obeys_rule(card, game) is None:
            i -= 1
        return self.rules[i].card_obeys_rule(card, game)
        # we'd better not have an index out of bounds, or else the starting rules are broken


class Rule(object):
    def __init__(self, legality, effect):
        self.legality = legality
        self.effect = effect

    def card_obeys_rule(self, card, gamestate):
        return self.legality(card, gamestate)

    def penalty(self, player, number, message):
        pass
