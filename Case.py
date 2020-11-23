#CASE CLASS

#Values taken from CSGO community data

#Well-Worn— 7.92%
#Battle-Scarred— 9.93%
#Field-Tested— 43.18%
#Minimal Wear— 24.68%
#Factory New— 14.71%

#stattrack - 10%

#Blue- 79.92%
#Purple- 15.98%
#Pink- 3.2%
#Red- 0.64%
#Yellow- 0.26%

#knife-rarity(Global?)


class Case:

	'''def __init__(self):
		self.name = ""
		self.weapons = []
		self.estimated_value = 0
		self.knife_value = 0
		'''

	def __init__(self, name="", weapons=[], estimated_value=0, knife_value=0):
		self.name = name
		self.weapons = weapons
		self.estimated_value = estimated_value
		self.knife_value = knife_value

	def setValue(self):
		temp = 0
		for w in self.weapons:
			temp += w.rarity * w.estimated_value
		temp += self.knife_value * .0025

		self.estimated_value = temp

	def printCase(self):
		print("Name:", self.name,
			"\nWeapons:", self.weapons,
			"\nEstimated Value:", self.estimated_value,
			"\nKnife Value:", self.knife_value)

x = Case()
x.setValue()
x.printCase()


