Sublime Text 2 Plugins
===============================================

This is just a handy place to store some plugins I wrote for ST2.


blame.py
========

blame.py is a Git blame plugin. It takes selected lines as arguments and outputs the data into the console.

![blame screenshot](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/blame.png)


Installation
------------

Copy **[blame.py](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/blame.py)** into your ST2 User packages folder *(Sublime Text 2 > Preferences > Browse Packages... > User)*


Usage
-----

Select text or click desired line(s), then activate. 

I've added this to my User Key Bindings (command-alt-b on a Mac):

    { "keys": ["super+alt+b"], "command": "blame" }

...and this in User/Default\_(your OS)\_Context.sublime-menu, which allows context menu access:

    { "command": "blame", "caption": "Blame…" }


googleIt.py
===========

googleIt.py is a Google looker-upper. It takes the scope of the file and appends it to a Google search of either the word under the cursor or the selected text.

![googleIt screenshot](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/googleIt.png)


Installation
------------

Copy **[googleIt.py](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/googleIt.py)** into your ST2 User packages folder *(Sublime Text 2 > Preferences > Browse Packages... > User)*


Usage
-----

Select text or click desired word, then activate. 

I've added this to my User Key Bindings (Control-Alt-/ on a Mac):

    { "keys": ["ctrl+alt+forward_slash"], "command": "google_it" }

...and this in User/Default\_(your OS)\_Context.sublime-menu, which allows context menu access:

    { "command": "googleIt", "caption": "googleIt…" }


pep8check.py
============

pep8check.py is a [PEP 8 style guide](http://www.python.org/dev/peps/pep-0008/) plugin. It uses another Python program called [pep8.py](http://pypi.python.org/pypi/pep8). It looks like this:

![blame screenshot](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/pep8check.png)


Installation
------------

Copy **[pep8check.py](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/pep8check.py)** into your ST2 User packages folder *(Sublime Text 2 > Preferences > Browse Packages... > User)*

Take a look through the code, and add or remove options that fit your needs. In the stock example, I have the following set up:

    --repeat          show all occurrences of the same error
    --verbose         print status messages, or debug with -vv
    --repeat          show all occurrences of the same error
    --ignore=errors   skip errors and warnings (e.g. E4,W)
    --show-source     show source code for each error
    --statistics      count errors and warnings
    --count           print total number of errors and warnings to standard error and set exit code to 1 if total is not null

Play around with the options until you get what you want.

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

...and this in User/Default\_(your OS)\_Context.sublime-menu, which allows context menu access:

    { "command": "pep8_check", "caption": "PEP8 Check…" }


settings_refresh.py
===================

settings_refresh.py is a ridiculously simple plugin. It saves your settings, which in effect, refreshes your changes, if any were made. I use this for tweaking my color scheme and then immediately seeing the changes.


Installation
------------

Copy **[settings_refresh.py](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/settings_refresh.py)** into your ST2 User packages folder *(Sublime Text 2 > Preferences > Browse Packages... > User)*


Usage
-----

After editing / adding / deleting a setting, or Theme, or Color Scheme, activate to refresh the changes. 

I've added this to my User Key Bindings (&#2303;-&#2318;-r on a Mac):

    { "keys": ["super+ctrl+r"], "command": "settings_refresh" }
