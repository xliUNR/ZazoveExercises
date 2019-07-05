#!/usr/bin/python3
# This file is a module that contains functions for coupon bond value calculator
import json
from scipy.interpolate import interp1d
import unittest

######################  Error definition for error handling   ###############################
class inputErrors(Exception):
    """Base error class for other exceptions"""
    pass

class negativeError( inputErrors ):
    """Raised when value is negative when it should be positive"""
    pass

class invalidTypeError( inputErrors ):
    """Raised when input is not of the correct type (i.e. str when it requires int)"""
    pass

class invalidStrError( inputErrors ):
    """Raised when input string does not match possible strings"""
    pass

######################  Function declarations  ####################################
# function for opening json files
# Takes input file name and outputs a json object
def jsonFileOpen( fileName ):
    with open( fileName ) as jsonFile:
        return json.load( jsonFile )

# checks json object data for invalid data, raises exceptions for invalid input
# and returns 1 for error
def inputChecker( jsonObj ):
    # initialize return value, 0 for pass, >1 for fail
    returnVal = 0
    # check input for par amount
    try:
        # check if float or int
        if type( jsonObj[ 'parAmount' ] ) != float and type( jsonObj[ 'parAmount' ] ) != int:
            raise invalidTypeError
        elif jsonObj[ 'parAmount' ] <= 0:
            raise negativeError
    except invalidTypeError:
        print( 'parAmount:', jsonObj[ 'parAmount' ] )
        print( 'is not of type float or int. Please try again.' )
        print()
        returnVal+=1
    except negativeError:
        print( 'parAmount:', jsonObj[ 'parAmount' ] )
        print( 'is a negative number or 0. Please try again with a positive value.' )
        print()
        returnVal+=1

    # error catching for years until maturity
    try:
        if type( jsonObj[ 'yearsUntilMaturity' ] ) != int:
            raise invalidTypeError
        elif jsonObj[ 'yearsUntilMaturity' ] < 0:
            raise negativeError
    except invalidTypeError:
        print( 'yearsUntilMaturity:', jsonObj[ 'yearsUntilMaturity' ] ) 
        print( 'is not of type int. Please try again.' )
        print()
        returnVal+=1
    except negativeError:
        print( 'yearsUntilMaturity:', jsonObj[ 'yearsUntilMaturity' ] ) 
        print( 'is a negative number. Please try again with a positive value.' )
        print()
        returnVal+=1

    # error catching for coupon rate
    try:
        if type( jsonObj[ 'coupon' ] ) != float and type( jsonObj[ 'coupon' ] ) != int:
            raise invalidTypeError
        elif jsonObj[ 'coupon' ] < 0:
            raise negativeError
    except invalidTypeError:
        print( 'coupon:', jsonObj[ 'coupon' ] )
        print( 'is not of type float or int. Please try again.' )
        print()
        returnVal+=1
    except negativeError:
        print( 'coupon:', jsonObj[ 'coupon' ] )
        print( 'is a negative number. Please try again with a positive value.' )
        print()
        returnVal+=1

    # error catching for coupon frequency
    try:
        if ( type( jsonObj[ 'couponFrequency' ] ) != int ):
            raise invalidTypeError
        elif jsonObj[ 'couponFrequency' ] <= 0:
            raise negativeError
    except invalidTypeError:
        print( 'couponFrequency:', jsonObj[ 'couponFrequency' ] )
        print( 'is not of type float or int. Please try again' )
        print()
        returnVal+=1
    except negativeError:
        print( 'couponFrequency:', jsonObj[ 'couponFrequency' ] )
        print( 'is a negative number or 0. Please try again with frequency > 0.' )
        print( 'To run program with NO coupon payments, please set couponFrequency to 1, and couponRate = 0.' )
        print()
        returnVal+=1

    # error catching for couponTiming
    try:
        if type( jsonObj[ 'couponTiming' ] ) != str:
            raise invalidTypeError
        elif jsonObj[ 'couponTiming' ] != 'end' and jsonObj[ 'couponTiming' ] != 'start':
            raise invalidStrError
    except invalidTypeError:
        print( 'couponTiming:', jsonObj[ 'couponTiming' ] )
        print( 'is not a string. PLease try again.' )
        print()
        returnVal+=1
    except invalidStrError:
        print( 'couponTiming:', jsonObj[ 'couponTiming' ] ) 
        print( 'does not match "end" or "start." Please try again with either of those two strings' )
        returnVal+=1

    # error catching for yieldCurve
    try:
        if type( jsonObj[ 'yieldCurve' ] ) != dict:
            raise invalidTypeError
        else:
            yearsArr, rateArr = dictToArr( jsonObj[ 'yieldCurve' ] )
            # Check if dictToArr ran into errors
            if yearsArr == 1 and rateArr == 1:
                raise invalidTypeError
            # Check for negative values
            else:    
                for year in yearsArr:
                    if year < 0:
                        raise negativeError
                        break
                for rate in rateArr:
                    if rate < 0:
                        raise negativeError
                        break
    except invalidTypeError:
        print( 'yieldCurve:', jsonObj[ 'yieldCurve' ] ) 
        print( 'is not in correct format. Please try again.' )
        print()
        returnVal+=1
    except negativeError:
        print( 'yieldCurve:', jsonObj[ 'yieldCurve' ] )
        print( 'has a value that is negative. Please make sure all values are positive and try again.' )
        print()
        returnVal+=1
    #return 0 for success    
    return returnVal
    
