def Game():
    def __init__(self, players):
        self.state = 'Ongoing'
        self.draw_deck = 0
        self.play_deck = 0
        self.hands = []
        self.players = players
        self.history = []
        