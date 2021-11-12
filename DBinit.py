# Initialize the bones of our MongoDB
# call it a Smababase
from pymongo import MongoClient
import pickle

#client = pymongo.MongoClient("mongodb+srv://thieljohn:SMABword1234@cluster0.ehgdd.mongodb.net/SMAB?retryWrites=true&w=majority")
client = MongoClient('mongodb://localhost:2701')
db = client.SMAB

txt_file = pickle.load(open('setup/temp.pkl', 'rb'))
for i in txt_file:
    #print(i)
    if type(i) == str:
        case_col = db[i]
    else:
        gun = i[1].split()[0]
        skin = i[1].split("|")[1]
        #print(i[1].split("|"))
        rarity = i[0]
        temp_dict = {
            'Gun' : gun,
            'Skin' : skin,
            'Rarity' : rarity
        }
        case_col.insert_one(temp_dict)
        print(temp_dict)

print("Done!")

    
    
    

