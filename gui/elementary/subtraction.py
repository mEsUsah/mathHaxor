import tkinter as tk
import tkinter.ttk as ttk
import web
import utils


class Tab():
    def __init__(self, tab):
        """This is the subtraction tab for the elementary school problems"""
        self.tab = tab
        self.firstNumber = tk.IntVar(value=1)
        self.secondNumber = tk.IntVar(value=1)
        self.allowNegative = tk.BooleanVar(value=False)
        self.optionOneRadios = []
        self.optionTwoRadios = []

        optionsFrame = ttk.Frame(self.tab)
        optionsFrame.pack(side="top", expand=1, fill="both")

        optionOne = ttk.Frame(optionsFrame)
        optionOne.pack(side="left", fill="both")

        optionOneLabel = ttk.Label(optionOne,text="Ciphers in the first factor:")
        optionOneLabel.pack(side="top", fill="x", padx=10, pady=6)

        
        for i in range(1, 5):
            radio = ttk.Radiobutton(
                optionOne,
                text=str(i),
                variable=self.firstNumber,
                value=i,
                command=self.limitCiphers
            )
            radio.pack(side="top", fill="x", padx=10)
            self.optionOneRadios.append(radio)

        optionTwo = ttk.Frame(optionsFrame)
        optionTwo.pack(side="left", fill="both")

        optionTwoLabel = ttk.Label(optionTwo,text="Ciphers in the second factor:")
        optionTwoLabel.pack(side="top", fill="x", padx=10, pady=6)

        for i in range(1, 5):
            radio = ttk.Radiobutton(
                optionTwo,
                text=str(i),
                variable=self.secondNumber,
                value=i
            )
            radio.pack(side="top", fill="x", padx=10)
            self.optionTwoRadios.append(radio)

        optionThree = ttk.Frame(optionsFrame)
        optionThree.pack(side="left", fill="both")

        optionThreeLabel = ttk.Label(optionThree,text="Options:")
        optionThreeLabel.pack(side="top", fill="x", padx=10, pady=6)

        allowNegativeCheck = ttk.Checkbutton(
            optionThree,
            text="Allow negative answers",
            variable=self.allowNegative,
            command=self.limitCiphers
        )
        allowNegativeCheck.pack(side="top", fill="x", padx=10)

        createButton = ttk.Button(
            tab, 
            text="Create PDF", 
            command=self.generatePDF
        )
        createButton.pack(side="top", fill="x", padx=10, pady=10)

        self.limitCiphers()
        

    def limitCiphers(self):
        if not self.allowNegative.get():
            for radio in self.optionTwoRadios:
                if radio['value'] <= self.firstNumber.get():
                    radio['state'] = "active"
                else:
                    radio['state'] = "disabled"  
            
            if self.secondNumber.get() > self.firstNumber.get():
                self.secondNumber.set(self.firstNumber.get())

        else:
            for radio in self.optionTwoRadios:
                radio['state'] = "active"



    def generatePDF(self):
        filePath = utils.pdf.guiSaveAsPath()
        if not filePath:
            return # User canceled the save dialog
        
        problems = []
        for i in range(0, 20):
            problem = utils.math_problems.subtractionProblem(
                self.firstNumber.get(), 
                self.secondNumber.get(),
                allowNegative=self.allowNegative.get()
            )
            problems.append(problem)
        
        showSolution = True
        html=web.generator.problemsHtml(problems, showSolution)
        css=web.resources.problemsCssFile()
        utils.pdf.create(html, css, filePath)

