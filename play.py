class play():
    def __init__(self, user):
        self.user = user
        self.drawn = []
        self.played = []
        self.said = []

    def get_chatted(self):
        '''pull what user said during play from the chat'''
        return