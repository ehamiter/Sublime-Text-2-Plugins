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

I've added this to my User Key Bindings (&#8984;-&#8997;-b on a Mac):

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

I've added this to my User Key Bindings (&#8963;-&#8997;-/ on a Mac):

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

I've added this to my User Key Bindings (&#8984;-&#8679;-8 on a Mac):
    
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

I've added this to my User Key Bindings (&#8963;-&#8984;-r on a Mac):

    { "keys": ["super+ctrl+r"], "command": "settings_refresh" }


generate_uuid.py
================

generate_uuid.py will generate a UUID (uuid4, to be specific-- if you want to know more, or if you should edit this to use uuid1, [read more here](http://stackoverflow.com/questions/1785503/when-should-i-use-uuid-uuid1-vs-uuid-uuid4-in-python)) or a series of UUIDs if you have selected multiple points.


Installation
------------

Copy **[generate_uuid.py](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/generate_uuid.py)** into your ST2 User packages folder *(Sublime Text 2 > Preferences > Browse Packages... > User)*


Usage
-----

Activate to generate a UUID. 

I've added this to my User Key Bindings (&#8984;-&#8679;-u on a Mac):

    { "keys": ["super+shift+u"], "command": "generate_uuid" }


local_validate.py
=================

Using the Mac OS X application *Validator S.A.C.* (separate installation required, see below), local_validate.py will locally validate the current XHTML / HTML file.

![local_validate screenshot](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/master/local_validate.png)


Installation
------------

1. Download [Validator S.A.C.](http://habilis.net/validator-sac/) and copy to your Applications folder.
2. Copy **[local_validate.py](https://github.com/ehamiter/Sublime-Text-2-Plugins/raw/masterlocal_validate.py)** into your ST2 User packages folder *(Sublime Text 2 > Preferences > Browse Packages... > User)*

After installation, your browser may prompt you to select the default handler for `x-validator-sac`. Select *Validator S.A.C.*


Usage
-----

Activate to locally validate the current XHTML / HTML file. 

I've added this to my User Key Bindings (&#8963;-&#8997;-v on a Mac):

    { "keys": ["ctrl+alt+v"], "command": "local_validate" }
