#!/usr/bin/python3
import sys
import argparse
from OptionsClass import Call,Put
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
    print(type(args.opt_type))
    print(type(args.k))
    print(args.s)
    print(args.t)
    print(args.u)
    print(args.r)
    #print(type(args))
    # check inputs
    errorCount = opt.inputArgChecker( args )

    if errorCount > 0:
        return 1
    
    print(errorCount)
    #instantiate P or C class
    if args.opt_type == 'C':
        optWork = Put( args.k, args.s, args.t, args.u, args.r )
    elif args.opt_type == 'P':
        optWork = Call( args.k, args.s, args.t, args.u, args.r )

    #fill out stock price tree
    optWork.stockPriceCalc()
    # fill out option price tree
    optWork.optionPriceCalc()
    #return root node value
    print(optWork.optTree[0])

    #print(optWork.strikePrice)

if __name__ == '__main__':
    main()
