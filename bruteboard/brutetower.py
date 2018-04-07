# bruteboard - created by julian weiss (c) 2018
# brutetower.py - This class acts as a watchtower and provides apps already running on Windows
import psutil
import os
import psutil

class brutetower:
	shell = None

	def __init__(self):
		self.shell = win32com.client.Dispatch("WScript.Shell")

	def observe():
		return []

	# https://stackoverflow.com/a/2241047
	def find_procs_by_name(name):
		"Return a list of processes matching 'name'."
		assert name, name
		ls = []
		for p in psutil.process_iter():
			name_, exe, cmdline = "", "", []
			try:
				name_ = p.name()
				cmdline = p.cmdline()
				exe = p.exe()
			except (psutil.AccessDenied, psutil.ZombieProcess):
				pass
			except psutil.NoSuchProcess:
				continue
			if name == name_ or cmdline[0] == name or os.path.basename(exe) == name:
				ls.append(name)
		return ls