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


class Case:

	def __init__(self):
		self.name = ""
		self.weapons = []
		self.estimated_value = 0

	def setValue(self):
		temp = 0
		for w in weapons:
			temp += w.rarity * w.estimated_value
		self.estimated_value = temp
