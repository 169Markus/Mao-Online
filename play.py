import string
from typing import List

from card import Card
from player import Player


class Play(object):
    def __init__(self, player: Player):
        self.player = player
        self.drawn = 0
        self.cards: List[Card] = []
        self.said: List[string] = []
