class mathProblem:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class additionProblem(mathProblem):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def getSolution(self):
        return self.a + self.b

    def getProblem(self):
        return f"{self.a} + {self.b}"