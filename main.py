from search_id import *

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

