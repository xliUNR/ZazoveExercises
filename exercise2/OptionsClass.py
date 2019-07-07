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
        # nodes required for binomial tree = (n^2 + 2)/2
        self.levels = time+1
        self.numNodes = int( ( ( self.levels ** 2 ) + self.levels ) / 2 )
        # initialize lists for tree storage
        self.stockTree = [0] * self.numNodes
        self.optTree = [0] * self.numNodes

    # method for populating stock tree with stock prices
    def stockPriceCalc( self ):
        for level in range( self.levels ):
            for i in range( level+1 ):
                index = ( level ** 2 + level / 2 ) + i
                self.stockTree[ index ] = self.startPrice * self.upSize ** ( level - 2 * i )


class Call( Options ):
    def intrinsicValCalc( stockPrice, strikePrice ):
        return max( (stockPrice - strikePrice),0 )

class Put( Options ):
    def intrinsicValCalc( stockPrice, strikePrice ):
        return max( (strikePrice - stockPrice), 0 )


