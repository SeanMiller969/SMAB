from tkinter import *
from tkinter import messagebox

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

		cases_menu.menu.add_checkbutton(label="Gamma", variable=gamma)
		cases_menu.menu.add_checkbutton(label="Chroma", variable=chroma)
		cases_menu.menu.add_checkbutton(label="Wildfire", variable=wildfire)
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


root = Tk()
root.geometry("400x600")

app = Window(root)
root.mainloop()