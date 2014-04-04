from gameboard import GameBoard
from card import Card
from player import Player
import random



class Game():

	def __init__(self, boardSize, cellSize, setSize, numFeatures, handSize, numPlayers):
		self.boardSize = boardSize
		self.cellSize = cellSize
		self.setSize = setSize
		self.numFeatures = numFeatures
		self.gameboard = GameBoard(boardSize, cellSize)
		self.cardSet = Card.createCardSet(setSize,numFeatures)
		self.deck = set(self.cardSet)
		self.players = [Player(i, self.drawCardsFromDeck(handSize)) 
						for i in range(numPlayers)]
		self.numPlayers = numPlayers

	@staticmethod
	def drawRandomCards(cards,n):
		sampledCards = set(random.sample(cards, n))
		cards -= sampledCards
		return sampledCards

	def drawCardsFromDeck(self, n):
		return Game.drawRandomCards(self.deck, n)

boardSize=3
cellSize=3
setSize=3
numFeatures=3
handSize = 3
numPlayers = 2
g = Game(boardSize, cellSize, setSize,
		 numFeatures, handSize, numPlayers);

def runGame():
	gameOver = False
	currentPlayerIdx = 0
	currentPlayer = g.players[currentPlayerIdx]
	while not gameOver:
		inp = raw_input()
		print "Player ", currentPlayer.getId(), " has: ", currentPlayer.getHand()
		currentPlayerIdx += 1
		currentPlayerIdx %= g.numPlayers
		currentPlayer = g.players[currentPlayerIdx]
		if inp=="bye":
			gameOver = True
	print "Adios"

if __name__ == '__main__':
	
	print len(g.cardSet)
	gameOver = False
	runGame()






