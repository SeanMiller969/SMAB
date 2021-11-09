# Initialize the bones of our MongoDB
# call it a Smababase
import pymongo
import pickle

client = pymongo.MongoClient("mongodb+srv://thieljohn:SMABword123@cluster0.ehgdd.mongodb.net/SMAB?retryWrites=true&w=majority")
db = client.SMAB
case_col = db.Case

txt_file = pickle.load(open('setup/temp.pkl', 'rb'))
for i in txt_file:
    print(i)

