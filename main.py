from game import Game
from player import Player

players = [Player("andrew"), Player("derik"), Player("markus"), Player("hanna")]

game = Game(players)

while not game.over:
    game.turn()
