# SMAB
A steam market analysis bot


This project is an application to scrape the Steam Marketplace for prices of items in CS:GO cases. The front end is buiilt with pug, and the backend is done using Mongo. Python and JavaScript are the languages used in this project. To run this application on your own machine, use the following steps. 

1. Download all the files in the project, or just clone the repository. 
2. Install pymongo, using the command pip install pymongo
3. To simply run and view the program, run main.py. Now you have SMAB!
4. IF you want to get the information in your own database, you will need to edit the DBinit.py and URLtraversal2.py. First you will need your own MongoDB database. To get this, go to mongo.com and create an account. Once you have done this, you will need to create a database on their. There is a tutorial on the website. Once you have a database made, you will need to find this line of code in DBinit.py and URLtraversa2.py. It is near the top for both programs.
client = MongoClient("mongodb+srv://thieljohn:@_SMABwordcluster0.ehgdd.mongodb.net/SMAB?retryWrites=true&w=majority_")
5. You will want to change the thieljohn:SMABword to be your own databases user's username and password in the following format. <username>:<password>. If this does not, try using the defalt connection string provided when you click the connect button on the website. 
6. Before running DBinit.py, make sure the temp.pkl file is either in the sae location as DBinit.py, or in a file called setup which is located in the same location. If temp.pkl is in the same location and not in the setup folder, change this line of code in DBinit.py 
  txt_file = pickle.load(open('setup/temp.pkl', 'rb'))
  to txt_file = pickle.load(open('temp.pkl', 'rb'))
7. Now you can run DBinit.py. If no errors are thrown, then you have initialized your database.
8. Now, you can run the URLtraversal2.py program to update the prices of every item in your database to their current buy and sell price on the steam marketplace.
    We are in the progress of automating this update. 

