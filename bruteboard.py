import win32com.client
import pyperclip
import time

# Step one: get all the items
all_the_items = []
for i in range(0, 2000):
	all_the_items.append(str(i))

# Step two: open up the correct app to paste the items
shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate("Firefox")

# Step three (maybe): select the correct text field or wait for user to do so

# Step four: loop through all items and paste them, then type ENTER, rinse & repeat
for item in all_the_items:
	shell.SendKeys(item)
	shell.SendKeys("{ENTER}")
	time.sleep(0.1)

print("Done!")
