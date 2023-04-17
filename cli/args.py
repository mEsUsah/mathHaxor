import argparse
import utils

def init():
    parser = argparse.ArgumentParser(
        epilog="Example: cli.py addition 1 1 -n 20 <-- \
                Will generate 20 addition probles with 1 cipher numbers"
    )

    parser.add_argument('action',
                        choices=['addition'],
                        help='Select problem type to generate')

    parser.add_argument('c1',
                        type=int,
                        help='Number of ciphers in first number')
    
    parser.add_argument('c2',
                        type=int,
                        help='Number of ciphers in second number')
    
    parser.add_argument('-n', '--number',
                        type=int,
                        required=False,
                        default=1,
                        help='Number of problems to genereate')

    parser.add_argument('-s', '--solution',
                        action='store_true',
                        help='Give solution in output')
    

    args = parser.parse_args()
    
    problems = []
    for i in range(args.number):     
        if args.action == 'addition':
            problems.append(utils.math_problems.additionProblem(args.c1, args.c2))

    for problem in problems:
        if args.solution:
            print(f'{problem.getProblem()} = {problem.getSolution()}')
        else:
            print(problem.getProblem())

