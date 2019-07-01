def Game():
    def __init__(self):
        self.state = 'Ongoing'
        self.rule_book = None
        self.draw_deck = None
        self.play_deck = None
        self.players = None
        self.history = []
        self.play_order = []
        self.turn = []
    
    def init(self, rules, deck, players):
        self.state = 'Ongoing'
        self.rule_book = rules
        self.draw_deck = deck
        self.play_deck = deck()
        self.players = players
        self.history = []
        self.play_order = []
        self.turn = []