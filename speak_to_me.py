import os
import sublime_plugin


class SpeakToMeCommand(sublime_plugin.TextCommand):
    '''Select some text, activate, and hear it read back to you.
    If you don't select anything, the file's contents will be read.
    '''

    voice = "alex"  # (OS X 10.6 default voice)

    ## More voice choices below:

    ## Female Voices            ## Male Voices
    # Agnes                     # Alex
    # Kathy                     # Bruce
    # Princess                  # Fred
    # Vicki                     # Junior
    # Victoria                  # Ralph

    ## Lion has many new voices-- if you have it, check them out here:
    ## http://goo.gl/iXCIY

    def run(self, edit):
        if not self.view.file_name():
            return

        full_name = self.view.file_name()
        folder_name, file_name = os.path.split(full_name)

        for region in self.view.sel():
            phrase = self.view.substr(region)
            if not region.empty():
                self.view.window().run_command('exec', {'cmd': ['say', '-v', 
                    self.voice, phrase,], 'working_dir': folder_name})         
            else:
                self.view.window().run_command('exec', {'cmd': ['say', '-v', 
                    self.voice, '-f', file_name,], 'working_dir': folder_name})         

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0
