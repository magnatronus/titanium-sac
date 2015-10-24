#
# tiutils.py is a Titanium function library for use with the SpiralArm Titanium plug-in for Sublime Text 3
#
# developed by Steve Rogers, SpiralArm Consulting Ltd (www.spiralarm.uk)
# @sarmcon
#
#

import sublime, subprocess,os
from os.path import expanduser



# read in our default Titanium settings
settings 	= sublime.load_settings('titanium-sac.sublime-settings')
LOGLEVEL    = settings.get("logLevel", "info")
PLATFORMS	= settings.get("platforms", "ios,android")
URL			= settings.get("url", "http://www.mywebaddress")
SDK       	= settings.get("sdk", "5.0.0.GA")
workSpace	= settings.get("workspace", "/")
tiPath		= settings.get("tiPath", "")
rootAppId 	= settings.get("appId", "com.myapp")


# set up some other useful vars
home 			= expanduser("~")
new_env 		= os.environ.copy()
new_env['PATH'] = new_env['PATH']+ ":" + tiPath
WORKSPACEDIR	= home + workSpace

# Run a Ti based shell command
def runCommand(params):
	subprocess.Popen(params, env=new_env).wait()


# Print out a console message
def consolePrint(label, message):
	print("%s> %s" % (label,message))


# Generate our application id
def getAppId(projectName):
	return rootAppId + "." + projectName


# Generate our fully qualified project name
def getProjectDirectory(projectName):
	return home + workSpace + "/" + projectName

# Create a classic project
def createClassicProject(projectName):
	consolePrint('info', "Creating Titanium Project....")
	runCommand(['ti', "create", "--force","--type", "app", "--sdk", SDK,  "--id", getAppId(projectName), "--log-level", LOGLEVEL, "--name", projectName, "--workspace-dir", WORKSPACEDIR,"--platform", PLATFORMS, "--url", URL])

# Add the Alloy Files
def generateAlloyProject(projectDir):
	consolePrint('info', "Generating Alloy Files....")
	subprocess.Popen(['alloy', "new", projectDir, "--force"], env=new_env).wait()

# Clean the current project
def cleanProject(projectDir):
	consolePrint('info', "Cleaning Project....")
	subprocess.Popen(['ti', "clean", "--project-dir", projectDir, "--log-level", LOGLEVEL, "--platforms", PLATFORMS], env=new_env).wait()

# Add an Alloy widget to the project
def createAlloyWidget(path, name):
	consolePrint('info', "Creating Widget %s...." % name)
	subprocess.Popen(['alloy', "generate", "widget", name, "--outputPath", path], env=new_env).wait()



# Add an Alloy controller to the project
def createAlloyController(path, name):
	consolePrint('info', "Creating Controller %s...." % name)
	subprocess.Popen(['alloy', "generate", "controller", name, "--outputPath", path], env=new_env).wait()

# Create the Sublime Project File
def createSublimeProject(projectDir):
	content = '{"folders":[{"path": "%s"}]}' % projectDir
	projectFile = open(projectDir+".sublime-project","w")	
	projectFile.write(content);
	projectFile.close()

