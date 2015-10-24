
#
# ti-sac.py is a Titanium plug-in for Sublime Text 3
#
# developed by Steve Rogers, SpiralArm Consulting Ltd (www.spiralarm.uk)
# @sarmcon
#
#
import sublime, sublime_plugin, os
import Titanium.lib.tiutils as Ti


# This will create a new Alloy Widget
class sacAlloyWidgetCommand(sublime_plugin.WindowCommand):

	def run(self,paths=[]):
		if len(paths) > 0 and self.window.active_view():
			self.projectDir = paths[0]
			self.window.active_view().window().show_input_panel("Widget name:", '',self.createWidget, None, None)
			
	def createWidget(self, name):
		Ti.createAlloyWidget(self.projectDir + "/app", name)


# This will create a new Alloy Controller
class sacAlloyControllerCommand(sublime_plugin.WindowCommand):

	def run(self,paths=[]):
		if len(paths) > 0 and self.window.active_view():
			self.projectDir = paths[0]
			self.window.active_view().window().show_input_panel("Controller name:", '',self.createController, None, None)
			
	def createController(self, name):
		Ti.createAlloyController(self.projectDir + "/app", name)



# This will clean the current project
class sacCleanProjectCommand(sublime_plugin.WindowCommand):

	def run(self,paths=[]):
		if len(paths) > 0:
			Ti.cleanProject(paths[0])


# This will create a Titanium Alloy Project
class sacCreateAlloyCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		# ask for the App name
		self.view.window().show_input_panel("Project name:", 'test',self.createProjectFiles, None, None)
		#self.createProjectFiles("alloytest") #- test version that just creates the specified project


	def createProjectFiles(self, projectName):

		# Turn the console on
		sublime.active_window().run_command("show_panel", {"panel": "console", "toggle": True})

		# Define the project meta data and the proposed directory
		self.projectDir = Ti.getProjectDirectory(projectName)
		Ti.consolePrint("","\n--------------------------------------------------------------------------------------------------")
		Ti.consolePrint("info", "Creating Project: %s  in %s................." % (projectName,self.projectDir))
		
		# If dir exists  then DONT create project
		if os.path.exists(self.projectDir):
			sublime.error_message("Unable to create Titanium project, the directory already exists: %s " % self.projectDir)
		else:

			# Step 1 - First Step Create Titanium skeleton project
			Ti.createClassicProject(projectName)

			# Step 2 - Now Generate the Alloy Bit	
			Ti.generateAlloyProject(self.projectDir)
	
			# Step 3 - Now Create the sublime Project files
			Ti.consolePrint('info', "Generating Sublime Project....")
			Ti.createSublimeProject(self.projectDir)

			# Step 4 Finally open the project (opens in a new sublime instance)
			os.system("open %s" % self.projectDir+".sublime-project")

			# Step 4a - possible add the project to the recent project list so it can be opened with Open Recent or Quick Project Switch
			#TODO::


# This will create a Titanium Classic Project
class sacCreateCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		# ask for the App name
		self.view.window().show_input_panel("Project name:", 'test',self.createProjectFiles, None, None)
		#self.createProjectFiles("test") #- test version that just creates the specified project


	def createProjectFiles(self, projectName):

		# Turn the console on
		sublime.active_window().run_command("show_panel", {"panel": "console", "toggle": True})

		# Define the project meta data and the proposed directory
		self.projectDir = Ti.getProjectDirectory(projectName)
		Ti.consolePrint("","\n--------------------------------------------------------------------------------------------------")
		Ti.consolePrint("info", "Creating Project: %s  in %s................." % (projectName,self.projectDir))
		
		# If dir exists  then DONT create project
		if os.path.exists(self.projectDir):
			sublime.error_message("Unable to create Titanium project, the directory already exists: %s " % self.projectDir)
		else:
			# Step 1 - Create Titanium skeleton project
			Ti.createClassicProject(projectName)
	
			# Step 2 - Now Create the sublime Project files
			Ti.consolePrint('info', "Generating Sublime Project....")
			Ti.createSublimeProject(self.projectDir)

			# Step 3 Finally open the project (opens in a new sublime instance)
			os.system("open %s" % self.projectDir+".sublime-project")

			# Step 3a - possible add the project to the recent project list so it can be opened with Open Recent or Quick Project Switch
			#TODO::

# This will open the Plugin - config file
class sacEditConfigCommand(sublime_plugin.TextCommand):

	def run(self,edit):
		open_file_settings('titanium-sac.sublime-settings')			

