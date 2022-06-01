import sublime
import sublime_plugin
import os, sys, time
from subprocess import check_output as cmd


class ExploreCommand(sublime_plugin.WindowCommand):
	"""
	Gets the active file in the view and opens it in the host explorer.
	"""

	def run(self):
		# Store current path
		startpath = os.path.abspath(os.curdir)
		# Get the name of the file in sublime and its path
		fullname = self.get_file_name()
		targetpath = self.get_path_from_file(fullname)
		# Store the command to run
		foldercmd = 'explorer {}'.format(targetpath)
		# Open the explorer in the desired folder
		cmd(foldercmd, shell=False)
		return

	def get_file_name(self):
		"""
		Gets the active file.
		"""
		win = sublime.active_window()
		sht = win.active_sheet()
		fullname = sht.file_name()
		return fullname



	def get_path_from_file(self, filename):
		"""
		Gets the path from the file.
		"""
		pathname = filename[:filename.rindex('\\')]
		return pathname

