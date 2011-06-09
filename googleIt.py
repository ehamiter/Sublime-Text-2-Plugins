import sublime
import sublime_plugin
import webbrowser


class googleItCommand(sublime_plugin.TextCommand):

    """
    This will search a word or a selection coupled with the file's
    scope. Default binding recommendation: "ctrl + alt + forward_slash"
    """

    def run(self, edit):
        if len(self.view.file_name()) > 0:
            word = self.view.substr(self.view.word(self.view.sel()[0].begin()))
            scope = self.view.scope_name(self.view.sel()[0].begin()).strip()
            getlang = scope.split('.')
            language = getlang[-1]
            sublime.status_message('googleIt invoked-- ' + 'Scope: ' + scope + \
                ' Word: ' + word + ' Language: ' + language)
            for region in self.view.sel():
                phrase = self.view.substr(region)
                search = 'http://google.com/search?q='
                # Feeling lucky? Use 'http://google.com/search?btnI=1&q=' instead
                if not region.empty():
                    webbrowser.open_new_tab(search + phrase + " " + language)
                else:
                    webbrowser.open_new_tab(search + word + " " + language)
        else:
            pass

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0
