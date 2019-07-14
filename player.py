import string
from typing import List

from card import Card


class Player(object):
    def __init__(self, username: string):
        self.id: int = hash(self.username)
        self.username = username
        self.hand: List[Card] = []
