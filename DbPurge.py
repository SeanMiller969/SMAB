from pymongo import MongoClient
import pickle
import sys

client = MongoClient("mongodb+srv://thieljohn:SMABword@cluster0.ehgdd.mongodb.net/SMAB?retryWrites=true&w=majority")
#client = MongoClient('mongodb://localhost:2701')
db = client.SMAB
posts = db["Case"]
#post_id = posts.insert_one({'Gun' : "ya mother"})

counter = 0
txt_file = pickle.load(open('setup/temp.pkl', 'rb'))
for i in txt_file:
    print(i)
    if type(i) is str:
        case_col = db[i]
        case_col.drop()
        db["Case.%s" % i].drop()