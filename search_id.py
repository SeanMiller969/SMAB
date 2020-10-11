import re

def find_case(case):
    Num = -1
    if(re.search("The Winter Offensive Collection",case)):
        Num = 1
    elif(re.search("Gamma", case)):
        Num = 13
        
    return "https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_" + str(Num) + "&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&appid=730"