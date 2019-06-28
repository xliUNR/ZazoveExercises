#!/usr/bin/python3
import sys
import json
import numpy
import unittest

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
    #first calculate coupon payment
    couponPay = data[ 'parAmount' ] * ( data[ 'coupon' ] / data[ 'couponFrequency' ] )
    #then calculate present value of coupon payments, depends on couponTiming
    # if end, then start range at 1, else start range at 0?
    couponSum = 0
    totalPeriods = data[ 'couponFrequency' ] * data[ ' yearsUntilMaturity ' ]
    if data[ 'couponTiming' ] == 'end':
        for i in range(1:totalPeriods ):
            couponSum += data[ ' parAmount ' ] * 
    elif data[ 'couponTiming' ] == 'start':
        for i in range(0:totalPeriods ):

    #add output of couponVal && bondVal to get present val



if __name__ == '__main__':
    main()


# read json file in

# set values


