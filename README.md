Sublime Text 2 Plugins
===============================================

This is just a handy place to store some plugins I wrote for ST2.

[blame.py][]
[pep8check.py][]


---

[blame.py]
========

blame.py is a Git blame plugin. It takes selected lines as arguments and outputs the data into the console.

![blame screenshot](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/blame.png)


Installation
------------

Copy **[blame.py](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/blame.py)** into your ST2 User packages folder *(Sublime Text 2 > Preferences > Browse Packages... > User)*


Usage
-----

Select text or click desired line(s), then activate. 

I've added this to my User Key Bindings (Command-Shift-B on a Mac):

    { "keys": ["super+shift+b"], "command": "blame" }

...and this in Default/Context.sublime-menu, which allows context menu access:

    { "command": "blame", "caption": "Blame…" }


---

[pep8check.py]
============

pep8check.py is a [PEP 8 style guide](http://www.python.org/dev/peps/pep-0008/) plugin. It uses another Python program called [pep8.py](http://pypi.python.org/pypi/pep8) that you can install in a few ways:


Installation
------------

Copy **[pep8check.py](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/pep8check.py)** into your ST2 User packages folder *(Sublime Text 2 > Preferences > Browse Packages... > User)*

**This plugin is dependent on pep8, which you must install yourself.** You can install, upgrade, uninstall pep8.py with these commands:

    $ sudo pip install pep8
    $ sudo pip install --upgrade pep8
    $ sudo pip uninstall pep8

Or if you don't have pip:

    $ sudo easy_install pep8

There's also a package for Debian/Ubuntu, but it's not always the latest version:

    $ sudo apt-get install pep8


Usage
-----

I've added this to my User Key Bindings (Command-Shift-8 on a Mac):
    
    { "keys": ["super+shift+8"], "command": "pep8_check" }

...and this in Default/Context.sublime-menu, which allows context menu access:

    { "command": "pep8_check", "caption": "PEP8" }
