#!/usr/bin/python3
# This file is a module that contains functions for coupon bond value calculator
import sys
import json
#import numpy
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
def inputChecker( jsonObj ):
    # check input for par amount
    try:
        # check if float or int
        if type( jsonObj[ 'parAmount' ] ) != float or type( jsonObj[ 'parAmount' ] ) != int:
            raise invalidTypeError
        elif jsonObj[ ' parAmount' ] < 0:
            raise negativeError
    except invalidTypeError:
        print( 'parAmount:', jsonObj[ 'parAmount' ],
         'is not of type float or int. Please try again.' )
        print()
    except negativeError:
        print( 'parAmount:', jsonObj[ 'parAmount' ], 
            'is a negative number. Please try again with a positive value.' )
        print()
    
    # error catching for years until maturity
    try:
        if type( jsonObj[ 'yearsUntilMaturity' ] ) != int:
            raise invalidTypeError
        elif jsonObj[ 'yearsUntilMaturity' ] < 0:
            raise negativeError
    except invalidTypeError:
        print( 'yearsUntilMaturity:', jsonObj[ 'yearsUntilMaturity' ], 
            'is not of type int. Please try again.')
        print()
    except negativeError:
        print( 'yearsUntilMaturity:', jsonObj[ 'yearsUntilMaturity' ], 
            'is a negative number. Please try again with a positive value.' )
        print()

    # error catching for coupon rate
    try:
        if type( jsonObj[ 'coupon' ] ) != float or type( jsonObj[ 'coupon' ] ) != int:
            raise invalidTypeError
        elif jsonObj[ 'coupon' ] < 0:
            raise negativeError
    except invalidTypeError:
        print( 'coupon:', jsonObj[ 'coupon' ], 'is not of type float or int. Please try again.' )
        print()
    except negativeError:
        print( 'coupon:', jsonObj[ 'coupon' ], 'is a negative number. Please try again with a positive value.' )
        print()

    # error catching for coupon frequency
    try:
        if ( type( jsonObj[ 'couponFrequency' ] ) != float or 
            type( jsonObj[ 'couponFrequency' ] ) != int ):
            raise invalidTypeError
        elif jsonObj[ 'couponFrequency' ] < 0:
            raise negativeError
    except invalidTypeError:
        print( 'couponFrequency', jsonObj[ 'couponFrequency' ], 
            'is not of type float or int. Please try again' )
        print()
    except negativeError:
        print( 'couponFrequency', jsonObj[ 'couponFrequency' ], 
            'is a negative number. Please try again with a positive value.' )
        print()

    # error catching for couponTiming
    try:
        if type( jsonObj[ 'couponTiming' ] ) != str:
            raise invalidTypeError
        elif jsonObj[ 'couponTiming' ] != 'end' or jsonObj[ 'couponTiming' ] != 'start':
            raise invalidStrError
    except invalidTypeError:
        print( 'couponTiming', jsonObj[ 'couponTiming' ], 'is not a string. PLease try again.' )
        print()
    except invalidStrError:
        print( 'couponTiming', jsonObj[ 'couponTiming' ], 
            'does not match "end" or "start." Please try again with either of those two strings' )

    # error catching for yieldCurve
    try:
        if type( jsonObj[ 'yieldCurve' ] ) != dict:
            raise invalidTypeError
        else:
            yearsArr, rateArr = dictToArr( jsonObj[ 'yieldCurve' ] )
            for year in yearsArr:
                if year < 0:
                    raise negativeError
                    break
            for rate in rateArr:
                if rate < 0:
                    raise negativeError
                    break
    except invalidTypeError:
        print( 'yieldCurve', jsonObj[ 'yieldCurve' ], 'is not in correct format. Please try again.' )
        print()
    except negativeError:
        print( 'yieldCurve', jsonObj[ 'yieldCurve' ], 
            'has a value that is negative. Please make sure all values are positive and try again.' )
        print()

# Returns amount for a single coupon payment
# calculated from a bond face value, the coupon rate, and the frequency coupon is paid
def singleCouponPayment( bondFaceVal, couponRate, couponFreq ):
    return bondFaceVal * ( couponRate / couponFreq )

# Returns total value of coupon payments discounted with DCF model.
# Takes in coupon payment amount calculated from singleCouponPayment, total periods,
# bond yield percentage, and coupon payment timing.
def couponVal( couponPayment, totalPeriods, bondYield, coupTiming ):
    start = 0
    # if coupon Timing is at end, then first payment starts at period 1 and must be discounted.
    if( coupTiming == 'end'):
        start = 1
        totalPeriods+=1
    # initialize coupon amount
    couponSum = 0
    # sum over total periods of bond
    for i in range( start:totalPeriods ):
        couponSum += couponPayment / ( 1+bondYield ) ^ i
    return couponSum

# function to calculate present value of bond if held to maturity
# Inputs are the face value of the bond, yield, and maturity time.
def bondValCalc( bondFaceVal, bondYield, maturityTime ):
    return bondFaceVal / ( 1 + bondYield ) ^ maturityTime

# function to convert a dictionary into two arrays, used in bondYieldCalc
# outputs two arrays, one for the keys and one for the values
def dictToArr( inputDict ):
    # converts each key value pair to integer, float and sorts by key ( years until maturity )
    try:
        keyValList = sorted( [ [ int(k), float(v) ] for k,v in inputDict.items() ] )
        keyArr = [ keyValList[ index ][ 0 ] for index in range( 0, len( keyValList ) ) ]
        valArr = [ keyValList[ index ][ 1 ] for index in range( 0, len( keyValList ) ) ]
        return keyArr, valArr
    except ValueError:
        print( "One of the dictionary items is not a number" ) 
    
# function to calculate bond yield, interpolate and extrapolate as necessary
# models yield curve using linear spline.
def bondYieldCalc( YUMArr, yieldRateArr, YUM ): 
    # perform linear spline
    f = interp1d( YUMArr, yieldRateArr, fill_value='extrapolate' )
    return f( YUM )

