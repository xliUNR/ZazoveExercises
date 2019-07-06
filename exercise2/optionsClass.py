#!/usr/bin/python3

# This file contains implementation of class and methods for exercise2

class Options:
    """This is the base class for all options"""
    def __init__(self, strikeP, startP, time, upSize, rfr):
        self.strikePrice = strikeP
        self.startPrice = startP
        self.time = time
        self.upSize = upSize
        self.riskFreeRate = rfr

class Call( Options ):
    def intrinsicValCalc( stockPrice, strikePrice ):
        return max( (stockPrice - strikePrice),0 )

class Put( Options ):
    def intrinsicValCalc( stockPrice, strikePrice ):
        return max( (strikePrice - stockPrice), 0 )


