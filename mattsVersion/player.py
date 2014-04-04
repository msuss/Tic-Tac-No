class Player():
	
	def __init__(self, id, startingHand):
		self.id = id
		self.hand = startingHand
		self.points = 0

	def getId(self):
		return self.id
		
	def getHand(self):
		return self.hand

	def setHand(self, hand):
		self.hand = hand
		return self.hand

	def playCard(self, card):
		self.hand.remove(card)
		return self.hand

	def addCardToHand(self, card):
		self.hand.add(card)
		return self.hand

	def getPoints(self):
		return self.points

	def addPoints(self, newPoints):
		self.points+=newPoints
		return self.points

	def setPoints(self, points):
		self.points = points
		return self.points
