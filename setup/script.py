import requests
import time
from bs4 import BeautifulSoup
import pickle

'''
Initialization script this collects data for every single weapon case in the game
this includes data for the rairty of the skin and the weapon and skin name
'''

def main():
    finalList = list()
    #iterate through every case in the game
    for val in caseList:
        finalList.append(val)
        #collect our url
        URL = "https://www.csgodatabase.com/cases/" + val
        #store which case we are int
        print(URL)
        #give the website some breathing room
        time.sleep(2)
        #get our html page using the request library
        page = requests.get(URL)
        #use soup to collect a bunch of html information
        soup = BeautifulSoup(page.content, "html.parser")
        #find every item in the case
        results = soup.find_all("div", class_='skin-box')
        #loop through every item in the html collecting the name and value of the item
        for val in results:
            #go one step deaper in the CSS
            tmp = val.find("div", class_='skin-box-header')
            #create a string version of our CSS
            strTmp = str(tmp)
            #get the start of the weapon rareity
            first = strTmp.find("\"")
            #get the end of the weapon rareity
            last = strTmp.find("\"", first + 1)
            #get the weapon rareity adding 17 to the front and removing the 7 at the end getting
            #the name of the rarity
            value = strTmp[first + 17:last - 7]
            #get the text in our div this is in the form [weapon name | skin name]
            name = tmp.text
            #add to our list this will change
            finalList.append([value, name])
    with open('temp.pkl', 'wb') as f:
        pickle.dump(finalList, f)


        

if __name__ == "__main__":
    caseList =  ["CS:GO-Weapon-Case", 
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

    main()