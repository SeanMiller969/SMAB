from bs4 import BeautifulSoup
from urllib.request import urlopen
from Weapon import Weapon
import pymongo
import ssl


client = pymongo.MongoClient("mongodb+srv://thieljohn:SMABword123@cluster0.ehgdd.mongodb.net/SMAB?retryWrites=true&w=majority")
db = client.SMAB
weapon_col = db.Weapon

def makeDoc(string_data, i):
    buy_price = string_data[i + 1]
    sell_price = string_data[i + 2]
    full_listing = string_data[i + 3]
    #Example listing --StatTrak™ Sawed-Off | Limelight (Well-Worn)
    split_listing = full_listing.split("|")
    #StatTrak checking implemented here ----
    weapon = split_listing[0]
    skin_condition = split_listing[1].split("(")
    skin = skin_condition[0].strip()
    condition = skin_condition[1].replace(')', '')
    '''Should be updating prices at each weapon type not adding a new entry!!!!'''
    weapon = {'gun' : weapon,
        'skin' : skin,
        'condition' : condition,
        'buy_at' : buy_price,
        'sell_at' : sell_price,
    }
    #Possible code to update the values, untestable until the base parts of the database is filled in.
    '''
    db.weapon_col.update(
        {_id: Possibly gun, or an integer value, unsure}
        $set:{
            buy_at: buy_price
            sell_at: sell_price
        }
    )
    '''


def scrape_data(url):
    #read html data
    page = urlopen(url)
    html = page.read().decode("utf-8")
    #Use BeauifulSoup to parse html data
    soup = BeautifulSoup(html, "html.parser")
    f = open("json.txt","w", encoding='utf-8')
    #store it in a .txt file
    f.write(soup.text)
    #Now parse the .txt file
    lines = []
    with open("json.txt", "r", encoding= 'utf-8') as f:
        for line in f:
            if(line != "\n"):
                lines.append(line.strip())
    f.close()
    #Now store the data in each line
    for i in range(len(lines)):
        if lines[i] == "Starting at:":
            makeDoc(lines, i)
            """This means we need to connect to the MongoDB, possibly with Flask, not entirely sure."""
            
