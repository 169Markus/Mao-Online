import string
from typing import List

from card import Card


class Player(object):
    def __init__(self, username: string):
        self.username = username
        self.id: int = hash(self.username)
        self.hand: List[Card] = []
