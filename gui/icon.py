import os
import tkinter as tk
def setIcon(window):
    dirName=os.path.dirname(__file__)
    absolutPath=os.path.join(dirName,'favicon.png')
    photo = tk.PhotoImage(file = absolutPath)
    window.wm_iconphoto(False, photo)