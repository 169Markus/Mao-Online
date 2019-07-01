from random import shuffle

class deck():
    def __init__(self):
        self.cards = []
        self.size = 0
        
    def __init__(self,cards):
        self.cards = cards
        self.size = len(cards)

    def shuffle(self):
        shuffle(self.cards)
        
    def add(self,card):
        self.cards.append(card)
        self.size += 1

    def draw(self):
        if(self.size >= 1):
            self.size -= 1
            return self.cards.pop()
        else:
            return None

    def remove(self, card):
            self.cards.remove(card)

        

