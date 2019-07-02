#!/usr/bin/python3
import sys
import json
import numpy
import unittest
import couponbond

# First will implement a test for taking in the JSON file.
# Print out values to check 
def test_jsonFileOpen( fileName ):
    with open( fileName ) as jsonFile:
        data = json.load( jsonFile )
        print( data[ 'parAmount'] )
        print( data[ 'yearsUntilMaturity'] )
        print( data[ 'coupon'] )
        print( data[ 'couponFrequency' ] )
        print( data[ 'couponTiming' ] )
        print( data[ 'yieldCurve' ] )

# function for opening json files
def jsonFileOpen( fileName ):
    with open( fileName ) as jsonFile:
        return json.load( jsonFile )
# function calculates coupon payments based on coupon frequency
def couponPaymentCalc( bondFaceVal, couponRate, couponFreq ):
    return bondFaceVal * ( couponRate / couponFreq )

# function to calculate present value of coupon payments
def couponValCalc( couponPayment, totalPeriods, bondYield, coupTiming ):
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
def bondValCalc( bondFaceVal, bondYield, maturityTime ):
    return bondFaceVal / ( 1 + bondYield ) ^ maturityTime

# function to calculate bond yield, interpolate and extrapolate as necessary
# want this function to use spline for interpolation/extrapolation
def bondYieldCalc( ) 
    # want to check if yearsUntilMaturity is in yield curve, 
    # if not then extrapolate/interpolate by using numpy polyfit

#####################  Main Function  ##########################################
def main():
    #with open( sys.argv[1] ) as jsonFile:
    #data = json.load( jsonFileName )
    #test_jsonFileOpen( sys.argv[1] )
    inputData = jsonFileOpen( sys.argv[1] )
    #print(data)
    # check to see if inputs are valid

    #first calculate coupon payment
    couponPay = singleCouponPayment( inputData['parAmount'], inputData[ 'coupon' ], inputData[ ' couponFrequency' ] )
    # calculate total number of periods
    totalPeriods = inputData[ 'yearsUntilMaturity' ] * inputData[ 'couponFrequency' ]
    # convert yield curve to two arrays for yield interpolation/extrapolation
    tenorArr, yieldArr = dictToArr( inputData[ 'yieldCurve' ] )
    # calculate bond yield from yield curve
    bYield = bondYieldCalc(tenorArr, yieldArr, inputData[ 'yearsUntilMaturity' ] )
    # calculate discounted coupon value
    discountCouponTot = couponVal( couponPay, totalPeriods, bYield, inputData[ ' couponFrequency' ] )
    # calculate discounted bond value
    discountBondVal = bondValCalc( inputData[ 'parAmount' ], bYield, inputData[ 'yearsUntilMaturity' ] )
    #add output of couponVal && bondVal to get present val
    presentVal = discountCouponTot + discountBondVal
    print( presentVal )

if __name__ == '__main__':
    main()


# read json file in

# set values


