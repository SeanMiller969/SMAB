# Initialize the bones of our MongoDB
# call it a Smababase
from pymongo import MongoClient
import pickle
import sys

client = MongoClient("mongodb+srv://thieljohn:SMABword@cluster0.ehgdd.mongodb.net/SMAB?retryWrites=true&w=majority")
db = client.SMAB

counter = 0
txt_file = pickle.load(open('setup/temp.pkl', 'rb'))
for i in txt_file:
    print(i)
    if type(i) is str:
        case_col = db[i]
    else:
        gun,skin = i[1].split("|")
        rarity = i[0]
        temp_dict = {
            'Gun' : gun,
            'Skin' : skin,
            'Rarity' : rarity
        }
        case_col.insert_one(temp_dict)
        print(type(temp_dict))
    counter+= 1

print("Done!")