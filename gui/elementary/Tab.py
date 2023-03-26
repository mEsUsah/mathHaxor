import tkinter as tk
import tkinter.ttk as ttk
import gui
import web
import utils
import os

class Tab():
    def __init__(self, tab):
        '''This is the tab for the elementary school problems'''
        ## Elementary School Tab
        elementaryTabContent = ttk.Frame(tab)
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
        gui.elementary.addition.Tab(elmAddTab)
        gui.elementary.subtraction.Tab(elmSubTab)
        gui.elementary.multiplication.Tab(elmMultiTab)
        gui.elementary.division.Tab(elmDivTab)