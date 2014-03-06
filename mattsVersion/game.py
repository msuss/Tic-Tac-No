from gameboard import GameBoard
from card import Card

class Game():
	def __init__(self, size, cellSize, setSize, numFeatures):
		self.size = size
		self.cellSize = cellSize
		self.setSize = setSize
		self.numFeatures = numFeatures
		self.gameboard = GameBoard(size, cellSize)
		self.cardSet = Card.createCardSet(setSize,numFeatures)

g = Game(3,3,3,3)
print len(g.cardSet)