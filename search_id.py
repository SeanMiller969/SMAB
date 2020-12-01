def find_case(case):
    #hard coded values for cases eventually will be 
    #done we web scraping
    SearchDict =  {"The Winter Offensive Collection": "1",
                   "The Phoenix Collection": "2",
                   "The Huntsman Collection": "3",
                   "The Breakout Collection": "4",
                   "The Vanguard Collection": "5",
                   "The Chroma Collection": "6",
                   "The Chroma 2 Collection": "7",
                   "The Falchion Collection": "8",
                   "The Shadow Collection": "9",
                   "The Revolver Case Collection": "10",
                   "The Wildfire Collection": "11",
                   "The Chroma 3 Collection":"12",
                   "The Gamma Collection": "13",
                   "The Glove Collection": "15",
                   "The Spectrum Collection": "16",
                   "The Operation Hydra Collection": "17",
                   "The Spectrum 2 Collection": "18",
                   "The Clutch Collection": "19",
                   "The Horizon Collection": "20",
                   "The Danger Zone Collection": "21",
                   "The Prisma Collection": "22",
                   "The Shattered Web Collection": "23",
                   "The CS20 Collection": "24",
                   "The Prisma 2 Collection": "25",
                   "The Fracture Collection": "26" }
    if case in SearchDict:  
        return "https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_" + SearchDict[case] + "&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&appid=730#p1_name_asc"
    else:   
        return "ERROR"