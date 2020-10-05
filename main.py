import re

def find_case(case):
    if(re.match("Gamma", case)):
        return "https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_13&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&appid=730"

def main():
    print("Welcome to SMAB")
    #do a case match
    case = input("Enter case you want to look at: ")
    #determine which case this is and get the correct url.
    #cases have an id tag associated with them in the url
    #tag_set_community_13 <-- this is that tag number
    #this will be hard coded and will be updated accordinginly
    url = find_case(case)
    print(url)

if __name__ == "__main__":
    main()

