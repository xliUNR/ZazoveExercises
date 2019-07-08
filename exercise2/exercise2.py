#!/usr/bin/python3
import sys
import argparse
from OptionsClass import Options,Call,Put
import optionsFunctions as opt

def main():
    # parse arguments
    parser = argparse.ArgumentParser('European Options Pricing.')
    parser.add_argument('--opt-type', help='Option type: C or P', required=True)
    parser.add_argument('-k', help='Strike price (floating point)', required=True)
    parser.add_argument('-s', help='Starting stock price (floating point)', required=True)
    parser.add_argument('-t', help='Number of days remaining until expiration (integer)', required=True)
    parser.add_argument('-u', help='Size of upward movement (floating point)', required=True)
    parser.add_argument('-r', help='Risk-free rate of interest as a decimal (floating point)', required=True)
    args = parser.parse_args()

    # check inputs
    errorCount = opt.inputArgChecker( args )
    # If input errors occured, exit program
    if errorCount > 0:
        return 1

    #instantiate P or C class
    if args.opt_type == 'C':
        optWork = Call( args.k, args.s, args.t, args.u, args.r )
    elif args.opt_type == 'P':
        optWork = Put( args.k, args.s, args.t, args.u, args.r )

    #fill out stock price tree
    optWork.stockPriceCalc()
    # fill out option price tree
    optWork.optionPriceCalc()
    #return root node value
    print('%.4f'%optWork.optTree[0])

 
if __name__ == '__main__':
    main()
