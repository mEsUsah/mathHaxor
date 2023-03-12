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
nProblems = int(input('How many problems would you like to generate? '))
firstNumberSiphers = int(input('How many siphers should the first number have? '))
secondNumberSiphers = int(input('How many siphers should the second number have? '))
showAnswer = input('Do you want to see the answer? (Y/n) ')
if showAnswer == 'y' or showAnswer == 'Y' or showAnswer == '':
    showAnswer = True
else:
    showAnswer = False

# Generate problems

print('')
print('#'*80)
print('#')
print('# Problem set:')
print('#')

for i in range(0, nProblems):
    firstNubmer = random.randint(10**(firstNumberSiphers-1), (10**(firstNumberSiphers))-1)
    secondNumber = random.randint(10**(firstNumberSiphers-1), (10**(secondNumberSiphers))-1)
    if(showAnswer):
        print('# ',firstNubmer, '+', secondNumber, '=', firstNubmer + secondNumber)
    else:
        print('# ',firstNubmer, '+', secondNumber)

print('#')
print('#'*80)