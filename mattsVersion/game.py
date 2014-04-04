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
		 numFeatures, handSize, numPlayers)

# Need to make logic atomic, either both go through or neither does
def playCard(player, card):
	player.playCard(card)
	g.gameboard.playCard(card, 0, 0)

def runGame():
	gameOver = False
	currentPlayerIdx = 0
	currentPlayer = g.players[currentPlayerIdx]
	while not gameOver:
		print "Player ", currentPlayer.getId(), " has: ", currentPlayer.getHand()
		inp = raw_input()
		cardToPlay = random.sample(currentPlayer.getHand(), 1)[0]
		playCard(currentPlayer, cardToPlay)

		currentPlayerIdx += 1
		currentPlayerIdx %= g.numPlayers
		currentPlayer = g.players[currentPlayerIdx]
		print g.gameboard
		if inp=="bye":
			gameOver = True
	print "Adios"

if __name__ == '__main__':
	
	print len(g.cardSet)
	gameOver = False
	runGame()






