from card import Card
class GameBoard():
	
	def __init__(self, boardSize,cellSize):
		self.rows = boardSize
		self.cols = boardSize
		self.cellSize = cellSize
		self.board = [[set()for _ in range(self.cols)] 
						for __ in range(self.rows)]

	def inBounds(self, r,c):
		return (0 <= r and r < self.rows) and ((0 <= c and c < self.cols))
		
	# Return a copy of the set of cards in cell (r,c)
	def getCardsInCell(self, r, c):
		return set(self.board[r][c])

	def hasCards(self,r,c):
		return not len(self.getCardsInCell(r,c)) == 0

	#Set the cards in cell (r,c) to be cards
	def setCards(self, cards, r, c):
		if len(cards)>self.cellSize:
			# Throw Exception
			print "NOPE"
			return
		self.board[r][c]=cards

	#Add
	def addCard(self, newCard, r, c):
		# Need to check if deck is empty to play in middle square
		if len(self.getCardsInCell(r,c))>=self.cellSize:
			# Throw Exception
			print "NOPE"
			return
		self.board[r][c].add(newCard)

	# All these line methods need to be modified for 
	# handling more than 3 cards
	def scoreLines(self, playedCard, r, c):
		lines = self.validLines(r,c)
		score = len([(card1,card2) for (cell1,cell2) in lines 
					for card1 in self.getCardsInCell(*cell1)
					for card2 in self.getCardsInCell(*cell2)
					if Card.isSet(playedCard, card1, card2)])
		stack = self.getCardsInCell(r,c)
		if len(stack)==self.cellSize:
			if Card.isSet(*stack):
				score+=1
		return score


	def validLines(self,r,c):
		lines = set()
		if r==c:
			lines.add(self.getForwardDiagonalLine(r,c))
		if (r+c)==(self.cols-1):
			lines.add(self.getBackwardDiagonalLine(r,c))
		lines.add(self.getVerticalLine(r,c))
		lines.add(self.getHorizontalLine(r,c))
		return lines

	def getVerticalLine(self,r,c):
		cells = {(i,c) for i in range(0,self.rows)}
		cells.remove((r,c))
		# if all(hasCards(*cell) for cell in cells):
		return tuple(cells)
		
	def getHorizontalLine(self,r,c):
		cells = {(r,i) for i in range(0,self.cols)}
		cells.remove((r,c))
		# if all(hasCards(*cell) for cell in cells):
		return tuple(cells)

	# Assumes square
	def getForwardDiagonalLine(self,r,c):
		cells = {(i,i) for i in range(0,self.cols)}
		cells.remove((r,c))
		# if all(hasCards(*cell) for cell in cells):
		return tuple(cells)

	# Assumes square
	def getBackwardDiagonalLine(self,r,c):
		cells = {(i,(self.cols-1)-i) for i in range(0,self.cols)}
		cells.remove((r,c))
		# if all(hasCards(*cell) for cell in cells):
		return tuple(cells)



	def playCard(self, playedCard, r, c):
		self.addCard(playedCard,r,c)
		return self.scoreLines(playedCard, r, c)

	def __str__(self):
		s="---------------------------------\n"
		for r in range(self.rows):
			s += "||  "
			for c in range(self.cols):
				s += self.cardsToString(self.board[r][c])
				s += "  ||  "
			s=s[0:-6] +"||"+ "\n"
			s+="---------------------------------\n"
		return s

	# Make this a real method
	def cardsToString(self, cards):
		if len(cards)==0:
			return "     "
		if len(cards)==1:
			return "  A  "
		if len(cards)==2:
			return " A B "
		if len(cards)==3:
			return "A B C"

# g = GameBoard(3,3)
# c1 = Card([0,0,0])
# c2 = Card([1,0,1])
# c3 = Card([2,0,2])
# c4 = Card([2,0,1])
# c5 = Card([1,1,1])
# c6 = Card([1,2,1])

# g.addCard(c1,0,0)
# g.addCard(c3,2,2)

# print g.board
# print g.playCard(c2,1,1)
# print g.board
# print g.playCard(c5,1,1)
# print g.playCard(c6,1,1)

