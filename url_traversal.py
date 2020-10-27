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
    print("Cleaning")
    parsefile = open(url, "r", encoding= 'utf-8')
    print(parsefile.read())
    for aline in parsefile:
        words = aline.split(' ')
        newlist = []
        for word in words:
            word = word.strip()
            newlist.append(word)
        print(newlist)
    parsefile.close()