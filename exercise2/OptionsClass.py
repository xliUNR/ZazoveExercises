#!/usr/bin/python3

# This file contains implementation of class and methods for exercise2

class Options:
    """This is the base class for all options"""
    def __init__( self, strikeP, startP, time, upSize, rfr ):
        self.strikePrice = float( strikeP )
        self.startPrice = float( startP )
        self.time = int( time )
        self.upSize = float ( upSize )
        self.riskFreeRate = float ( rfr )
        # nodes required for binomial tree = (n^2 + 2)/2
        self.levels = self.time+1
        self.numNodes = int( ( ( self.levels ** 2 ) + self.levels ) / 2 )
        # initialize lists for tree storage
        self.stockTree = [0] * self.numNodes
        self.optTree = [0] * self.numNodes

    # method for populating stock tree with stock prices
    def stockPriceCalc( self ):
        for level in range( 0,self.levels ):
            for i in range( level+1 ):
                index = int( ( ( level ** 2 + level )/ 2 ) + i )
                self.stockTree[ index ] = self.startPrice * self.upSize ** ( level - 2 * i )


    # method for calculating option prices
    def optionPriceCalc( self ):
        # calculate probabilities of upward and downward movement
        pUp = ( 1 + self.riskFreeRate -  1 / 
            self.upSize ) / ( self.upSize - 1 / self.upSize ) 
        pDown = 1 - pUp
        # calculate riskFreeRate discount
        disRate = 1 / ( 1+self.riskFreeRate )
        # calculate intrinsic value at final nodes
        for i in range( int ( ( ( self.levels - 1 ) ** 2 + self.levels )  / 2 ), self.numNodes ):
            self.optTree[i] = self.intrinsicValCalc( self.stockTree[i] )
        #calculate option price for rest of tree
        for level in range( self.levels - 2, -1, -1 ):
            for i in range( level+1 ):
                index = int( ( ( level ** 2 + level ) / 2 ) + i )
                # calculate option price at node from next node weighted by probability
                oPrice = disRate * ( 
                    pUp * self.optTree[ int( index + level + 1) ] + 
                    pDown * self.optTree[ int( index + level + 2 ) ] )
                self.optTree[ index ] = oPrice

class Call( Options ):
    def intrinsicValCalc( self, stockPrice ):
        return max( (stockPrice - self.strikePrice), 0 )

class Put( Options ):
    def intrinsicValCalc( self, stockPrice ):
        return max( (self.strikePrice - stockPrice), 0 )



