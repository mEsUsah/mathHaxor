import tkinter as tk
import tkinter.ttk as ttk
import web
import utils


class Tab():
    def __init__(self, tab):
        """This is the multiplication tab for the elementary school problems"""
        self.tab = tab
        self.firstNumber = tk.IntVar(value=1)
        self.secondNumber = tk.IntVar(value=1)
        self.allowNegative = tk.BooleanVar(value=False)
        self.randomOrder = tk.BooleanVar(value=False)
        self.optionOneCheckbuttons = []
        self.multiplicationTables = []

        optionsFrame = ttk.Frame(self.tab)
        optionsFrame.pack(side="top", expand=1, fill="both")

        # Collumn 1
        optionOne = ttk.Frame(optionsFrame)
        optionOne.pack(side="left", fill="both")
        optionOneLabel = ttk.Label(optionOne,text="Tables to use:")
        optionOneLabel.pack(side="top", fill="x", padx=10, pady=6)

        
        for i in range(1, 11):
            multiplicationTable = tk.BooleanVar(value=False)
            self.multiplicationTables.append(multiplicationTable)

            checkButton = ttk.Checkbutton(
                optionOne,
                text=str(i),
                variable=self.multiplicationTables[i-1],
                command=self.checkSelected
            )
            checkButton.pack(side="top", fill="x", padx=10)
            self.optionOneCheckbuttons.append(checkButton)

        # Collumn 2
        optionTwo = ttk.Frame(optionsFrame)
        optionTwo.pack(side="left", fill="both")
        optionTwoLabel = ttk.Label(optionTwo,text="Quick select:")
        optionTwoLabel.pack(side="top", fill="x", padx=10, pady=6)

        setAllTables = ttk.Button(
            optionTwo,
            text="Select all",
            command=self.setAll
        )
        setAllTables.pack(side="top", fill="x", padx=10, pady=6)

        unsetAllCheck = ttk.Button(
            optionTwo,
            text="Unselect all",
            command=self.unsetAll
        )
        unsetAllCheck.pack(side="top", fill="x", padx=10, pady=6)

        # Collumn 3
        optionThree = ttk.Frame(optionsFrame)
        optionThree.pack(side="left", fill="both")
        optionThreeLabel = ttk.Label(optionThree,text="Options:")
        optionThreeLabel.pack(side="top", fill="x", padx=10, pady=6)

        randomOrder = ttk.Checkbutton(
            optionThree,
            text="Random number order",
            variable=self.randomOrder
        )
        randomOrder.pack(side="top", fill="x", padx=10, pady=6)
        

        # Bottom
        self.createButton = ttk.Button(
            tab, 
            text="Create PDF", 
            command=self.generatePDF
        )
        self.createButton.pack(side="top", fill="x", padx=10, pady=10)
        self.checkSelected()


    def checkSelected(self):
        for table in self.multiplicationTables:
            if table.get():
                self.createButton['state'] = "normal"
                return
        
        self.createButton['state'] = "disabled"

    def setAll(self):
        for table in self.multiplicationTables:
            table.set(True)
        self.checkSelected()


    def unsetAll(self):
        for table in self.multiplicationTables:
            table.set(False)
        self.checkSelected()

    def getTables(self):
        tables = []
        for i in range(0, len(self.multiplicationTables)):
            if self.multiplicationTables[i].get():
                tables.append(i+1)
        return tables
    

    def generateProblems(self):
        tables = self.getTables()
        problems = []
        for i in range(0, 20):
            problem = utils.math_problems.multiplicationProblemWithTables(
                tables,
                randomOrder=self.randomOrder.get()
            )
            problems.append(problem)
        return problems

    def generatePDF(self):
        filePath = utils.pdf.guiSaveAsPath()
        if not filePath:
            return # User canceled the save dialog
        problems = self.generateProblems()
        
        showSolution = True
        html=web.generator.problemsHtml(problems, showSolution)
        css=web.resources.problemsCssFile()
        utils.pdf.create(html, css, filePath)

