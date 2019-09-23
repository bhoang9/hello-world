from pywinauto.application import Application

app = Application(backend="uia").start('C:\\Program Files\\Sublime Text 3\\sublime_text.exe')

sublime_window = app.window(class_name="PX_WINDOW_CLASS")

sublime_window.wait('visible')

#print("great success")

#sublime_window.print_control_identifiers()

print(sublime_window.descendants(control_type="MenuBar"))

#sublime_window.menu_select("Preferences->Font").menu_select("Larger")

#https://github.com/pywinauto/pywinauto/issues/385