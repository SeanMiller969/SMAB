# SMAB
A steam market analysis bot


This project is an application to scrape the Steam Marketplace for prices of items in CS:GO cases. It then stores this information in a Mongo Database, which holds each case and the weapons inside. To run this application on your own machine, use the following steps. 

1. Download all the files in the project, or just clone the repository. 
2. Install pymongo, using the command <pip install pymongo>
3. 


This project consists of a text interface designed to scrape the Steam Marketplace and obtain an array of JSONs. To compile and run the program, install all supplementary python files along with main.py and run main.py in an ide or compile it. It takes in a specific case and the link to the Steam Marketplace file and based off of the individual link collects JSON data. Moving forward, code will be added to read through the JSON and find numbers based off of it to crunch. An example currently exists based off of the Gamma Case, it is currently runnable.
When run, the program returns the JSON from the Gamma Case. Further cases or a case selector have been added, just uncomment the selection part. It now supports all different collections in the dictionary file. All of these are functional. The json is converted into a txt file, and parsed. The printing of the json is now optimized and prints most of the data found. It shows prices of the first page of listings. The function returns a list of classes. These classes are then built in the mainfile. It then outputs the data in a .csv.

