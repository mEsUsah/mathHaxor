#! /usr/bin/env python

# import modules
import cli
import utils

cli.output.welcomeSplash()

# Ask for user input
nProblems = int(input('\nHow many problems would you like to generate? '))
firstNumberSiphers = int(input('How many ciphers should the first number have? '))
secondNumberSiphers = int(input('How many ciphers should the second number have? '))

problemTypes = ['Addition']
problemSelected = False

print('What kind of problem do you want to generate?')
for i in range(0, len(problemTypes)):
    print('  ', i+1, ': ', problemTypes[i], sep='')

ask = True
while ask:
    problemType = int(input("Select a number: "))
    if problemType > 0 and problemType <= len(problemTypes):
        problemSelected = problemType - 1
        ask = False
    
showAnswer = input('Do you want to see the answer? (Y/n) ')

if showAnswer == 'y' or showAnswer == 'Y' or showAnswer == '':
    showAnswer = True
else:
    showAnswer = False

# Generate problems
problems = []
for i in range(0, nProblems):
    firstNumber = utils.general.generateNumber(firstNumberSiphers)
    secondNumber = utils.general.generateNumber(secondNumberSiphers)
    firstNumber, secondNumber = utils.general.randomPosition(firstNumber, secondNumber)
    
    match problemSelected:
        case 0:
            problem = utils.math_problems.additionProblem(firstNumber, secondNumber)
        case _: # Default
            problem = utils.math_problems.additionProblem(firstNumber, secondNumber)

    problems.append(problem)    

# Print problems
print('')
print('#'*80)
print('#')
print('#  Problem set with addition:')
print('#')
print('#'*80)
print('#')

for problem in problems:
    print ('#  ', problem.getProblem(), end='')
    if showAnswer:
        print(' = ', problem.getSolution(), end="\n")
    else:
        print()

print('#')
print('#'*80)