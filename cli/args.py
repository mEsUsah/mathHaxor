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
    
    args = parser.parse_args()

    for i in range(args.number):
        number_1 = utils.general.generateNumber(args.c1)
        number_2 = utils.general.generateNumber(args.c2)
        
        if args.action == 'addition':
            print(number_1, number_2)

