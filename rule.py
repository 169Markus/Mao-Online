class rule_book():
    '''keep track of all the rules'''
    def __init__(self):
        self.rules = []
       
    


class rule():
    def __init__(self, legality, effect):
        self.legality = legality
        self.effect = effect

    def check_legality(self,play,gamestate):
        return self.legality(play,gamestate)
    
    def penalty(self, player, number, message):
        pass
