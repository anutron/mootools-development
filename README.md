MooTools Development Environment
--------------------------------

This repo contains a set of hashes designed to allow you to get a MooTools development sandbox up and running quickly. It uses a python virtual environment to install itself; it does not modify your system in any way outside the repository in which you install it.

Requirements:
* [python](http://www.python.org/)
* git (obviously)

Setup
=====

	$ git clone {your fork of this repo}
	$ cd mootools-development
	$ ./install //installs everything; takes about 3 or 4 minutes
	$ ./go depender //checks dependencies
	$ ./go run //runs the server

Then open http://localhost:9876 in your browser.

Commands
========
After you run `./install`, execute `./go` you'll get a menu prompting you for actions. The available options are:

* depender - checks js dependencies; aka `./go d`
* sync - synchronizes external libraries; aka `./go s`
* run - runs the server on port 9876; aka `./go r`
* live - runs the server on port 80; NOT in DEBUG mode, so it's faster because it caches the JS; aka `./go l`