# Returns amount for a single coupon payment
# calculated from a bond face value, the coupon rate, and the frequency coupon is paid
def singleCouponPayment( bondFaceVal, couponRate, couponFreq ):
    # Check for 0 couponFreq
    if couponFreq == 0:
        return 0
    else:
        return bondFaceVal *  couponRate / couponFreq 

# Returns total value of coupon payments discounted with DCF model.
# Takes in coupon payment amount calculated from singleCouponPayment, total periods,
# bond yield percentage, and coupon payment timing.
def couponVal( couponPayment, totalPeriods, bondYield, couponFreq, coupTiming ):
    start = 0
    # if coupon Timing is at end, then first payment starts at period 1 and must be discounted.
    if( coupTiming == 'end'):
        start = 1
        totalPeriods+=1
    # initialize coupon amount
    couponSum = 0
    # sum over total periods of bond
    for i in range( start,totalPeriods ):
        couponSum += couponPayment / ( 1 + ( bondYield / couponFreq ) ) ** i
    return couponSum

# function to calculate present value of bond if held to maturity
# Inputs are the face value of the bond, yield, and maturity time.
def bondValCalc( bondFaceVal, bondYield, couponFreq, totalPeriods):
    return bondFaceVal / ( 1 + ( bondYield / couponFreq ) ) ** totalPeriods

# function to convert a dictionary into two arrays, used in bondYieldCalc
# outputs two arrays, one for the keys and one for the values
def dictToArr( inputDict ):
    # converts each key value pair to integer, float and sorts by key ( years until maturity )
    try:
        keyValList = sorted( [ [ int(k), float(v) ] for k,v in inputDict.items() ] )
    except ValueError:
        print( "One of the dictionary items is not a number" )
        # If one of the dictionary items is not a number, return 1,1
        return 1,1 
    keyArr = [ keyValList[ index ][ 0 ] for index in range( 0, len( keyValList ) ) ]
    valArr = [ keyValList[ index ][ 1 ] for index in range( 0, len( keyValList ) ) ]
    return keyArr, valArr

# function to calculate bond yield, interpolate and extrapolate as necessary
# models yield curve using linear spline.
def bondYieldCalc( YUMArr, yieldRateArr, YUM ): 
    # perform linear spline
    f = interp1d( YUMArr, yieldRateArr, fill_value='extrapolate' )
    return float(f( YUM ))
# calculates final values
def dcfAll( jsonObj ):
    
    return value