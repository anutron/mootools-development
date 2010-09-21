MooTools Development Environment
--------------------------------

This repo contains a set of hashes designed to allow you to get a MooTools development sandbox up and running quickly. It has a few dependencies listed below, but after you have those sorted it should be easy to get things running.

Requirements:
* [crepo](http://github.com/cloudera/crepo) - this is used to manage the submodules
* [virtualenv](http://pypi.python.org/pypi/virtualenv) - see note below on how to install this on OSX
* [python](http://www.python.org/)
* git (obviously)

Installation
============

To install virtualenv on OSX, [follow these instructions](http://www.fprimex.com/coding/pymac.html):

	# Install easy_install and virtualenv into the system wide python package dir
	$ curl -O http://peak.telecommunity.com/dist/ez_setup.py > ez_setup.py
	$ sudo python ez_setup.py
	$ sudo easy_install virtualenv
	$ rm ez_setup.py

To install crepo on OSX:

	# follow the instructions above to install easy_install, then:
	$ easy_install crepo

Setup
=====

	$ git clone {your fork of this repo}
	$ cd mootools-development
	$ ./go install //installs everything; takes about 3 or 4 minutes
	$ ./go depender //checks dependencies
	$ ./go run //runs the server

Then open http://localhost:9876 in your browser.

Commands
========
If you just execute `./go` you'll get a menu prompting you for actions. The available options are:

* install - installs everything; you can also just type `./go i`
* depender - checks js dependencies; aka `./go d`
* sync - synchronizes external libraries; aka `./go s`
* run - runs the server on port 9876; aka `./go r`