# bruteboard - created by julian weiss (c) 2018
# bruteclient.py - This class manages the interface between Bruteboard ----> Windows 10
import win32com.client
import time

class bruteclient:
	app_name = None
	shell = None

	def __init__(self, app_name="Firefox"):
		self.app_name = app_name
		self.shell = win32com.client.Dispatch("WScript.Shell")

	def activate(self):
		self.shell.AppActivate(self.app_name)

	def type(self, key):
		self.shell.SendKeys(key)

	def send(self):
		self.type("{ENTER}")

	def wait(self, cooldown=0.2):
		time.sleep(cooldown)

	def typeAndSend(self, key):
		self.type(key)
		self.send()

	def typeAndSendKeys(self, keys):
		self.activate()
		for key in keys:
			self.typeAndSend(key)

	def typeAndSendKeysWithCooldown(self, keys, cooldown=0.2):
		self.activate()
		for key in keys:
			self.wait(cooldown)
			self.typeAndSend(key)
