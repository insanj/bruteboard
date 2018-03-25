import win32com.client
import pyperclip
import datetime
import time

# Step one: get all the items
class Bruteboard:
	init_timestamp = datetime.datetime.now()
	bruteboard_shell = win32com.client.Dispatch("WScript.Shell")

	def getBruteforceItems(self):
		all_the_items = []
		for i in range(0, 2000):
			all_the_items.append(str(i))

		return all_the_items

	# Step two: open up the correct app to paste the items
	def activeBruteforceApp(self, app_name):
		self.bruteboard_shell.AppActivate(app_name)

	# Step three (maybe): select the correct text field or wait for user to do so
	def waitForBruteforceAction(self, wait_time):
		time.sleep(wait_time)

	def typeBruteforceItem(self, item):
		self.bruteboard_shell.SendKeys(item)

	def sendBruteforceItem(self):
		self.bruteboard_shell.SendKeys("{ENTER}")

	def typeAndSendBruteforceItem(self, item):
		self.typeBruteforceItem(item)
		self.sendBruteforceItem()

	# Step four: loop through all items and paste them, then type ENTER, rinse & repeat
	def performBruteforce(self, app_name, wait_time):
		self.activeBruteforceApp(app_name)
		bruteforce_items = self.getBruteforceItems()
		for item in bruteforce_items:
			self.waitForBruteforceAction(wait_time)
			self.typeAndSendBruteforceItem(item)

class BruteboardHelper:
	def prettyPrint(self, string):
		pretty_sep = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		pretty_rtn = "\n"
		pretty_composed = pretty_rtn + pretty_sep + pretty_rtn + string + pretty_rtn + pretty_sep
		return pretty_composed

	def prettyWelcomeString(self):
		welcome_string = "\t\tWelcome to Bruteboard v2"
		welcome_string += "\n\t(c) insanj 2018   github.com/insanj/bruteboard"
		welcome_string += "\n   See README for details and how to customize bruteboard."
		return self.prettyPrint(welcome_string)

	def getUserInputString(self):
		print self.prettyWelcomeString()
		welcome_input_string = "\n\nPress ENTER to bruteforce..."
		input_text = raw_input(welcome_input_string)
		return input_text

class BruteboardRun:
	app_name = "Firefox"
	wait_time = 0.1

	def __init__(self, app_name, wait_time):
		self.app_name = app_name
		self.wait_time = wait_time

	def main(self):
		helper = BruteboardHelper()
		helper_string = helper.getUserInputString()

		bruteboard = Bruteboard()
		bruteboard.performBruteforce(self.app_name, self.wait_time) # app name, wait time

	if __name__ == "__main__":
		main()