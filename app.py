#! /usr/bin/env python

# import modules
import random

# Welcome screen
print('#'*80)
print('#')
print('#   Welcome to Math Haxor!')
print('#')
print('#   This is a simple math problem generator')
print('#')
print('#'*80)

# Ask for user input
nProblems = int(input('\nHow many problems would you like to generate? '))
firstNumberSiphers = int(input('How many ciphers should the first number have? '))
secondNumberSiphers = int(input('How many ciphers should the second number have? '))
showAnswer = input('Do you want to see the answer? (Y/n) ')

if showAnswer == 'y' or showAnswer == 'Y' or showAnswer == '':
    showAnswer = True
else:
    showAnswer = False


def generateNumber(siphers):
    return random.randint(10**(siphers-1), (10**(siphers))-1)

def printAddition(firstNumber, secondNumber, showAnswer):
    if(showAnswer):
        print('# ',firstNumber, '+', secondNumber, '\t=', firstNumber + secondNumber)
    else:
        print('# ',firstNumber, '+', secondNumber)

def randomPosition(a, b):
    if random.randint(0, 1) == 0:
        return a, b
    else:
        return b, a

# Generate problems
print('')
print('#'*80)
print('#')
print('#  Problem set with addition:')
print('#')
print('#'*80)
print('#')

for i in range(0, nProblems):
    firstNumber = generateNumber(firstNumberSiphers)
    secondNumber = generateNumber(secondNumberSiphers)
    
    firstNumber, secondNumber = randomPosition(firstNumber, secondNumber)
    printAddition(firstNumber, secondNumber, showAnswer)

print('#')
print('#'*80)