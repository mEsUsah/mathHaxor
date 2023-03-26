import tkinter as tk
import tkinter.ttk as ttk
import web
import utils


class Tab():
    def __init__(self, tab):
        self.tab = tab
        self.firstNumber = tk.IntVar(value=1)
        self.secondNumber = tk.IntVar(value=1)

        elmAddProblemContainer = ttk.Frame(self.tab)
        elmAddProblemContainer.pack(side="top", expand=1, fill="both")

        elmAddTabContent1 = ttk.Frame(elmAddProblemContainer)
        elmAddTabContent1.pack(side="left", fill="both")

        elmAddLabel1 = ttk.Label(elmAddTabContent1,text="Ciphers in first factor:")
        elmAddLabel1.pack(side="top", fill="x", padx=10, pady=6)

        for i in range(1, 5):
            ttk.Radiobutton(
                elmAddTabContent1,
                text=str(i),
                variable=self.firstNumber,
                value=i
            ).pack(side="top", fill="x", padx=10)

        elmAddTabContent2 = ttk.Frame(elmAddProblemContainer)
        elmAddTabContent2.pack(side="left", fill="both")

        elmAddLabel2 = ttk.Label(elmAddTabContent2,text="Ciphers in second factor:")
        elmAddLabel2.pack(side="top", fill="x", padx=10, pady=6)

        for i in range(1, 5):
            ttk.Radiobutton(
                elmAddTabContent2,
                text=str(i),
                variable=self.secondNumber,
                value=i
            ).pack(side="top", fill="x", padx=10)

        createButton = ttk.Button(
            tab, 
            text="Create PDF", 
            command=self.generatePDF
        )
        createButton.pack(side="top", fill="x", padx=10, pady=10)


    def generatePDF(self):
        filePath = utils.pdf.guiSaveAsPath()
        if not filePath:
            return # User canceled the save dialog
        
        problems = []
        for i in range(0, 20):
            problem = utils.math_problems.additionProblem(self.firstNumber.get(), self.secondNumber.get())
            problems.append(problem)
        
        showSolution = True
        html=web.generator.problemsHtml(problems, showSolution)
        css=web.resources.problemsCssFile()
        utils.pdf.create(html, css, filePath)

