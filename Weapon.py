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
		#sell and buy prices are the prices for the weapon at each rarity, in the order the rarities are listed in the order of the quality value list
		self.buy_price = buy_price
		self.sell_price = sell_price
		#summation of price at a certain quality * the percent chance of that quality (Expected Value)
		temp = 0
		quality_value_list = [.0792, .0993, .4318, .2468, .1471]
		max = len(sell_price)
		for i in range(0, max):
			temp += sell_price[i] * quality_value_list[i]
		self.estimted_value = temp

	def stat_track(self, stattrack):
		if(stattrack):
			self.stattrack = True
		else:
			self.stattrack = False

	def printWeapon(self):
		print("Name: " + self.name + 
			"\nSkin: " + self.skin +
			"\nRarity:", self.rarity,
			"\nBuy Prices:", self.buy_price,
			"\nSell Prices:", self.sell_price,
			"\nEstimated Value:", self.estimted_value)

		if(self.stattrack):
			print("Stat-Track: True")
		else:
			print("Stat-Track: False")

x = Weapon()
x.printWeapon()





