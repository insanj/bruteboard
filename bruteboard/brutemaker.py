# bruteboard - created by julian weiss (c) 2018
# brutemaker.py - This class generates data to send to the bruteclient (aka windows 10 apps)
class brutemaker:
	def make(self):
		all_the_items = []
		for i in range(0, 2000):
			all_the_items.append(str(i))

		return all_the_items
