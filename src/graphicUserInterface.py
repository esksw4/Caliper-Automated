import re, string, sys
import colorama
import collections
import time as time1

# import Login_Security
# import DashBoardPage
# import HiringStatusPage
# import OrderNewReport
from Order_New_Report import Test_Order1
import Functions
import unittest, time, re
import Tab

import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.simpledialog as dlg
class GUIFunctions:


	def allFieldCheck():
		if Functions.GUIdisplay.frameType == "ONR1":
			if len([v for v in Functions.OPLInfo.values() if v == '']) > 0 or (Functions.GUIdisplay.URL.get() == "empty"):
				# print(Functions.OPLINfo)
				return False
			else:
				# print(Functions.OPLINfo)
				Functions.GUIdisplay.User_Input_Frame_Frame.fullElement = True
				return True
		elif Functions.GUIdisplay.frameType == "ONR2":
			if len([v for v in Functions.CustomInfo.values() if v == '']) > 0:
				# print(Functions.OPLINfo)
				return False
			else:
				# print(Functions.OPLINfo)
				Functions.GUIdisplay.OPL_Input_Frame_Frame.fullElement = True
				return True

	def errorMessageCheck(arg):
		print(arg)
		if Functions.GUIdisplay.allFieldCheckAnswer == False:
			if typeName == "ONR1":
				if Functions.GUIallFieldError == None:
					Functions.GUIallFieldError = Label(Functions.GUIdisplay.GUIOPLErrorRow_Frame, text=labelText, fg='red', anchor='nw')
					Functions.GUIallFieldError.pack(side=TOP)


	def buttonPressCheck():
		if Functions.GUIdisplay.current_Button != None:
			# print(Functions.GUIdisplay.current_Button)
			if Functions.GUIdisplay.current_Button == "Order New Report":
				Functions.GUIdisplay.orderNewReport_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.User_Input_Frame_Frame.pack_forget()
				# Functions.GUIdisplay.ONR_GUIconsoleFrame.pack_forget()
				Functions.GUIdisplay.current_Button = None

			elif Functions.GUIdisplay.current_Button == "Hiring Status":
				Functions.GUIdisplay.hiringStatusPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
				Functions.GUIdisplay.current_Button = None

			elif Functions.GUIdisplay.current_Button == "Login_Security":
				Functions.GUIdisplay.loginSecurity_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.LS_LL_Frame.pack_forget()
				Functions.GUIdisplay.LS_PR_Frame.pack_forget()
				Functions.GUIdisplay.LS_PU_Frame.pack_forget()
				Functions.GUIdisplay.LS_LL_console_Frame.pack_forget()
				Functions.GUIdisplay.LS_PR_console_Frame.pack_forget()
				Functions.GUIdisplay.LS_PU_console_Frame.pack_forget()
				Functions.GUIdisplay.current_Button = None

			elif Functions.GUIdisplay.current_Button == "Dashboard":
				Functions.GUIdisplay.dashBoardPage_Button.config(bg=Functions.GUIdisplay.default_Color, relief=RAISED)
				Functions.GUIdisplay.myParent.config(bg=Functions.GUIdisplay.default_Color)
				Functions.GUIdisplay.current_Button = None

