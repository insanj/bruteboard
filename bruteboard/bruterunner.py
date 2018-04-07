# bruteboard - created by julian weiss (c) 2018
# bruterunner.py - This is the topmost class that pulls together the brutemaker, helper, and client
from bruteboard import *

class bruterunner:
	def force(self, app_name="Firefox", cooldown=0.2):
		helper = brutehelper.brutehelper()
		helper_timestamp = helper.timestamp() # in case we want stats on total run time
		helper_string = helper.getUserInputString() # buffer key; press start to begin

		maker = brutemaker.brutemaker()
		maker_items = maker.make() # generates items; subclass or swap out to gen different items

		client = bruteclient.bruteclient(app_name) # optional param: app_name
		client.typeAndSendKeysWithCooldown(maker_items, cooldown) # optional param: cooldown (aka wait_time)
