#!/usr/bin/python3
# This file is a module that contains functions for coupon bond value calculator
import sys
import json
import numpy
import unittest

# function for opening json files
# Input: json file name
# output a json object
def jsonFileOpen( fileName ):
    with open( fileName ) as jsonFile:
        return json.load( jsonFile )

# Returns amount for a single coupon payment
# calculated from a bond face value, the coupon rate, and the frequency coupon is paid
def singleCouponPayment( bondFaceVal, couponRate, couponFreq ):
    return bondFaceVal * ( couponRate / couponFreq )

