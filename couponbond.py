#!/usr/bin/python3
# This file is a module that contains functions for coupon bond value calculator
import sys
import json
#import numpy
from scipy.interpolate import interp1d
import unittest

# function for opening json files
# Takes input file name and outputs a json object
def jsonFileOpen( fileName ):
    with open( fileName ) as jsonFile:
        return json.load( jsonFile )

# checks json object data for invalid data
def inputChecker( jsonObj ):
    if jsonObj

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
    keyValList = sorted( [ [ int(k), float(v) ] for k,v in inputDict.items() ] )
    keyArr = [ keyValList[ index ][ 0 ] for index in range( 0, len( keyValList ) ) ]
    valArr = [ keyValList[ index ][ 1 ] for index in range( 0, len( keyValList ) ) ]
    return keyArr, valArr

# function to calculate bond yield, interpolate and extrapolate as necessary
# models yield curve using linear spline.
def bondYieldCalc( YUMArr, yieldRateArr, YUM ): 
    # perform linear spline
    f = interp1d( YUMArr, yieldRateArr, fill_value='extrapolate' )
    return f( YUM )

