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


def main():
    #with open( sys.argv[1] ) as jsonFile:
    #data = json.load( jsonFileName )
    #test_jsonFileOpen( sys.argv[1] )
    inputData = jsonFileOpen( sys.argv[1] )
    #print(data)

if __name__ == '__main__':
    main()


# read json file in

# set values


