#!/usr/bin/python3

# This file contains implementation of class and methods for exercise2

class options:
    """This is the base class for all options"""
    def __init__(self, strikeP, startP, time, upSize, rfr):
        self.strikePrice = strikeP
        self.startPrice = startP
        self.time = time
        self.upSize = upSize
        self.riskFreeRate = rfr

class call( options ):
    def intrinsicValCalc( stockPrice, strikePrice ):
        return max( (stockPrice - strikePrice),0 )

class put( options ):
    def intrinsicValCalc( stockPrice, strikePrice ):
        return max( (strikePrice - stockPrice), 0 )