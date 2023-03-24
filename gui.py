# import modules
import cli
import utils
import web
import tkinter as tk                    
from tkinter import ttk

window = tk.Tk()
window.title("Math Haxor")
window.geometry("-100+100")
window.resizable(False, False)

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
elmAddProblemContainer = ttk.Frame(elmAddTab)
elmAddProblemContainer.pack(side="top", expand=1, fill="both")

elmAddTabContent1 = ttk.Frame(elmAddProblemContainer)
elmAddTabContent1.pack(side="left", fill="both")

elmAddLabel1 = ttk.Label(elmAddTabContent1,text="Ciphers in the first number:")
elmAddLabel1.pack(side="top", fill="x", padx=10, pady=6)

elmAddValue1 = tk.IntVar()
for i in range(1, 5):
    ttk.Radiobutton(
        elmAddTabContent1,
        text=str(i),
        variable=elmAddValue1,
        value=i
    ).pack(side="top", fill="x", padx=10)
elmAddValue1.set(1)

elmAddTabContent2 = ttk.Frame(elmAddProblemContainer)
elmAddTabContent2.pack(side="left", fill="both")

elmAddLabel2 = ttk.Label(elmAddTabContent2,text="Ciphers in the second number:")
elmAddLabel2.pack(side="top", fill="x", padx=10, pady=6)

elmAddValue2 = tk.IntVar()
for i in range(1, 5):
    ttk.Radiobutton(
        elmAddTabContent2,
        text=str(i),
        variable=elmAddValue2,
        value=i
    ).pack(side="top", fill="x", padx=10)
elmAddValue2.set(1)


def generateElmAdditionProblems():
    problems = []
    for i in range(0, 20):
        problem = utils.math_problems.additionProblem(elmAddValue1.get(), elmAddValue2.get())
        problems.append(problem)
    
    showSolution = True
    html=web.generator.problemsHtml(problems, showSolution)
    css=web.resources.problemsCssFile()
    utils.pdf.create(html, css, 'problems.pdf')


elmAddButton = ttk.Button(
    elmAddTab, 
    text="Generate Problems",
    command=generateElmAdditionProblems
)
elmAddButton.pack(side="top", fill="x", padx=10, pady=10)


## Various Problems Tab
tab_2_content = ttk.Frame(randomTab)
tab_2_content.pack(expand=1, fill="both")


window.mainloop()