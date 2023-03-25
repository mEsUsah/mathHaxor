# import modules
import utils
import web
import gui
import tkinter as tk                    
from tkinter import ttk

window = tk.Tk()
window.title("Math Haxor")
window.geometry("-100+100")
window.resizable(False, False)
gui.icon.setIcon(window)

mainTabControl = ttk.Notebook(window)

elementraySchoolTab = ttk.Frame(mainTabControl)
mainTabControl.add(elementraySchoolTab, text ='Elementary School')

randomTab = ttk.Frame(mainTabControl)
mainTabControl.add(randomTab, text ='Various Problems')

mainTabControl.pack(expand = 1, fill ="both")

gui.elementary.Tab(elementraySchoolTab)


## Various Problems Tab
tab_2_content = ttk.Frame(randomTab)
tab_2_content.pack(expand=1, fill="both")


window.mainloop()