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