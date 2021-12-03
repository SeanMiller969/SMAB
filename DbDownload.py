from pymongo import MongoClient
import pickle
import sys
from bson.json_util import dumps, loads

client = MongoClient("mongodb+srv://thieljohn:SMABword@cluster0.ehgdd.mongodb.net/SMAB?retryWrites=true&w=majority")
db = client.SMAB

cases = ["CS:GO-Weapon-Case", 
"eSports 2013 Case",  
"Operation Bravo Case", 
"CS:GO Weapon Case 2", 
"eSports 2013 Winter Case", 
"Winter Offensive Weapon Case",
"CS:GO Weapon Case 3",
"Operation Phoenix Weapon Case",
"Huntsman Weapon Case",
"Operation Breakout Weapon Case",
"eSports 2014 Summer Case",
"Operation Vanguard Weapon Case",
"Chroma Case",
"Chroma 2 Case",
"Falchion Case",
"Shadow Case",
"Revolver Case",
"Operation Wildfire Case",
"Chroma 3 Case",
"Gamma Case",
"Gamma 2 Case",
"Glove Case",
"Spectrum Case",
"Operation Hydra Case",
"Spectrum 2 Case",
"Clutch Case",
"Horizon Case",
"Danger Zone Case",
"Prisma Case",
"CS20 Case",
"Shattered Web Case",
"Prisma 2 Case",
"Fracture Case",
"Operation Broken Fang Case",
"Snakebite Case",
"Operation Riptide Case"]

file = open("offlineDatabase.json", 'w+')
for case in cases:
	collection = db[case]
	cursor = collection.find()
	list_cur = list(cursor)
	print(list_cur)
	l = {case : list_cur}
	print(l)
	json_data = dumps(l, indent=2)
	file.write(json_data)
file.close()