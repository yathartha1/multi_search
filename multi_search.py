import webbrowser
import sublime
import sublime_plugin

settings = sublime.load_settings("multi_search.sublime-settings")
search_areas = settings.get('domains')
urls = settings.get('domain_urls')
def Search(index, query_string):
    if index != -1:
        url = urls[index] + "/search?q=" + query_string
        webbrowser.open(url)
    else:
        pass

class MultiSearchCommand(sublime_plugin.TextCommand):
    query_string = ''
    def run(self, edit):
        global search_areas
        for region in self.view.sel():
            if not region.empty():
                self.query_string = self.view.substr(region)
            elif region.empty():
                self.query_string = self.view.substr(self.view.word(region))

        if self.query_string != '':
            self.view.show_popup_menu(search_areas, self.on_done)
        else:
            sublime.status_message("No Selection to Search")
            print("StackSearch Plugin: No Selection to Search")
    def on_done(self, index):
        Search(index, self.query_string)
