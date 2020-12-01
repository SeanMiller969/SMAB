from bs4 import BeautifulSoup
from urllib.request import urlopen
from search_id import *
from url_traversal import get_json
from tkinter import *
from tkinter import messagebox
import csv
import time
from Weapon import *
import os

class Window(Frame):

	#initialize the window and frame
	def __init__(self, master = None):
		Frame.__init__(self, master)

		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("GUI")
		self.pack(fill=BOTH, expand=1)
		
		menu_bar = Menu(self.master)
		self.master.config(menu=menu_bar)

		title = Label(self, text="Steam Market Analysis Bot", font=25)
		title.pack()
		
		#case menu 
		cases_menu = Menubutton(self, text="Cases", relief=RAISED)
		cases_menu.menu = Menu(cases_menu, tearoff=0)
		cases_menu["menu"] = cases_menu.menu
	
		gamma = IntVar()
		chroma = IntVar()
		wildfire = IntVar()

		cases_menu.menu.add_checkbutton(label="Gamma", variable=gamma, command=self.caseOnClick)
		cases_menu.menu.add_checkbutton(label="Chroma", variable=chroma, command=self.caseOnClick)
		cases_menu.menu.add_checkbutton(label="Wildfire", variable=wildfire, command=self.caseOnClick)
		cases_menu.pack()
		
		#quit button
		file = Menu(menu_bar, tearoff=0)
		file.add_command(label = "Exit", command=self.client_exit)

		menu_bar.add_cascade(label = "File", menu=file)

		edit = Menu(menu_bar, tearoff=0)
		edit.add_command(label= "Show Text", command=self.showText)

		menu_bar.add_cascade(label="Edit", menu=edit)

		help_tab = Menu(menu_bar, tearoff=0)
		help_tab.add_command(label="Read This", command=self.showHelp)
		menu_bar.add_cascade(label="Help", menu=help_tab)

		
	def client_exit(self):
		exit()

	def showText(self):
		text = Label(self, text="SMAB SMAB SMAB User Interface")
		text.pack()

	def showHelp(self):
		fulltext = "The quit button is located under the file dropdown menu."
		text = Label(self, text=fulltext)
		text.pack()

	def caseOnClick(self):
		caseClickAction()


def caseClickAction():
	url = find_case("The Gamma Collection")
	if(url == "ERROR"):
		print("Case not found!")
	print(url)
	#going through all the links should pass back a list of skin objects
	#eventually we will intialize the list of case objects.
	JSON = []
	NumberOfPages = 7
	for i in range(NumberOfPages):
		JSON.append(get_json(url[:len(url) - 11] + str(i) + url[len(url) - 10:]))
		time.sleep(3)
		i += 1
	#Pipe out to a csv
	f = open("EV.csv", "w+")
	f.close()
	print(len(JSON))
	with open('EV.csv', 'wt') as f:
		csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
		csv_writer.writerow(["Gun","skin","condition","stat_track","buy_price","sell_price", "estimated_value"])
		for j in JSON:
			for i in j:
				csv_writer.writerow(i.CSVstructure())
		csv_writer.writerow(["=Sum(F3:F" + str((NumberOfPages * 2 * 10) + 1) + ")"])

		#opening the file
		dir = os.path.abspath(os.getcwd())
		os.startfile(dir + "\\EV.csv")

def main():
	print("Welcome to SMAB")
	#do a case match
	#case = input("Enter case you want to look at: ")
	#determine which case this is and get the correct url.
	#cases have an id tag associated with them in the url
	#tag_set_community_13 <-- this is that tag number
	#this will be hard coded and will be updated accordinginly

	root = Tk()
	root.geometry("400x600")
	app = Window(root)
	root.mainloop()


if __name__ == "__main__":
	main()