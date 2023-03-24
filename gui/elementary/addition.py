import tkinter as tk
import tkinter.ttk as ttk
import web
import utils


def gui(tab):
    elmAddProblemContainer = ttk.Frame(tab)
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
        tab, 
        text="Generate Problems",
        command=generateElmAdditionProblems
    )
    elmAddButton.pack(side="top", fill="x", padx=10, pady=10)

