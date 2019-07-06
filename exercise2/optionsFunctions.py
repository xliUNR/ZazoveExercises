#!/usr/bin/python3


######################  Error definition for error handling   ###############################
class InputErrors( Exception ):
    """Base error class for other exceptions"""
    pass

class NegativeError( InputErrors ):
    """raised when value is negative when it should be positive"""
    pass
    
class InvalidOptTypeError( InputErrors):
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
            raise NegativeError
    except NegativeError:
        print( varName,':', checkValue )
        print( 'is negative or 0, please try again with a positive number.' )
        print()
        # return 1 for test fail for error counter in inputArgChecker
        return 1
    # return 0 for test pass for error counter in inputArgChecker
    return 0

def inputArgChecker( parsedArgs ):
    errorCount = 0
    # Check option type for C or P
    try:
        if parsedArgs.opt_type != 'C' and parsedArgs.opt_type != 'P':
            raise InvalidOptTypeError
    except InvalidOptTypeError:
        print( 'opt-type:', parsedArgs.opt_type )
        print( 'is not C or P. Input is case sensitive.')
        print( 'Please enter either C or P and try again.' )
        print()
        errorCount+=1
# next section tests for valid type inputs and non negative or 0 values    
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
    return errorCount 

