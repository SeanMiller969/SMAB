from bs4 import BeautifulSoup
from urllib.request import urlopen
from Weapon import Weapon
import ssl

def get_json(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    f = open("json.txt","w", encoding='utf-8')
    f.write(soup.text)
    f.seek(0)
    jsonoutput = clean_json("json.txt")
    return jsonoutput

def clean_json(url):
    #print("Cleaning")
    content = []
    with open(url, "r", encoding= 'utf-8') as f:
        for line in f:
            if(line != "\n"):
                content.append(line.strip())
    f.close()
    parsedoutput = []
    parserpart = []
    output = []
    print(len(content))
    for i in range(len(content)):
        print(content[i])
        if(content[i] == "Starting at:"):
            price1 = content[i + 1]
            price2 = content[i + 2]
            fullitem = content[i+3]
            splititem = fullitem.split("|")
            weapon = splititem[0]
            splitseconditem = splititem[1].split("(")
            print(splitseconditem)
            skin = splitseconditem[0].strip()
            condition = splitseconditem[1].replace(')', '')
            print("Weapon is:", weapon)
            print("Skin is:", skin)
            print("Condition is:", condition)
            print("Buy price is:", price1)
            print("Sell price is:", price2)
            parserpart.append(weapon)
            parserpart.append(skin)
            parserpart.append(condition)
            parserpart.append(price1)
            parserpart.append(price2)
            conditiondict = {
                "Well-Worn" : 4 ,
                "Battle-Scarred" : 3 ,
                "Field-Tested" : 2,
                "Minimal Wear" : 1,
                "Factory New" : 0,
            }
            print("Conditiondict", conditiondict[condition])
            stattrak = False
            weapon = weapon.strip()
            attributelist = weapon.split(" ")
            print(attributelist)
            if(len(attributelist) != 1):
                if(len(attributelist)== 2):
                    print(attributelist)
                    if(attributelist[0] == "R8"):
                        weapon = attributelist[0] + " " + attributelist[1]
                    else:
                        weapon = attributelist[1]
                        stattrak = True
                #R8 Revolver Case
                if(len(attributelist)== 3):
                    weapon = attributelist[1] + " " + attributelist[2]
                    stattrak = True
            price1 = price1.replace('$', '')
            price2 = price2.replace('$', '')
            print("prices are fixed", price1,price2)
            weap = Weapon(weapon,skin,stattrak,conditiondict[condition],price1,price2)
            output.append(weap)
            print(parserpart)
            parsedoutput.append(parserpart)
            splititem.clear()
            splitseconditem.clear()

    #print(parsedoutput)
    #for i in parsedoutput:
    #    print("Weapon is:", i[0])
    #    print("Skin is:", i[1])
    #    print("Condition is:", i[2])
    #    print("Buy price is:", i[3])
    #    print("Sell price is:", i[4])
    return output
