# Imports
from utils import general
import random

# Base class for math problems
class mathProblem:
    def __init__(self, a, b):
        self.a = general.generateNumber(a)
        self.b = general.generateNumber(b)
        self.a, self.b = general.randomPosition(self.a, self.b)


# Addition problems
class additionProblem(mathProblem):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def getSolution(self):
        return self.a + self.b

    def getProblem(self):
        return f"{self.a} + {self.b}"


class subtractionProblem():
    def __init__(self, a, b, randomPosition=False, allowNegative=True):
        
        self.a = general.generateNumber(a)
        self.b = general.generateNumber(b)
        
        if not allowNegative and not randomPosition:
            self.b = general.generateNumber(b, maxNumber=self.a + 1)

        if randomPosition:
            self.a, self.b = general.randomPosition(self.a, self.b)

    
    def getSolution(self):
        return self.a - self.b
    

    def getProblem(self):
        return f"{self.a} - {self.b}"
    

class multiplicationProblem(mathProblem):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def getSolution(self):
        return self.a * self.b

    def getProblem(self):
        return f"{self.a} * {self.b}"
    

class multiplicationProblemWithTables(mathProblem):
    def __init__(self, tables:list, randomOrder=False):
        self.tables = tables
        self.randomOrder = randomOrder
        self.a = random.choice(tables)
        self.b = random.randint(1, 10)

        if randomOrder:
            self.a, self.b = general.randomPosition(self.a, self.b)
    
    def getSolution(self):
        return self.a * self.b

    def getProblem(self):
        return f"{self.a} * {self.b}"


class divisionProblem:
    def __init__(self, cipherA, cipherB, difficulty=0):
        self.difficulty = difficulty
        
        if difficulty == 0:
            foundProblem = False
            while not foundProblem:
                a = general.generateNumber(cipherA)
                b = general.generateNumber(cipherB)
                if a % b == 0:
                    self.a = a
                    self.b = b
                    foundProblem = True
        else:
            self.a = general.generateNumber(cipherA)
            self.b = general.generateNumber(cipherB)

    def getSolution(self):
        if self.difficulty == 0:
            return int(self.a / self.b)
        else:
            return self.a / self.b

    def getProblem(self):
        return f"{self.a} / {self.b}"


class divisionProblemmWithTables(mathProblem):
    def __init__(self, tables:list):
        # Divident / Divisor = Quotient
        self.divisor = random.choice(tables)
        self.quotient = random.randint(1, 10)
        self.divident = self.divisor * self.quotient
    
    def getSolution(self):
        return self.quotient

    def getProblem(self):
        return f"{self.divident} / {self.divisor}"
        
