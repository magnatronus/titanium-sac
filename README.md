
# Titanium Appcelerator Plug In for Sublime Text 3

The plug-in offers a number of features to help with the generation of a Titanium Project and Alloy Components. 

You can create  Classic and Alloy projects with the plug-in which also automatically creates a new Sublime Project and opens it (this opens as a new Sublime Window).

**This has only been developed and tested running on a MAC**


## Current Features

* Preset Titanium Project Settings
* Creation of Titanium Classic and Alloy projects
* Automatically create and open  a Titanium Sublime Project
* Create Alloy Controllers and Widgets
* Project Cleaning


## Project Config File

The project generation relies on the config file set up within the Plug-In structure (see below for an example of the one I am using). The setting relate to the options in the Ti CLI.
~~~
{
	"logLevel": "info",
	"appId": "uk.spiralarm",
	"sdk": "5.0.0.GA",
	"platforms": "ios,android",
	"url": "http://www.spiralarm.uk",
	"workspace" : "/sublimethree",
	"tiPath" : "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
}
~~~

* logLevel - the level you want to set for the project (see Ti help)
* appId - the base app id used when creating a project ( the prpject name is added to the end of this during creation)
* sdk - what SDK are you using
* platforms - the platforms that will be used when the project is generated
* url - Your web address to add to the project
* workspace - this is a directory(that MUST exist) whene the project will be created. (the dir needs to reside in you 'home' directory)
* tiPath - this is the path used for the Ti shell commands

NB: For tiPath you can use the shell command **echo $PATH** to see what path is set and used that.

This can be accessed, and modified using the Titanium->Config File menu option.

## Planned Work

* Create an associated build system (currently I do this in a command window with the Ti CLI)

## Installation

//TODO::


## Issues with Ti CLI

I have come across some issues when running various "flavours" of Titanium, usually showing as the infamous "longJohn" error. When this happens it was fixed by trying various installs of node versions to match the current Titaium set up, for example:

* Ti CLI 5.0.5 (using SDK5.0.2.GA and Alloy 1.5.1) - I installed Node v4.2.1 
* Ti CLI 3.4.2 (using SDK 3.5.1.GA and Alloy 1.5.1) - installed node V0.12.7

It was basically a suck it and see trial, as I could find no official list of environments/Ti CLI versions



## Acknowledgments

* Matt Tuttles Sublime Plug-in - https://github.com/MattTuttle/sublime-ti-build
* Everyone who shares their Sublime code on Github and beyond - a great way to learn and research

## MIT License

Copyright (C) 2015 Steve Rogers, SpiralArm Consulting Ltd

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.