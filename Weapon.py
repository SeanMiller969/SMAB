#Class for a WEAPON in CSGO Cases

class Weapon:
	#need at least the weapon name to initialize the object
	#FOR QUALITY
	#4 is battle scarred
	#3 is well worn
	#2 is field tested
	#1 is minimal wear
	#0 is factory new
	
	#Battle-Scarred— 9.93%
	#Well-Worn— 7.92%
	#Field-Tested— 43.18%
	#Minimal Wear— 24.68%
	#Factory New— 14.71%

	def __init__(self, name_of_weapon = "", skin = "", stattrack = False, condition = -1, buy_price = 0, sell_price = 0):
		self.name_of_weapon = name_of_weapon
		self.skin = skin
		self.stattrack = stattrack
		self.condition = condition 
		self.buy_price = float(buy_price)
		self.sell_price = float(sell_price)
		#summation of price at a certain quality * the percent chance of that quality (Expected Value)
		#temp = 0
		quality_value_list = [.1471, .2468, .4118, .0792, .0993]
		#for i in range(5):
		#	temp += sell_price[i] * quality_value_list[i]
		self.estimated_value = float(sell_price) * quality_value_list[condition]

	#changes the odds of getting the weapon.
	def stat_track(self, stattrack):
		if(stattrack):
			self.stattrack = True
		else:
			self.stattrack = False

	#Example:
	#This will be updated with how we want the data.
	#"Name","skin","condition","buy_prive","sell_price", "estimated_value"
	def CSVstructure(self):
		return [self.name_of_weapon,self.skin,self.condition,self.stattrack, self.buy_price,self.sell_price, round(self.estimated_value, 2)]


