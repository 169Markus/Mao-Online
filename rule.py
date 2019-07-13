class RuleBook():
    '''keep track of all the rules'''
    def __init__(self):
        self.rules = []
       
    def addrule(self, rule):
        rule.effect
        self.rules.insert(0,rule)

    
    def checkplay(self, play, game):
        for rule in self.rules:
            if(rule(play,gamestate) != 0):
                return rule(play,gamestate)
        return 1
        
    


class rule():
    def __init__(self, legality, effect):
        self.legality = legality
        self.effect = effect

    def checklegality(self,play,gamestate):
        return self.legality(play,gamestate)
    
    def penalty(self, player, number, message):
        pass
