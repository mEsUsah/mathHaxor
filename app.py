#! /usr/bin/env python

# import modules
import cli
import utils

cli.output.welcomeSplash()

# Ask for user input
nProblems = int(input('\nHow many problems would you like to generate? '))
firstNumberSiphers = int(input('How many ciphers should the first number have? '))
secondNumberSiphers = int(input('How many ciphers should the second number have? '))

problemTypes = ['Addition', 'Subtraction','Multiplication', 'Division']
problemSelected = False
problemLvls = ['Elementary', 'Middle']
problemLvlSelected = False

problemSelected = cli.input.list(problemTypes, 'What kind of problem do you want to generate?')
print()
if problemSelected == 3:
    problemLvlSelected = cli.input.list(problemLvls, 'What difficulty?')
    print()
            
showAnswer = input('Do you want to see the answer? (Y/n) ')

if showAnswer == 'y' or showAnswer == 'Y' or showAnswer == '':
    showAnswer = True
else:
    showAnswer = False

# Generate problems
problems = []
for i in range(0, nProblems):
    match problemSelected:
        case 0:
            problem = utils.math_problems.additionProblem(firstNumberSiphers, secondNumberSiphers)
        case 1:
            problem = utils.math_problems.subtractionProblem(firstNumberSiphers, secondNumberSiphers)
        case 2:
            problem = utils.math_problems.multiplicationProblem(firstNumberSiphers, secondNumberSiphers)
        case 3:
            problem = utils.math_problems.divisionProblem(firstNumberSiphers, secondNumberSiphers, problemLvlSelected)
        case _: # Default
            problem = utils.math_problems.additionProblem(firstNumberSiphers, secondNumberSiphers)
    problems.append(problem)    

outputMethod = cli.input.list(['Text','HTML'], 'How do you want to see the problems?')
match outputMethod:
    case 0:
        cli.showProblems(problems, showAnswer)
    case 1:
        print(utils.web_generator.WebGenerator.generateHtml(problems, showAnswer))