# relief FLAT == if frame does not contain no fields
# relief GROOVE == if frame CONTAINS all fields BUT NOT full entries
# relief RAISED == if frame CONTAINS all fields & full entries
class GUItkinter:
	def __init__(self, Parent):
		self.chooseTestFrame_Width = 100
		self.chooseTestFrame_Height = 450
		self.chooseTestButton_Height = 26
		self.chooseTestPlace_Yaxis = 173
		self.OPLInfoWidth_Width = 22
		self.betweeenFrame = 5

		self.OPLFrame_Dimension = '300x170'
		self.mainFrame_Dimension = '900x530'
		self.LS_Dimension = '875x525'

		self.default_Color = Parent.cget("bg")
		self.background_Color = "White"

		self.URL = StringVar(value="empty")

		self.allFieldError = None
		self.current_Button = None

		self.GUIuserInputErrorRow_Frame = Frame()

		self.myParent = Parent
		self.myParent.geometry(self.mainFrame_Dimension)
		self.myParent.title("Automated Smoke Test")

		self.mainTestingFrame()

		self.User_Input_Frame_Frame = tkinter.Frame(self.myParent)
		self.User_Input_Frame_Frame.existElement = False
		self.User_Input_Frame_Frame.fullElement = False

		self.OPL_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)
		# self.OPL_Input_Frame_Frame.existElement = False
		# self.OPL_Input_Frame_Frame.fullElement = False
		# self.OPL_Input_Frame_Frame.Error_Label = tkinter.Label()
		# self.OPL_Input_Frame_Frame.Error_Label.existElement = False

		self.Custom_Input_Frame_Frame = tkinter.Frame(self.User_Input_Frame_Frame, relief=FLAT)
		# self.Custom_Input_Frame_Frame.existElement = False
		# self.Custom_Input_Frame_Frame.Error_Label = tkinter.Label()
		# self.Custom_Input_Frame_Frame.Error_Label.existElement = False

	def mainTestingFrame(self):
		self.chooseTest_Frame = Frame(self.myParent,  width=self.chooseTestFrame_Width, height=self.chooseTestFrame_Height, bg=self.default_Color)
		self.chooseTest_Frame.pack(side=LEFT, fill=Y)
		self.chooseTest_Frame.existElement = True

		# self.loginSecurity_Button = tkinter.Button(self.chooseTest_Frame, text="Login_Security", command=self.loginSecurity, bg=self.default_Color)
		# self.loginSecurity_Button.pack()
		# self.loginSecurity_Button.place(y=self.chooseTestPlace_Yaxis, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.dashBoardPage_Button = tkinter.Button(self.chooseTest_Frame, text="Dashboard", command =self.dashBoard, bg=self.default_Color)
		# self.dashBoardPage_Button.pack()
		# self.dashBoardPage_Button.place(y=self.chooseTestPlace_Yaxis+self.chooseTestButton_Height, height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		# self.hiringStatusPage_Button = tkinter.Button(self.chooseTest_Frame, text="Hiring Status", command = self.hiringStatus, bg=self.default_Color)
		# self.hiringStatusPage_Button.pack()
		# self.hiringStatusPage_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*2), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

		self.orderNewReport_Button= tkinter.Button(self.chooseTest_Frame, text="Order New Report", relief=RAISED, command = self.ordernewReport, bg=self.default_Color)
		self.orderNewReport_Button.pack()
		self.orderNewReport_Button.place(y=self.chooseTestPlace_Yaxis+(self.chooseTestButton_Height*3), height=self.chooseTestButton_Height, width=self.chooseTestFrame_Width)

	def ordernewReport(self):
		self.background_Color = "lavender"
		GUIFunctions.buttonPressCheck()
		self.current_Button = "Order New Report"
		self.myParent.config(bg=self.background_Color)
		self.orderNewReport_Button.config(bg=self.background_Color, relief=FLAT)

		self.User_Input_Frame_Frame.config(bg=self.background_Color)
		self.User_Input_Frame_Frame.pack(side=LEFT)

		self.frameType = "ONR1"
		self.createTitle_Frame(self.OPL_Input_Frame_Frame, "Login Information:", 16)
		self.createErrorLabel(self.OPL_Input_Frame_Frame) 
		self.createRadioButton(self.OPL_Input_Frame_Frame, "Server", ["QA", "Production"], ["https://portal.caliperqaaws.com/", "https://portal.calipercorp.com/"])
		self.whichInfo = ["Email Address", "Email Password", "Portal Username", "Portal Password"]
		self.userInputFrame(self.OPL_Input_Frame_Frame)

		self.frameType = "ONR2"
		self.createTitle_Frame(self.Custom_Input_Frame_Frame, "Additional Information:", 16)
		self.createErrorLabel(self.Custom_Input_Frame_Frame)
		self.whichInfo = ["First Name","Last Name", "Email Address", "Job Title", "PO Box", "Cost Center", "Color", "Position Number", "Favorite Number", "Message to Consultant", "Message to Assessee", "Also Notify", "New Tag Name"]
		self.userInputFrame(self.Custom_Input_Frame_Frame)

		self.ONR_GUIconsoleFrame = tkinter.Frame(self.myParent)
		self.ONR_GUIconsoleFrame.existElement = False
		# self.conSoleFrame(self.ONR_GUIconsoleFrame, "ONR")
		
		self.whichInfo = []

	def OPLgetUserInputSendFunction(self):
		# print("Does it come here1")
		# if Functions.GUIallFieldError != None:
		# 	Functions.GUIallFieldError.pack_forget()

		dictValue = []

		if (self.OPL_Input_Frame_Frame.cget("relief") == GROOVE):
			print("Does it come here2")
			for f in self.OPLINfoEntry:
				dictValue.append(f.get())

			Functions.OPLInfo = collections.OrderedDict(zip(self.whichInfo, dictValue))
			self.allFieldCheckAnswer = GUIFunctions.allFieldCheck()
			GUIFunctions.errorMessageCheck(self.OPL_Input_Frame_Frame.Error_Label)

	def CustomgetUserInputSendFunction(self):
		# print("Does it come here3")
		# if Functions.GUIallFieldError != None:
		# 	Functions.GUIallFieldError.pack_forget()

		dictValue = []

		if (self.Custom_Input_Frame_Frame.cget("relief") == GROOVE):
			print("Does it come here4")
			for f in self.CustomInfo:
				dictValue.append(f.get())

			Functions.CustomInfo = collections.OrderedDict(zip(self.whichInfo, dictValue))
			self.allFieldCheckAnswer = GUIFunctions.allFieldCheck()
			print(self.Custom_Input_Frame_Frame.Error_Label)
			GUIFunctions.errorMessageCheck(self.Custom_Input_Frame_Frame.Error_Label)

	# used in "userInputFrame"
	def makeUserInputForm(self, arg):
		if self.frameType == "LS":
			labelanchorAs = W
			self.userInputWidth_Width = 16
			frameSideAs = LEFT

		elif self.frameType == "ONR1":
			labelanchorAs = 'center'
			enterButtonContinue = "Save"
			self.userInputWidth_Width = 23
			frameSideAs = TOP

			self.OPLINfoEntry = []
			for entry in self.whichInfo:	
				userInputRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
				userInputLabel_Label = tkinter.Label(userInputRow_Frame, width=self.userInputWidth_Width, text=entry, anchor=labelanchorAs, bg=self.background_Color)
				userInputEntry_Entry = tkinter.Entry(userInputRow_Frame)
				userInputRow_Frame.pack(side=frameSideAs, fill=X)
				userInputLabel_Label.pack(side=LEFT)
				userInputEntry_Entry.pack(side=RIGHT, expand=YES, fill=X)
				self.OPLINfoEntry.append(userInputEntry_Entry)
			arg.config(relief=GROOVE)
			userInputEnterRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
			userInputEnterRow_Frame.pack(side=TOP, fill=X)
			UserInputEnterButton = tkinter.Button(userInputEnterRow_Frame, text=enterButtonContinue, command =self.OPLgetUserInputSendFunction, relief=RAISED)
			UserInputEnterButton.pack(side=RIGHT)
			
		elif self.frameType == "ONR2":
			labelanchorAs = 'center'
			enterButtonContinue = "Save & Continue"
			self.userInputWidth_Width = 23
			frameSideAs = TOP

			self.CustomInfo = []
			for entry in self.whichInfo:	
				userInputRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
				userInputLabel_Label = tkinter.Label(userInputRow_Frame, width=self.userInputWidth_Width, text=entry, anchor=labelanchorAs, bg=self.background_Color)
				userInputEntry_Entry = tkinter.Entry(userInputRow_Frame)
				userInputRow_Frame.pack(side=frameSideAs, fill=X)
				userInputLabel_Label.pack(side=LEFT)
				userInputEntry_Entry.pack(side=RIGHT, expand=YES, fill=X)
				self.CustomInfo.append(userInputEntry_Entry)
			arg.config(relief=GROOVE)
			userInputEnterRow_Frame = tkinter.Frame(arg, bg=self.background_Color)
			userInputEnterRow_Frame.pack(side=TOP, fill=X)
			UserInputEnterButton = tkinter.Button(userInputEnterRow_Frame, text=enterButtonContinue, command =self.CustomgetUserInputSendFunction, relief=RAISED)
			UserInputEnterButton.pack(side=RIGHT)


		# print("end of makeUserInputForm")

	def userInputFrame(self, arg):
		arg.config(bg=self.background_Color)

		if self.background_Color == "light goldenrod yellow": 
			arg.pack(side=LEFT, fill=Y, padx=self.betweeenFrame, expand=0)
		else:
			arg.pack(side=TOP, fill=X, padx=self.betweeenFrame)

		if (arg.cget("relief") == FLAT):
			self.makeUserInputForm(arg)

	def createErrorLabel(self,arg):
		if (arg.cget("relief") == FLAT):
			arg.Error_Label = tkinter.Label(arg, text=" ", bg=self.background_Color, anchor = 'w', height=0, state=DISABLED)
			arg.Error_Label.pack(side=TOP, fill=X)

	def createRadioButton(self, arg, labelText, radioList, valueList):
		if (arg.cget("relief") == FLAT):
			if self.frameType == "ONR1":
				labelanchorAs = 'center'
				self.userInputWidth_Width = 23
				frameSideAs = TOP
				
				radioRow_Frame = Frame(arg, width=self.OPLInfoWidth_Width, bg=self.background_Color)
				radioRow_Frame.pack(side=frameSideAs, fill=X)
				radioLabel_Label = Label(radioRow_Frame, width=self.OPLInfoWidth_Width, text=labelText, anchor=labelanchorAs, bg=self.background_Color)
				radioLabel_Label.pack(side=LEFT)

				for radioText,valueText in zip(radioList, valueList):
					radioButton_Button = Radiobutton(radioRow_Frame, text=radioText, variable=self.URL, value=valueText, bg=self.background_Color)
					radioButton_Button.pack(side=LEFT)

	def createExtraBlankRow_Frame(self, arg, howMany):
		if (arg.existElement == False):
	 		for i in range(howMany):
	 			# extraRow_Frame= Frame(arg, bg=self.background_Color)
	 			# extraRow_Frame.pack(side=TOP, fill=X)
	 			extraRow_Label = Label(arg, bg=self.background_Color, text=" ")
	 			extraRow_Label.pack(side=LEFT, fill=X)

	def createTitle_Frame(self, arg, txt, fontSize):
		if (arg.cget("relief") == FLAT):
			title_Label = tkinter.Label(arg, bg=self.background_Color, text=txt, font=(fontSize), anchor='w')
			title_Label.pack(side=TOP, fill=X)

if Functions.GUImainFrame == None:
	Functions.GUImainFrame = Tk()
	Functions.GUIdisplay = GUItkinter(Functions.GUImainFrame)
	Functions.GUImainFrame.mainloop()