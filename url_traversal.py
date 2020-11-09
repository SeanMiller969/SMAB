from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_json(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    f = open("json.txt","w", encoding='utf-8')
    f.write(soup.text)
    f.seek(0)
    clean_json("json.txt")
    return "Json Obtained"

def clean_json(url):
    #print("Cleaning")
    content = []
    with open(url, "r", encoding= 'utf-8') as f:
        for line in f:
            if(line != "\n"):
                content.append(line.strip())
    ###
    f.close()
    #contentcopy = content
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
            print("Weapon is:", splititem)
            print("Skin is:", skin)
            print("Condition is:", condition)
            print("Buy price is:", price1)
            print("Sell price is:", price2)


    #print(parsefile.read())
    #for aline in parsefile:
        #words = aline.split(' ')
        #newlist = []
        #for word in words:
            #word = word.strip()
            #newlist.append(word)
        #print(newlist)
