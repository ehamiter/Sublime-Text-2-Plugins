import sublime_plugin
import uuid


class GenerateUuidCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        u = str(uuid.uuid1())
        for r in self.view.sel():
            self.view.replace(edit, r, u)
