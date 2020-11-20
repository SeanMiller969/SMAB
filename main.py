from bs4 import BeautifulSoup
from urllib.request import urlopen
from search_id import *
from url_traversal import get_json
from Weapon import *

def main():
    print("Welcome to SMAB")
    #do a case match
    #case = input("Enter case you want to look at: ")
    #determine which case this is and get the correct url.
    #cases have an id tag associated with them in the url
    #tag_set_community_13 <-- this is that tag number
    #this will be hard coded and will be updated accordinginly
    url = find_case("The Gamma Collection")
    if(url == "ERROR"):
        print("Case not found!")
    #going through all the links should pass back a list of skin objects
    #eventually we will intialize the list of case objects.
    JSON = []
    for i in range(1):
        JSON.append(get_json(url[:len(url) - 11] + str(i) + url[len(url) - 10:]))
        i += 1
    #Pipe out to a csv
    for j in JSON:
        for i in j:
            print(i.name_of_weapon, i.skin, i.stattrack, i.condition, i.sell_price, i.buy_price)

if __name__ == "__main__":
    main()

