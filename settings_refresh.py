import sublime
import sublime_plugin


class SettingsRefreshCommand(sublime_plugin.TextCommand):
    '''This will allow you to refresh your settings. Handy 
    for editing color schemes and seeing the changes quickly.
    '''

    def run(self, edit):
        if not self.view.file_name():
            return

        sublime.save_settings("Base File.sublime-settings")
        sublime.status_message('Settings refreshed.')

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0
