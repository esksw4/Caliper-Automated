import re, string, sys
import colorama
import time as time1
import collections

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import tkinter
from tkinter import *

class Functions:
	global timeAfterLogin
	timeAfterLogin = 7

	global OPLInfo
	OPLInfo = collections.OrderedDict()

	global CustomInfo
	CustomInfo = collections.OrderedDict()

	global GUImainFrame
	GUImainFrame = None

	global GUIdisplay
	GUIdisplay = None

	global GUIEvaluationText
	GUIEvaluationText = None

	global GUIallFieldError
	GUIallFieldError = None

	# def checkForError(checkNumError, GUIdisplay.testName):
	# 	colorama.init(autoreset=True)
	# 	print(colorama.Fore.BLACK + colorama.Back.YELLOW + str(GUIdisplay.testName) + " with " + str(checkNumError) + " error(s).")

# Hiring Stauts
	# Used inside of "sortingCheck" function
	def compareAlphabeticOrder(f, l, mustbesmaller, mustbelarger):
		returnthis = 0
		if mustbesmaller == mustbelarger:
			returnthis = 1
			return returnthis
		elif ord(mustbesmaller[f][l]) == ord(mustbelarger[f][l]):   
			while l < min(len(mustbesmaller[f]), len(mustbelarger[f]))-1:
				l += 1
				whatReturned = Functions.compareAlphabeticOrder(f,l,mustbesmaller,mustbelarger)
				if whatReturned == 1:
	            #print('1')
					returnthis = 1
					return returnthis
				else:
	            #print('2')
					returnthis = 0
					return returnthis
			if len(mustbesmaller[f]) == len(mustbelarger[f]):
				if f == 0:
	            #print('3')
	            # print('assessee names are same')
					returnthis = 1
					return returnthis
				else:
	            #print('4')
					Functions.compareAlphabeticOrder(f-1,0,mustbesmaller,mustbelarger)
			elif len(mustbesmaller[f]) < len(mustbelarger[f]):
	          #print('5')
				returnthis = 1
				return returnthis
			else:
	          #print('6')
				returnthis = 0
				return returnthis
		elif ord(mustbesmaller[f][l]) < ord(mustbelarger[f][l]):
		    #print('7')
			returnthis = 1
			return returnthis
		elif ord(mustbesmaller[f][l]) > ord(mustbelarger[f][l]):
	        #print('8')
			returnthis = 0
			# automatedSmokeTest.GUIFunctions.outputDisplayConsole("First Name is not sorted correctly", Functions.GUIdisplay.testName,'se')
			return returnthis
		else:
			#print('9')
			returnthis = 0
			# automatedSmokeTest.GUIFunctions.outputDisplayConsole("Last Name is not sorted correctly", Functions.GUIdisplay.testName,'se')
			return returnthis
	    #print('10')
	    # return returnthis

	# Used inside of "sortingCheck" function, Test_SortingDropdown, Test_SearchForAssessee, Test_HiringFunction, Test_Filters
	def howmanyAssesseeListSystem(tableText):
	    tableText = re.split('\s+', tableText)
	    global systemAssessee, listAssessee
	    systemAssessee = int(tableText[5])
	    listAssessee = int(tableText[3]) - int(tableText[1]) + 1
	    return systemAssessee, listAssessee

	# Used in Test_SortingDropdown
	def sortingCheck(driver, whatToSort, sortColumn, listAssessee):
		from datetime import date
		from datetime import time 
		from datetime import datetime
		from datetime import timedelta
		
		i = 1
		if (whatToSort == 'Name'):
			while i < listAssessee:
				str_element = str("//table[@class='table cal-datagrid dataTable no-footer']/tbody/tr[%d]/td[%d]" %(i,sortColumn))
				mustbesmaller = driver.find_element_by_xpath(str_element).text.upper()
				# split the Firstname and Lastname
				# Firstname : mustbesmaller[0]
				# Lastname : mustbesmaller[1]
				mustbesmaller = re.split('\s+', mustbesmaller)
		        
				i = i+1
				str_element = str("//table[@class='table cal-datagrid dataTable no-footer']/tbody/tr[%d]/td[%d]" %(i,sortColumn))
				mustbelarger = driver.find_element_by_xpath(str_element).text.upper()
				# split the Firstname and Lastname
				# Firstname : mustbesmaller[0]
				# Lastname : mustbesmaller[1]
				mustbelarger = re.split('\s+', mustbelarger)

				typeSortWorks = Functions.compareAlphabeticOrder(1, 0, mustbesmaller, mustbelarger)
				print("alphabeticWorks", typeSortWorks)
				if (typeSortWorks != 1):
					# checkNumError += 1
					# colorama.init(autoreset=True)
					# print(colorama.Fore.RED + 'The row ' + str(i-1) + ' and ' + str(i) + ' are not sorted correctly')
					automatedSmokeTest.GUIFunctions.outputDisplayConsole("The row %d and %d are not sorted correctly" %(i-1, i), Functions.GUIdisplay.testName,'se')

				return typeSortWorks

		elif (whatToSort == 'Date'):
			while i < listAssessee:
				str_element = str("//table[@class='table cal-datagrid dataTable no-footer']/tbody/tr[%d]/td[%d]" %(i,sortColumn))
				mustbelarger = driver.find_element_by_xpath(str_element).text
				mustbelarger = datetime.strptime(mustbelarger, '%m/%d/%Y')
				i = i+1
				str_element = str("//table[@class='table cal-datagrid dataTable no-footer']/tbody/tr[%d]/td[%d]" %(i,sortColumn))
				mustbesmaller = driver.find_element_by_xpath(str_element).text
				mustbesmaller = datetime.strptime(mustbesmaller, '%m/%d/%Y')

				if (mustbelarger < mustbesmaller):
					automatedSmokeTest.GUIFunctions.outputDisplayConsole("The row %d and %d are not sorted correctly" %(i-1, i), Functions.GUIdisplay.testName,'se')
					typeSortWorks = 0
				else:
					typeSortWorks = 1
				return typeSortWorks

		elif (whatToSort == 'Supervisor'):
			tableText = driver.find_element_by_id("hiring-status-table_info").text
			systemAssessee, listAssessee = Functions.howmanyAssesseeListSystem(tableText)
	      
			if listAssessee != 100:
				driver.find_element_by_xpath("//select[@name='hiring-status-table_length']").click()
				time1.sleep(1)
				driver.find_element_by_xpath("//select[@name='hiring-status-table_length']").send_keys(Keys.ARROW_DOWN)
				driver.find_element_by_xpath("//select[@name='hiring-status-table_length']").send_keys(Keys.ARROW_DOWN)
				driver.find_element_by_xpath("//select[@name='hiring-status-table_length']").send_keys(Keys.ARROW_DOWN)
				time1.sleep(1)
				driver.find_element_by_xpath("//select[@name='hiring-status-table_length']").send_keys(Keys.ENTER)
				time1.sleep(2)
				tableText = driver.find_element_by_id("hiring-status-table_info").text
				systemAssessee, listAssessee = Functions.howmanyAssesseeListSystem(tableText)

				if (listAssessee != 100):
					automatedSmokeTest.GUIFunctions.outputDisplayConsole("Changing the number of entries of list is not working." , Functions.GUIdisplay.testName,'se')
					typeSortWorks = 0
					return typeSortWorks
	      
			while i < listAssessee:
				str_element = str("//table[@class='table cal-datagrid dataTable no-footer']/tbody/tr[%d]/td[%d]/div[1]/div[1]/span[1]" %(i,sortColumn))

				while driver.find_element_by_xpath(str_element).text == 'Supervisor not available':
					#print(driver.find_element_by_xpath(str_element).text)
					i += 1
					str_element = str("//table[@class='table cal-datagrid dataTable no-footer']/tbody/tr[%d]/td[%d]/div[1]/div[1]/span[1]" %(i,sortColumn))
				i = i-1;
				str_element = str("//table[@class='table cal-datagrid dataTable no-footer']/tbody/tr[%d]/td[%d]/div[1]/div[1]/span[1]" %(i,sortColumn))
				mustbesmaller = driver.find_element_by_xpath(str_element).text.upper()
				# split the Firstname and Lastname
				# Firstname : mustbesmaller[0]
				# Lastname : mustbesmaller[1]
				mustbesmaller = re.split('\s+', mustbesmaller)
	        
				if mustbesmaller[0] == 'SUPERVISOR':
					mustbesmaller.pop(1)

				i = i+1
				str_element = str("//table[@class='table cal-datagrid dataTable no-footer']/tbody/tr[%d]/td[%d]/div[1]/div[1]/span[1]" %(i,sortColumn))
				mustbelarger = driver.find_element_by_xpath(str_element).text.upper()
				# split the Firstname and Lastname
				# Firstname : mustbesmaller[0]
				# Lastname : mustbesmaller[1]
				mustbelarger = re.split('\s+', mustbelarger)

				#print('row ' + str(i-1) + ' vs ' + str(i))
				typeSortWorks = Functions.compareAlphabeticOrder(1, 0, mustbesmaller, mustbelarger)
				#print(alphabeticWorks)

				if typeSortWorks == 0:
					automatedSmokeTest.GUIFunctions.outputDisplayConsole("The row %d and %d are not sorted correctly" %(i-1, i), Functions.GUIdisplay.testName,'se')
				return typeSortWorks
		print("Come to this typeSortWorks")
		return typeSortWorks



	# Used in Test_Filters
	def checkStatusList(driver, listAssessee, filterStatus):
		whatStatus = driver.find_element_by_xpath("//tbody/tr[1]/td[5]/div[1]/div[@class='matchText status']").text
		if listAssessee == 1 and (whatStatus is filterStatus):
			return 1

		elif listAssessee == 1 and (whatStatus is not filterStatus):
			return 0
		else:
			check = 1
			for i in range(1, listAssessee+1):
				whatStatus = driver.find_element_by_xpath("//tbody/tr[%d]/td[5]/div[1]/div[@class='matchText status']" % (i)).text
				if whatStatus != filterStatus:
					check = 0
					return check
			return check

	# Used in Test_Filters
	def hiringButtonCheck(checkNumError, filterStatus):
		#print("checkNumError: " + str(checkNumError) + ",  FilterStatsu: " + filterStatus)
		if checkNumError > 0:
			colorama.init(autoreset=True)
			print(colorama.Fore.RED + filterStatus + str(" button doesn't work"))

	# Used in Test_Filters
	def hiringEmptyCheck(varToCheckIfEmpty,checkNumError):
		if varToCheckIfEmpty == []:
			checkNumError += 1
		return checkNumError

	# Used in Test_Filters
	def checkDateList(driver, checkNumError, listAssessee, tothis, fromthis):
	    checkdateinRange = driver.find_element_by_xpath("//tbody/tr[1]/td[3]//div[@class='second-line']").text
	    checkdateinRange = datetime.strptime(checkdateinRange, '%m/%d/%Y')
	    checkdateinRange = checkdateinRange.date()

	    if listAssessee == 1 and checkdateinRange >= fromthis and checkdateinRange <= tothis:
	      pass

	    elif listAssessee == 1 and (checkdateinRange <= fromthis or checkdateinRange >= tothis):
	      checkNumError += 1

	    else:
	      for i in range(1, listAssessee+1):
	        time1.sleep(1)
	        #print("i: " + str(i))
	        checkdateinRange = driver.find_element_by_xpath("//tbody/tr[%d]/td[3]//div[@class='second-line']" % (i)).text
	        checkdateinRange = datetime.strptime(checkdateinRange, '%m/%d/%Y')
	        checkdateinRange = checkdateinRange.date()

	        if checkdateinRange < fromthis or checkdateinRange > tothis :
	          checkNumError += 2
	      return checkNumError

	def findWhichRow(driver, byWhat, findValue, listAssessee):
		if byWhat == "Name": 
			row = 1
			time1.sleep(1)
			check = driver.find_element_by_xpath("//tbody/tr[%d]/td[4]/div[1]/div[@class='main-text assessee-name']" % row).text
			time1.sleep(1)
			while check != findValue and  row < listAssessee:
				row += 1
				check = driver.find_element_by_xpath("//tbody/tr[%d]/td[4]/div[1]/div[@class='main-text assessee-name']" % row).text
				time1.sleep(1)
				if row == listAssessee and check != findValue:
					row = 9999
			print()
			return row 

	# Used inside of "sortingCheck" function, Test_SortingDropdown, Test_SearchForAssessee, Test_HiringFunction, Test_Filters
	def hiringOPL(self):
		# print('Testing ', GUIdisplay.testName)
		driver = self.driver
		# System.setProperty(FirefoxDriver.SystemProperty.DRIVER_USE_MARIONETTE,"false");
		driver.get(GUIdisplay.URL.get())

		# print(1)
		if Functions.is_element_present(driver, By.CLASS_NAME, "text-center"):
			# print(2)
			if "This browser version is not supported." in driver.find_element_by_class_name("text-center").text:
				# print(3)
				# GUIdisplay.result.stop()
				GUIdisplay.OPL_Input_Frame_Frame.config(relief=GROOVE)
				# print(4)
				automatedSmokeTest.GUIFunctions.outputDisplayConsole("Please update the browser. Your Browser is not supported",GUIdisplay.testName, 'se')
				# print(5)
				driver.quit()
		else:
			# print(6)
			driver.find_element_by_id("user_email").clear()
			# print(7)
			# print("OPLInfo['Portal Username']: ", OPLInfo['Portal Username'])
			driver.find_element_by_id("user_email").send_keys(OPLInfo['Portal Username'])
			# print(8)
			# type User Password
			driver.find_element_by_id("user_password").clear()
			# print(9)
			driver.find_element_by_id("user_password").send_keys(OPLInfo['Portal Password'])
			# print(10)
			# click Ente
			driver.find_element_by_id("login-btn").click()
			# print(11)
			time1.sleep(timeAfterLogin)

			# print(12)
			if Functions.is_element_present(driver, By.CLASS_NAME, "alert.alert-error") or Functions.is_element_present(driver, By.CLASS_NAME, "alert.alert-alert"):
				# GUIdisplay.result.stop()
				# print(14)
				# print(Functions.is_element_present(driver, By.CLASS_NAME, "alert.alert-error"))
				# print(1)
				GUIdisplay.OPL_Input_Frame_Frame.config(relief=GROOVE)
				# print(2)
				# print(15)
				driver.quit()
				automatedSmokeTest.GUIFunctions.outputDisplayConsole("Please check user's email address/password.", GUIdisplay.testName, 'ie')
				# print(16)
				# print(3)
				
				# print(17)
				# print(4)
			else: 
				# print(18)
				time1.sleep(2)
				# print(19)
				driver.find_element_by_link_text("Hiring Status").click()
				time1.sleep(2)
				check = driver.title
				if check != "Caliper: Hiring Status":
					automatedSmokeTest.GUIFunctions.outputDisplayConsole("Hiring Status Button DOES NOT directs you to its page.", Functions.GUIdisplay.testName,'se')
				else:
					time1.sleep(2)
					return driver

	# Used inside of function "OPL"
	def is_element_present(driver, how, what):
	    try:
	      driver.find_element(by=how, value=what)
	    except NoSuchElementException as e:
	      return False
	    return True

	def OPL(self):
		import automatedSmokeTest

		# print('Testing ', GUIdisplay.testName)
		# print(GUIdisplay.URL.get())
		driver = self.driver
		# System.setProperty(FirefoxDriver.SystemProperty.DRIVER_USE_MARIONETTE,"false");
		driver.get(GUIdisplay.URL.get())

		# print(1)
		if Functions.is_element_present(driver, By.CLASS_NAME, "text-center"):
			# print(2)
			if "This browser version is not supported." in driver.find_element_by_class_name("text-center").text:
				# print(3)
				# GUIdisplay.result.stop()
				GUIdisplay.OPL_Input_Frame_Frame.config(relief=GROOVE)
				# print(4)
				automatedSmokeTest.GUIFunctions.outputDisplayConsole("Please update the browser. Your Browser is not supported",GUIdisplay.testName, 'se')
				# print(5)
				driver.quit()
		else:
			# print(6)
			driver.find_element_by_id("user_email").clear()
			# print(7)
			# print("OPLInfo['Portal Username']: ", OPLInfo['Portal Username'])
			driver.find_element_by_id("user_email").send_keys(OPLInfo['Portal Username'])
			# print(8)
			# type User Password
			driver.find_element_by_id("user_password").clear()
			# print(9)
			driver.find_element_by_id("user_password").send_keys(OPLInfo['Portal Password'])
			# print(10)
			# click Ente
			driver.find_element_by_id("login-btn").click()
			# print(11)
			time1.sleep(timeAfterLogin)

			# print(12)
			if Functions.is_element_present(driver, By.CLASS_NAME, "alert.alert-error") or Functions.is_element_present(driver, By.CLASS_NAME, "alert.alert-alert"):
				# GUIdisplay.result.stop()
				# print(14)
				# print(Functions.is_element_present(driver, By.CLASS_NAME, "alert.alert-error"))
				# print(1)
				GUIdisplay.OPL_Input_Frame_Frame.config(relief=GROOVE)
				# print(2)
				# print(15)
				driver.quit()
				automatedSmokeTest.GUIFunctions.outputDisplayConsole("Please check user's email address/password.", GUIdisplay.testName, 'ie')
				# print(16)
				# print(3)
				
				# print(17)
				# print(4)
			else: 
				# print(18)
				time1.sleep(2)
				# print(19)
				return driver




#########################WAIT UNTIL THE DRIVER FIND THE ELEMENT
# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "C29_W35_V37_V46_btresporg_struct.partner_no-btn")))
#     driver.find_element_by_id("C29_W35_V37_V46_btresporg_struct.partner_no-btn").click()
# except TimeoutException:
#     print("C29_W35_V37_V46_btresporg_struct.partner_no-btn not found")