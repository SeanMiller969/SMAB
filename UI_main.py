from tkinter import *

from tkinter import messagebox

class Window(Frame):

	#initialize the window and frame
	def __init__(self, master = None):
		Frame.__init__(self, master)

		self.master = master
		self.init_window()

	def init_window(self):
		self.master	.title("GUI")
		self.pack(fill=BOTH, expand=1)
		#create quit button

		menu = Menu(self.master)
		self.master.config(menu=menu)

		file = Menu(menu)
		file.add_command(label = "Exit", command=self.client_exit)

		menu.add_cascade(label = "File", menu=file)

		edit = Menu(menu)
		edit.add_command(label= "Show Text", command=self.showText)

		menu.add_cascade(label="Edit", menu=edit)

	def client_exit(self):
		exit()

	def showText(self):
		text = Label(self, text="SMAB SMAB SMAB User Interface")
		text.pack()


root = Tk()
root.geometry("400x600")

app = Window(root)
root.mainloop()