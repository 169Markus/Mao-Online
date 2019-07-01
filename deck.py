class deck():
    def __init__(self, ty):
        self.cards = []

    def shuffle(self):
        return
    
    def add(self):
        return

    def draw(self):
        return

    def remove(self, card):
        '''remove the cards from the deck that are drawn or played'''
        return

    

class draw_deck(deck):
    def __init__(self):
        self.size = 52

class play_deck(deck):
    def __init__(self):
        self.size = 0

        

def create_cards():
    '''create all the cards in a standard deck'''
    nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suit = ['S', 'H', 'D', 'C']

    cards = []
    for s in suit:
        for n in nums:
            cards.append(str(s + n))

    cards.append('BJ')
    cards.append('RJ')

    return cards