import sublime, sublime_plugin, os.path

class OpenFileQuickListCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    window = sublime.active_window()
    views = window.views()
    self.fullPath = []
    self.folders = window.folders()


    self.fileNames = []
    for view in views:
      if view and view.file_name():
        file = view.file_name()
        self.fullPath.append(file)
        self.fileNames.append([self.get_file_name(file), self.replace_root(file)])

    window.show_quick_panel(self.fileNames, self.on_quick_panel_selection, 0, 0)

  def on_quick_panel_selection(self, index):
    if index > -1:
      file = self.fullPath[index]
      print("Opening file '%s'" % (file))
      self.view.window().open_file(file)

  def get_file_name(self, path):
    return os.path.basename(path)

  def replace_root(self, path):
    name = path
    for folder in self.folders:
      name = path.replace(folder, "")

    return name