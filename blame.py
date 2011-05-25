import os
import sublime
import sublime_plugin

class BlameCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:  
            folder_name, file_name = os.path.split(self.view.file_name())
            begin_line, begin_column = self.view.rowcol(self.view.sel()[0].begin())
            end_line, end_column = self.view.rowcol(self.view.sel()[0].end())
            begin_line = str(begin_line)
            end_line = str(end_line)
            lines = begin_line + ',' + end_line
            self.view.window().run_command('exec', {'cmd': ['git', 'blame', '-L', lines, file_name], 'working_dir': folder_name})         
            sublime.status_message("git blame -L " + lines + " " + file_name)

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0
