#! /usr/bin/env python

# import modules
from cli import *

output.welcomeSplash()

# Ask for user input
nProblems = int(input('\nHow many problems would you like to generate? '))
firstNumberSiphers = int(input('How many ciphers should the first number have? '))
secondNumberSiphers = int(input('How many ciphers should the second number have? '))
showAnswer = input('Do you want to see the answer? (Y/n) ')

if showAnswer == 'y' or showAnswer == 'Y' or showAnswer == '':
    showAnswer = True
else:
    showAnswer = False

def printAddition(firstNumber, secondNumber, showAnswer):
    if(showAnswer):
        print('# ',firstNumber, '+', secondNumber, '\t=', firstNumber + secondNumber)
    else:
        print('# ',firstNumber, '+', secondNumber)

# Generate problems
print('')
print('#'*80)
print('#')
print('#  Problem set with addition:')
print('#')
print('#'*80)
print('#')

for i in range(0, nProblems):
    firstNumber = utils.generateNumber(firstNumberSiphers)
    secondNumber = utils.generateNumber(secondNumberSiphers)
    
    firstNumber, secondNumber = utils.randomPosition(firstNumber, secondNumber)
    printAddition(firstNumber, secondNumber, showAnswer)

print('#')
print('#'*80)