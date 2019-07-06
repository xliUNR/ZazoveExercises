#!/usr/bin/python3
import sys
import argparse
from options import call,put

######################  Error definition for error handling   ###############################
class inputErrors( Exception ):
    """Base error class for other exceptions"""
    pass

class negativeError( inputErrors ):
    """raised when value is negative when it should be positive"""
    pass

class invalidTypeError( inputErrors ):
    """Raised when input is not of the correct type (i.e. str when it requires int)"""
    pass
    
class invalidOptTypeError( inputErrors):
    """Raised when input option type is not supported"""
    pass

#######################  free function definitions  ##################################    
# helper function for inputArgChecker that checks if input checkValue is a float
# input variable: varName for printing purposes
def floatTypeCheck( checkValue, varName ):
    try:
        float( checkValue )
    except ValueError:
        print( varName,':', checkValue )
        print( 'is not a float. Please enter a float and try again.' )
        print()
        # return False for test fail
        return False
    # return True for pass
    return True

# helper function for inputArgChecker that checks if input checkValue is an integer
# input variable: varName for printing purposes
def intTypeCheck( checkValue, varName ):
    try:
        int( checkValue )
    except ValueError:
        print( varName,':', checkValue )
        print( 'is not an integer. Please enter an integer and try again.' )
        print()
        # return false for test fail
        return False
    # return True for pass
    return True

# helper function for inputArgChecker that checks if input checkValue is negative or 0
# input variable: varName for printing purposes
def negativeCheck( checkValue, varName ):
    try:
        if checkValue <= 0:
            raise negativeError
    except negativeError:
        print( varName,':', checkValue )
        print( 'is negative or 0, please try again with a positive number.' )
        print()
        # return 1 for test fail for error counter in inputArgChecker
        return 1
    # return 0 for test pass for error counter in inputArgChecker
    return 0

def inputArgChecker( parsedArgs ):
    errorCount = 0
    # flags for valid type, used for negative checks if passes valid type check
    valid_k = True
    valid_s = True
    valid_u = True
    valid_r = True
    valid_t = True
    # Check option type for C or P
    try:
        if parsedArgs.opt_type != 'C' and parsedArgs.opt_type != 'P':
            raise invalidOptTypeError
    except invalidOptTypeError:
        print( 'opt-type:', parsedArgs.opt_type )
        print( 'is not C or P. Input is case sensitive. Please enter either C or P and try again.' )
        print()
        errorCount+=1
# next section tests for valid type inputs    
    # Check if strike price is float
    """try:
        float( parsedArgs.k )
    except ValueError:
        print( 'k:', parsedArgs.k )
        print( 'is not a float. Please enter a float and try again.' )
        print()
        errorCount+=1
        valid_k = False
    # Check if stock price is float
    try:
        float( parsedArgs.s )
    except ValueError:
        print( 's:', parsedArgs.s )
        print( 'is not a float. Please enter a float and try again.' )
        print()
        errorCount+=1
        valid_s = False

    # Check if upward movement is float
    try:
        float( parsedArgs.u )
    except ValueError:
        print( 'u:', parsedArgs.u )
        print( 'is not a float. Please enter a float and try again.' )
        print()
        errorCount+=1
        valid_u = False

    # Check if risk free interest rate is float
    try:
        float( parsedArgs.r )
    except ValueError:
        print( 'r:', parsedArgs.r )
        print( 'is not a float. Please enter a float and try again.' )
        print()
        errorCount+=1
        valid_r = False

    try:
        int( parsedArgs.t )
    except ValueError:
        print( 't:', parsedArgs.t )
        print( 'is not an integer. Please enter a n integer and try again.' )
        print()
        errorCount+=1
        valid_t = False
"""
    # test for negative or 0 strike price
    if floatTypeCheck( parsedArgs.k, 'k' ):
        errorCount += negativeCheck( float( parsedArgs.k ), 'k')
    # test for negative stock price
    if floatTypeCheck( parsedArgs.s, 's' ):
        errorCount += negativeCheck( float(parsedArgs.s ), 's' )
    # test for negative time
    if intTypeCheck( parsedArgs.t, 't' ):
        errorCount += negativeCheck( int(parsedArgs.t ), 't' )
    # test for negative upward movement size
    if floatTypeCheck( parsedArgs.u, 'u' ):
        errorCount += negativeCheck( float(parsedArgs.u ), 'u' )
    # test for negative risk-free interest rate
    if floatTypeCheck( parsedArgs.r, 'u' ):
        errorCount += negativeCheck( float(parsedArgs.r ), 'r' )
        
    # test for negative or 0 stock price
    """if valid_s == True:
        try:
            if float( parsedArgs.s ) <= 0:
                raise negativeError
        except negativeError:
            print( 's:', parsedArgs.s )
            print( 'is negative or 0, please try again with a positive number' )
            print()
            errorCount+=1

    if valid_u == True:
        try:
            if float( parsedArgs.u ) <= 0:
                raise negativeError
        except negativeError:
            print( 'u:', parsedArgs.u )
            print( 'is negative or 0, please try again with a positive number' )
            print()
            errorCount+=1"""

    return errorCount 

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
    errorCount = inputArgChecker( args )
    #instantiate P or C class
    if args.opt_type == 'C':
        optWork = put( args.k, args.s, args.t, args.u, args.r )
    elif args.opt_type == 'P':
        optWork = call( args.k, args.s, args.t, args.u, args.r )

if __name__ == '__main__':
    main()
