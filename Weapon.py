#Class for a WEAPON in CSGO Cases

class Weapon:
	#need at least the weapon name to initialize the object
	#FOR QUALITY
	#5 is battle scarred
	#4 is well worn
	#3 is field tested
	#2 is minimal wear
	#1 is factory new
	#Well-Worn— 7.92%
	#Battle-Scarred— 9.93%
	#Field-Tested— 43.18%
	#Minimal Wear— 24.68%
	#Factory New— 14.71%

#	def __init__(self):
#		self.name = ""
#		self.skin = ""
#		self.stattrack = False
#		self.rarity = 0
#		self.buy_price = []			
#		self.sell_price = []
#		self.estimted_value = 0

	def __init__(self, name = "", skin = "", stattrack = False, rarity = 0, buy_price = [], sell_price = []):
		self.name = name
		self.skin = skin
		self.stattrack = stattrack
		self.rarity = rarity
		self.buy_price = buy_price
		self.sell_price = sell_price
		#summation of price at a certain quality * the percent chance of that quality (Expected Value)
		temp = 0
		quality_value_list = [.0792, .0993, .4318, .2468, .1471]
		for i in range(5):
			temp += sell_price[i] * quality_value_list[i]
		self.estimted_value = temp

	def stat_track(self, stattrack):
		if(stattrack):
			self.stattrack = True
		else:
			self.stattrack = False



