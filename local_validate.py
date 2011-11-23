import sublime_plugin

class LocalValidateCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        full_link = "x-validator-sac://open?uri=%s" % self.view.file_name()
        self.view.window().run_command('open_url', {"url": full_link})
