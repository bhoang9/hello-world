from pywinauto.application import Application
from pywinauto import mouse as py_mouse
from pywinauto import keyboard as py_keyboard

from pywinauto.application import Application

#app = Application(backend="uia").start('C:\\Program Files\\Sublime Text 3\\sublime_text.exe')

app = Application(backend="uia").connect(path='C:\\Program Files\\Sublime Text 3\\sublime_text.exe')

sublime_window = app.window(class_name="PX_WINDOW_CLASS")
sublime_window.wait('visible')

#returns an array of objects w/ control_type "MenuBar"
app_menu = sublime_window.descendants(control_type="MenuBar")[1]

print(app_menu.items()[8])

#focus on the 9th item in the list of MenuItems
app_menu.items()[8].set_focus()

#select that item
app_menu.items()[8].select()

#When selecting a menu item, that item becomes the top window; look for descendents of the window w/ control type "MenuItem"
#Even if this "menuitem" technically contains an array of more menu items, it is still treated as a menuitem rather than a menubar
preferences_menu = app.top_window().descendants(control_type="MenuItem")[7]

preferences_menu.select()
print(app.top_window().descendants())

app.top_window.descendants().
#print(app.top_window().desecendants(control_types="MenuItem"))

'''for mi in app_menu.items():
    mi.set_focus()
    mi.select()
    print(app.top_window().descendants(control_type="MenuItem"))
    print("=============================================")'''

#adobe_window.menu_select("View->Show/Hide->Tools Pane")
#adobe_window.menu_select("")

#adobe_window.menu_select("View->Display Theme->Dark Gray")

#adobe_window.menu_select("Open")

print("\n EOF ====================")
