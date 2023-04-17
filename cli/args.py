import argparse

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('action',
                        choices=['addition'],
                        help='Select problem type to generate')

    parser.add_argument('n1',
                        type=int,
                        help='Number of ciphers in first number')
    
    parser.add_argument('n2',
                        type=int,
                        help='Number of ciphers in second number')
    
    args = parser.parse_args()

    if args.action == 'addition':
        print('addition was selected')

