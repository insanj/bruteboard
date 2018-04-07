# bruteboard - created by julian weiss (c) 2018
# brutehelper.py - This is a convenience wrapper class for command line I/O
import datetime

class brutehelper:
	def timestamp(self):
		return datetime.datetime.now()

	def prettyPrint(self, string):
		pretty_sep = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		pretty_rtn = "\n"
		pretty_composed = pretty_rtn + pretty_sep + pretty_rtn + string + pretty_rtn + pretty_sep
		return pretty_composed

	def prettyWelcomeString(self):
		welcome_string = "\t\twelcome to bruteboard v3"
		welcome_string += "\n\t(c) insanj 2018   github.com/insanj/bruteboard"
		welcome_string += "\n   see readme for details and how to customize bruteboard"
		return self.prettyPrint(welcome_string)

	def getUserInputString(self):
		print self.prettyWelcomeString()
		welcome_input_string = "\n\npress enter to begin..."
		input_text = raw_input(welcome_input_string)
		return input_text