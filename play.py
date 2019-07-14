import string
from typing import List

from card import Card
from player import Player


class Play(object):
    def __init__(self, player: Player, drawn: int, cards: List[Card], said: List[string]):
        self.player = player  # Player
        self.drawn = drawn    # int
        self.cards = cards    # list of Card
        self.said = said      # string (list of?)
