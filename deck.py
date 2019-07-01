from random import shuffle

class deck():
    def __init__(self):
        self.cards = []

    def shuffle(self):
        shuffle(self.cards)
        
    def add(self,card):
        self.cards.append(card)

    def draw(self):
        return self.cards.pop()

    def remove(self, card):
        '''remove the cards from the deck that are drawn or played'''
        return


class draw_deck(deck):
    def __init__(self):
        self.size = 52

class play_deck(deck):
    def __init__(self):
        self.size = 0

        

def create_standard():
    '''create all the cards in a standard deck'''
    nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suit = ['S', 'H', 'D', 'C']

    cards = deck()
    for s in suit:
        for n in nums:
        
            cards.add(card(s,n))

    cards.add(card('BJ',''))
    cards.add(card('RJ',''))
    cards.shuffle()
    return cards