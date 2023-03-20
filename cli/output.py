def welcomeSplash():
    print('#'*80)
    print('#')
    print('#   Welcome to Math Haxor!')
    print('#')
    print('#   This is a simple math problem generator')
    print('#')
    print('#'*80)

def showProblems(problems, showAnswer):
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

def goodbyeSplash():
    print('')
    print('#'*80)
    print('#')
    print('#   Thank you for using Math Haxor!')
    print('#')
    print('#'*80)