import os
import sublime
import sublime_plugin


class Pep8CheckCommand(sublime_plugin.TextCommand):

    """This will invoke PEP8 checking on the given file.
    pep8.py must be in your system's path for this to work.

    http://pypi.python.org/pypi/pep8

    Options:
    --version            show program's version number and exit
    --help               show this help message and exit
    --verbose            print status messages, or debug with -vv
    --quiet              report only file names, or nothing with -qq
    --repeat             show all occurrences of the same error
    --exclude=patterns   exclude files or directories which match these comma
                         separated patterns (default: .svn,CVS,.bzr,.hg,.git)
    --filename=patterns  when parsing directories, only check filenames
                       matching these comma separated patterns (default: *.py)
    --select=errors      select errors and warnings (e.g. E,W6)
    --ignore=errors      skip errors and warnings (e.g. E4,W)
    --show-source        show source code for each error
    --show-pep8          show text of PEP 8 for each error
    --statistics         count errors and warnings
    --count              print total number of errors and warnings to standard
                       error and set exit code to 1 if total is not null
    --benchmark          measure processing speed
    --testsuite=dir      run regression tests from dir
    --doctest            run doctest on myself
    """

    def run(self, edit):
        if self.view.file_name().endswith('.py'):
            folder_name, file_name = os.path.split(self.view.file_name())
            self.view.window().run_command('exec', {'cmd': ['pep8',         \
                '--repeat', '--verbose', '--ignore=E501', '--show-source',  \
                '--statistics', '--count',                                  \
                 file_name], 'working_dir': folder_name})
            sublime.status_message("pep8 " + file_name)

    def is_enabled(self):
        return self.view.file_name().endswith('.py')
