from bs4 import BeautifulSoup
from urllib.request import urlopen
from Weapon import Weapon
import ssl

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
    print("check")
    for i in range(len(lines)):
        if lines[i] == "Starting at:":
            #"starting at" is followed by our relevant data
            buy_price = lines[i + 1]
            sell_price = lines[i + 2]
            full_listing = lines[i+3]
            #Example listing --StatTrak™ Sawed-Off | Limelight (Well-Worn)
            split_listing = full_listing.split("|")
            #StatTrak checking implemented here ----
            weapon = split_listing[0]
            skin_condition = split_listing[1].split("(")
            skin = skin_condition[0].strip()
            condition = skin_condition[1].replace(')', '')
            #Now lets put the weapons in Mongo under the case name
            """This means we need to connect to the MongoDB, possibly with Flask, not entirely sure."""
