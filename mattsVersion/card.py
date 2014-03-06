class Card():

	numFeatures = 3
	setSize = 3
	# Set for 3 features and set size of 3 for now
	# Can theoretically expand to any N for both
	@staticmethod
	def isSet(card1, card2, card3):
		for i in range(Card.numFeatures):
			s = set([card1.features[i],card2.features[i],card3.features[i]])
			if not (len(s)==1 or len(s)==Card.setSize):
					return False
		return True

	@staticmethod
	def createCardSet(setSize, numFeatures):
		import itertools
		deck = {Card(list(i)) for i in itertools.product(range(setSize), repeat = numFeatures)}
		return deck

	def __init__(self, features):
		self.features = features

	def __repr__(self):
		return "Card: " + str(self.features)

# c1 = Card([0,0,0])
# c2 = Card([1,0,1])
# c3 = Card([2,0,2])
# c4 = Card([2,0,1])
# print Card.isSet(c1,c1,c1)
# print Card.isSet(c1,c2,c3)
# print Card.isSet(c1,c2,c4)