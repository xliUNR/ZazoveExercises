#!/usr/bin/python3
import unittest
import optionsFunctions as opt

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


if __name__ == '__main__':
    unittest.main()