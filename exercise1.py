!#/usr/bin/python3
import sys
import json
import unittest

# First will implement a test for taking in the JSON file.
def test_jsonFileOpen( fileName ):
    with open( fileName ) as jsonFile:
        data = json.load( jsonFile )
        #print(  )

with open( sys.argv[1] ) as jsonFile:
    data = json.load( jsonFileName )

# read json file in

# set values


