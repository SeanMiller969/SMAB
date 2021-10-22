import requests
import json
import time
from bs4 import BeautifulSoup

def main():
    for val in caseList:
        URL = "https://steamcommunity.com/market/listings/730/" + val
        print(URL)
        
        page = requests.get(URL)
        time.sleep(4)
        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find_all(type="text/javascript")

        start = results[-1].text.find("var g_rgAssets")
        end = results[-1].text.find(";", start)
        test = json.loads(results[-1].text[start + 17:end])
        key = list(test['730']['2'].keys())[0]
        print(test['730']['2'][key]['descriptions'])

if __name__ == "__main__":
    caseList =  ["CS:GO Weapon Case", 
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