#!/usr/bin/python3
import unittest
import optionsFunctions as opt
from OptionsClass import Options, Call, Put

class InputTest( unittest.TestCase ):

    # tests for float checker
    def test_floatTypeCheckCorrect(self):
        self.assertEqual( opt.floatTypeCheck( 1.25, 'num' ), True )
    
    def test_floatTypeCheckIncorrect(self):
        self.assertEqual( opt.floatTypeCheck( 'hello', 'num' ), False )


    #test for integer checker
    def test_intTypeCheckCorrect(self):
        self.assertEqual( opt.intTypeCheck( 1, 'num' ), True )

    def test_intTypeCheckIncorrect(self):
        self.assertEqual( opt.intTypeCheck( 'hello', 'num' ), False )


    # tests for negative values check
    def test_negativeCheckNegVals(self):
        self.assertEqual( opt.negativeCheck( -10, 'num' ), 1 )

    def test_negativeCheckZero(self):
        self.assertEqual( opt.negativeCheck( 0, 'num' ), 1 )

    def test_negativeCheckPosVals(self):
        self.assertEqual( opt.negativeCheck( 10, 'num' ), 0 )

# Tests for the Options Class methods
class OptionsClassTest( unittest.TestCase ):
    # tests constructor
    def test_optionsConstructor(self):
        testOpt = Options( 5, 10, 2, 1.01, 0.01 )
        # test each attribute
        self.assertEqual( testOpt.strikePrice, 5 )
        self.assertEqual( testOpt.startPrice, 10 )
        self.assertEqual( testOpt.time, 2 )
        self.assertEqual( testOpt.upSize, 1.01 )
        self.assertEqual( testOpt.riskFreeRate, 0.01 )
        self.assertEqual( testOpt.levels, 3 )
        self.assertEqual( testOpt.numNodes, 6 )
        self.assertEqual( testOpt.stockTree, [ 0,0,0,0,0,0 ] )
        self.assertEqual( testOpt.optTree, [ 0,0,0,0,0,0 ] )

    def test_stockPriceCalc(self):
        testOpt = Options( 101, 100, 3, 1.03, 0.023 )
        testOpt.stockPriceCalc()
        self.assertEqual( testOpt.stockTree, 
            [100.0, 103.0, 97.0873786407767, 106.08999999999999, 100.0, 94.25959091337543, 
            109.2727, 103.0, 97.0873786407767, 91.51416593531594] )
        

if __name__ == '__main__':
    unittest.main()