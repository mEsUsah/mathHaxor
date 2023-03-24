# import modules
import cli
import utils
import web
import tkinter as tk                    
from tkinter import ttk

window = tk.Tk()
window.title("Tab Widget 2")
window.geometry("600x400-100+100")

tabControl = ttk.Notebook(window)
elementraySchoolTab = ttk.Frame(tabControl)
randomTab = ttk.Frame(tabControl)
tabControl.add(elementraySchoolTab, text ='Elementary School')
tabControl.add(randomTab, text ='Various Problems')
tabControl.pack(expand = 1, fill ="both")


## Elementary School Tab
elementaryTabContent = ttk.Frame(elementraySchoolTab)
elementaryTabContent.pack(side="top", expand=1, fill="both")

tab1_label = ttk.Label(elementaryTabContent, text="Stuff in Tab 1")
tab1_label.pack(side="top", fill="x")
tab1_button = ttk.Button(elementaryTabContent, text="Button in Tab 1")
tab1_button.pack(side="bottom", fill="x")


## Various Problems Tab
tab_2_content = ttk.Frame(randomTab)
tab_2_content.pack(expand=1, fill="both")


window.mainloop()