from bs4 import BeautifulSoup
from urllib.request import urlopen
from search_id import *
from url_traversal import get_json
import csv
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
    with open('EV.csv', 'wt') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        csv_writer.writerow(["Name","skin","condition","buy_prive","sell_price", "estimated_value"])
        for j in JSON:
            for i in j:
                csv_writer.writerow(i.CSVstructure())

if __name__ == "__main__":
    main()

