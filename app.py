#! /usr/bin/env python

# import modules
import cli
import utils

cli.output.welcomeSplash()

# Ask for user input
nProblems = int(input('\nHow many problems would you like to generate? '))
firstNumberSiphers = int(input('How many ciphers should the first number have? '))
secondNumberSiphers = int(input('How many ciphers should the second number have? '))
showAnswer = input('Do you want to see the answer? (Y/n) ')

if showAnswer == 'y' or showAnswer == 'Y' or showAnswer == '':
    showAnswer = True
else:
    showAnswer = False

# Generate problems
print('')
print('#'*80)
print('#')
print('#  Problem set with addition:')
print('#')
print('#'*80)
print('#')

for i in range(0, nProblems):
    firstNumber = utils.general.generateNumber(firstNumberSiphers)
    secondNumber = utils.general.generateNumber(secondNumberSiphers)
    
    firstNumber, secondNumber = utils.general.randomPosition(firstNumber, secondNumber)
    problem = utils.math_problems.additionProblem(firstNumber, secondNumber)
    
    print ('#  ', problem.getProblem(), end='')
    if showAnswer:
        print(' = ', problem.getSolution(), end="\n")
    else:
        print()

print('#')
print('#'*80)