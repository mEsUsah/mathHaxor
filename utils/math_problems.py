# Imports
from utils import general

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


class divisionProblem:
    def __init__(self, cipherA, cipherB, difficulty):
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
            self.a = general.generateNumber(a)
            self.b = general.generateNumber(b)
        

    def getSolution(self):
        if self.difficulty == 0:
            return int(self.a / self.b)
        else:
            return self.a / self.b

    def getProblem(self):
        return f"{self.a} / {self.b}"