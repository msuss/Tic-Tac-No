from gameboard import GameBoard
from card import Card

class Game():
	def __init__(self, size, cellSize):
		self.size = size
		self.cellSize = cellSize
		self.gameboard = GameBoard(size, cellSize)