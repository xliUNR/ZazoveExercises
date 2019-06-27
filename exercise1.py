#!/usr/bin/python3
import sys
import json
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

#function to calculate present value of coupon payments
def couponVal( couponPayment, totalPeriods, bondYield ):
    couponSum = 0
    for i in range( 0:totalPeriods ):
        couponSum += couponPayment / ( 1+bondYield ) ^ i
    return couponSum
# function to calculate present value of bond if held to maturity
def bondVal( bondFaceVal, bondYield, maturityTime ):
    return bondFaceVal / ( 1 + bondYield ) ^ maturityTime

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


