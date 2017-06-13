###################################################
# Tabbed interface script
# www.sunjay-varma.com
###################################################

__doc__ = info = '''
# This script was written by Sunjay Varma - www.sunjay-varma.com

# This script has two main classes:
# Tab - Basic tab used by TabBar for main functionality
# TabBar - The tab bar that is placed above tab bodies (Tabs)

# It uses a pretty basic structure:
# root
# -->TabBar(root, init_name) (For switching tabs)
# -->Tab    (Place holder for content)
# 	\t-->content (content of the tab; parent=Tab)
# -->Tab    (Place holder for content)
# 	\t-->content (content of the tab; parent=Tab)
# -->Tab    (Place holder for content)
# 	\t-->content (content of the tab; parent=Tab)
# etc.
# '''

import tkinter
import Functions
from tkinter import *

BASE = RAISED
SELECTED = SUNKEN

# a base tab class
class Tab(Frame):
	def __init__(self, master, name):
		Frame.__init__(self, master)
		self.tab_name = name

# the bulk of the logic is in the actual tab bar
class TabBar(Frame):
	def __init__(self, master=None, init_name=None, testName=None):
		Frame.__init__(self, master)
		self.tabs = {}
		self.buttons = {}
		self.current_tab = None
		self.init_name = init_name
		self.testName = testName
	
	def show(self):
		#self.pack(side=TOP, expand=YES, fill=X)
		self.grid(sticky='w')
		self.switch_tab(self.init_name or self.tabs.keys()[-1])# switch the tab to the first tab
	
	def add(self, tab):
		tab.grid_forget()									# hide the tab on init
		
		self.tabs[tab.tab_name] = tab						# add it to the list of tabs
		print("tab.tab_name: ", tab.tab_name)
		b = Button(self, text=tab.tab_name, relief=BASE,	# basic button stuff
			command=(lambda name=tab.tab_name: self.switch_tab(name)))	# set the command to switch tabs
		b.pack(side=LEFT)												# pack the buttont to the left mose of self

		if tab.tab_name == "Console":
			Functions.GUIdisplay.consoleTab[self.testName] = [Functions.GUIdisplay.consoleTab[self.testName][0], Text(master=self.tabs[tab.tab_name], width=Functions.GUIdisplay.consoleTextWidth, height=Functions.GUIdisplay.consoleTextHeight, wrap=WORD)]   # pack the buttont to the left mose of self
			Functions.GUIdisplay.consoleTab[self.testName][1].focus()
			Functions.GUIdisplay.consoleTab[self.testName][1].grid(sticky='w')
			# Functions.GUIdisplay.textConsole_Text.place(x=3, y=1)
		elif tab.tab_name == "Evaluation":
			Functions.GUIdisplay.consoleTab[self.testName] = [Text(master=self.tabs[tab.tab_name], width=Functions.GUIdisplay.consoleTextWidth, height=Functions.GUIdisplay.consoleTextHeight ,wrap=WORD)]   # pack the buttont to the left mose of self
			Functions.GUIdisplay.consoleTab[self.testName][0].focus()
			Functions.GUIdisplay.consoleTab[self.testName][0].grid(sticky='w')
			# Functions.GUIdisplay.textEvaluation_Text.place(x=3, y=1)

		self.buttons[tab.tab_name] = b									# add it to the list of buttons

	
	def delete(self, tabname):
		if tabname == self.current_tab:
			self.current_tab = None
			self.tabs[tabname].pack_forget()
			del self.tabs[tabname]

			if tabname == "Console":
				Functions.GUIdisplay.consoleTab[self.testName][1].grid_forget()
				del Functions.GUIdisplay.consoleTab[self.testName][1]
			elif tab_name == "Evaluation":
				Functions.GUIdisplay.consoleTab[self.testName][0].grid_forget()
				del Functions.GUIdisplay.consoleTab[self.testName][0]

			self.switch_tab(self.tabs.keys()[0])
		
		else:
			del self.tabs[tabname]
			if tabname == "Console":
				del Functions.GUIdisplay.consoleTab[self.testName][1]
			elif tab_name == "Evaluation":
				del Functions.GUIdisplay.consoleTab[self.testName][0]
		
		self.buttons[tabname].pack_forget()
		del self.buttons[tabname] 
		
	
	def switch_tab(self, name):
		if self.current_tab:
			self.buttons[self.current_tab].config(relief=BASE)
			self.tabs[self.current_tab].grid_forget()			# hide the current tab
			# self.tabs[self.current_tab].forget()
			if name == "Console":
				Functions.GUIdisplay.consoleTab[self.testName][1].grid_forget()
			elif name == "Evaluation":
				Functions.GUIdisplay.consoleTab[self.testName][0].grid_forget()

		# self.tabs[name].pack(side=BOTTOM)							# add the new tab to the display
		self.tabs[name].grid(sticky='w')

		if name == "Console":
			Functions.GUIdisplay.consoleTab[self.testName][1].grid(sticky='w')
		elif name == "Evaluation":
			Functions.GUIdisplay.consoleTab[self.testName][0].grid(sticky='w')

		self.current_tab = name									# set the current tab to itself
		
		self.buttons[name].config(relief=SELECTED)					# set it to the selected style
			
# if __name__ == '__main__':
# 	def write(x):
# 		print(x)
		
# 	root = Tk()
# 	root.title("Tabs")
	
# 	bar = TabBar(root, "Info")
	
# 	tab1 = Tab(root, "Wow...")				# notice how this one's master is the root instead of the bar
# 	Label(tab1, text="Sunjay Varma is an extra ordinary little boy.\n\n\n\n\nCheck out his website:\nwww.sunjay-varma.com", bg="white", fg="red").pack(side=TOP, expand=YES, fill=BOTH)
# 	Button(tab1, text="PRESS ME!", command=(lambda: write("YOU PRESSED ME!"))).pack(side=BOTTOM, fill=BOTH, expand=YES)
# 	Button(tab1, text="KILL THIS TAB", command=(lambda: bar.delete("Wow..."))).pack(side=BOTTOM, fill=BOTH, expand=YES)
	
# 	tab2 = Tab(root, "Hi there!")
# 	Label(tab2, text="How are you??", bg='black', fg='#3366ff').pack(side=TOP, ifll=BOTH, expand=YES)
# 	txt = Text(tab2, width=50, height=20)
# 	txt.focus()
# 	txt.pack(side=LEFT, fill=X, expand=YES)
# 	Button(tab2, text="Get", command=(lambda: write(txt.get('1.0', END).strip()))).pack(side=BOTTOM, expand=YES, fill=BOTH)

# 	tab3 = Tab(root, "Info")
# 	Label(tab3, bg='white', text="This tab was given as an argument to the TabBar constructor.\n\nINFO:\n"+info).pack(side=LEFT, expand=YES, fill=BOTH)
	
# 	bar.add(tab1)                   # add the tabs to the tab bar
# 	bar.add(tab2)
# 	bar.add(tab3)

# 	#bar.config(bd=2, relief=RIDGE)			# add some border
	
# 	bar.show()
	
# 	root.mainloop()
