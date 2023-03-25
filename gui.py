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
randomTab = ttk.Frame(mainTabControl)
mainTabControl.add(elementraySchoolTab, text ='Elementary School')
mainTabControl.add(randomTab, text ='Various Problems')
mainTabControl.pack(expand = 1, fill ="both")


## Elementary School Tab
elementaryTabContent = ttk.Frame(elementraySchoolTab)
elementaryTabContent.pack(side="top", expand=1, fill="both")

tab1_label = ttk.Label(
    elementaryTabContent, 
    text="Problems in this category is designed for kids in the norwegian shool system. from 1st. to 4th. grade:"
)
tab1_label.pack(side="top", fill="x", padx=10, pady=10)

elmTabControl = ttk.Notebook(elementaryTabContent)
elmTabControl.pack(expand = 1, fill ="both")
elmAddTab = ttk.Frame(elmTabControl)
elmTabControl.add(elmAddTab, text ='Addition')
elmSubTab = ttk.Frame(elmTabControl)
elmTabControl.add(elmSubTab, text ='Subtraction')
elmMultiTab = ttk.Frame(elmTabControl)
elmTabControl.add(elmMultiTab, text ='Multiplication')
elmDivTab = ttk.Frame(elmTabControl)
elmTabControl.add(elmDivTab, text ='Division')

# Elementary Addition Tab
gui.elementary.addition.Gui(elmAddTab)


## Various Problems Tab
tab_2_content = ttk.Frame(randomTab)
tab_2_content.pack(expand=1, fill="both")


window.mainloop()