from bs4 import BeautifulSoup
from urllib.request import urlopen
from Weapon import Weapon
import ssl


'''
Well-Worn—7.92 percent
Battle-Scarred—9.93 percent
Field-Tested—43.18 percent
Minimal Wear—24.68 percent
Factory New—14.71 percent
'''

def get_json(url):
    ###This allows the program to run on a nac.
    ssl._create_default_https_context = ssl._create_unverified_context
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    ###Gives us a .txt formatted file
    # jsson -> html -> txt
    f = open("json.txt","w", encoding='utf-8')
    f.write(soup.text)
    f.seek(0)
    jsonoutput = clean_json("json.txt")
    #returns the list of classes.
    return jsonoutput

def clean_json(url):
    #print("Cleaning")
    content = []
    #content is the list of lines from the txt.
    with open(url, "r", encoding= 'utf-8') as f:
        for line in f:
            if(line != "\n"):
                content.append(line.strip())
    f.close()
    #close the file now that all data is saved
    output = []
    #run through the parser
    for i in range(len(content)):
        if(content[i] == "Starting at:"):
            #Starting at is a hook
            price1 = content[i + 1]
            price2 = content[i + 2]
            fullitem = content[i+3]
            splititem = fullitem.split("|")
            weapon = splititem[0]
            splitseconditem = splititem[1].split("(")
            skin = splitseconditem[0].strip()
            condition = splitseconditem[1].replace(')', '')
            #all data has been split, additional parseing necessary
            #these prints are not necessary
            print("Weapon is:", weapon)
            print("Skin is:", skin)
            print("Condition is:", condition)
            print("Buy price is:", price1)
            print("Sell price is:", price2)
            #holds all condition values
            conditiondict = {
                "Well-Worn" : 4 ,
                "Battle-Scarred" : 3 ,
                "Field-Tested" : 2,
                "Minimal Wear" : 1,
                "Factory New" : 0,
            }
            #stattraks the only attribute we support, lets check for it!
            stattrak = False
            weapon = weapon.strip()
            attributelist = weapon.split(" ")
            #Check if there is an attribute.
            if(len(attributelist) != 1):
                if(len(attributelist)== 2):
                    if(attributelist[0] == "R8"):
                        weapon = attributelist[0] + " " + attributelist[1]
                    else:
                        weapon = attributelist[1]
                        stattrak = True
                #R8 Revolver Case
                if(len(attributelist)== 3):
                    weapon = attributelist[1] + " " + attributelist[2]
                    stattrak = True
            #remove dollar signs from prices for computation
            price1 = price1.replace('$', '')
            price2 = price2.replace('$', '')
            #build class and append it
            weap = Weapon(weapon,skin,stattrak,conditiondict[condition],price1,price2)
            output.append(weap)
            #reset the loop
            splititem.clear()
            splitseconditem.clear()
    return output
