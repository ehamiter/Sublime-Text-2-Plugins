Sublime Text 2 Plugins
===============================================

This is just a handy place to store some plugins I use for ST2.


blame.py
========

blame.py is a Git blame plugin. It takes selected lines as arguments 
and outputs the data into the console.

![Blame screenshot](http://github.com/ehamiter/Sublime-Text-2-Plugins/blame.png "Blame in action")

Installation
------------

Copy **blame.py** into your ST2 User packages folder *(Sublime Text 2 > 
Preferences > Browse Packages... > User)*

Usage
-----

Select text or click desired line(s), then context (right) click. 
Choose "Blame..."

I've added this to my User Key Bindings, which works well (Command-Shift-B on a Mac):

    { "keys": ["super+shift+b"], "command": "blame" }
