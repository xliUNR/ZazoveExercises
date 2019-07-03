#!/usr/bin/python3
import couponbond as cb
import unittest

##################  This is the test script.  #########################

class inputTest( unittest.TestCase):
	
	# Tests for negative values
	def test_NegativeValues(self):
		testData = cb.jsonFileOpen('negativeTest.json' )
		# inputChecker should return 5 if all invalid values caught
		self.assertEqual(cb.inputChecker( testData ), 5 )

	# Tests for negative yield year ONLY	
	def test_NegativeYieldYear(self):
		testData = cb.jsonFileOpen( 'negativeYieldYear.json' )
		# inputChecker returns 1 if negative year in yield curve is caught
		self.assertEqual(cb.inputChecker( testData ), 1 )

	# Test for negative yield rate ONLY	
	def test_NegativeYieldRate(self):
		testData = cb.jsonFileOpen( 'negativeYieldRate.json' )
		# inputChecker returns 1 if negative rate in yield curve is caught
		self.assertEqual(cb.inputChecker( testData ), 1 )	

	# Tests non dictionary yieldCurve
	def tests_nonDictYieldCurve(self):
		testData = cb.jsonFileOpen( 'nonDictYieldCurve.json' )
		# inputChecker returns 1 if negative rate in yield curve is caught
		self.assertEqual(cb.inputChecker( testData ), 1 )	

	# Tests for invalid inputs such as str/char when expecting int or float and vice versa
	def test_InvalidValues(self):
		testData = cb.jsonFileOpen( 'invalidTest.json' )
		# inputChecker should return 6 if all invalid values caught
		self.assertEqual( cb.inputChecker( testData ), 6 )

	# Tests if check for strings other than "end" and "start" for couponTiming
	def test_CouponTiming(self):
		testData = cb.jsonFileOpen( 'invalidCouponTiming.json')
		# inputChecker should return 1 if exception is caught
		self.assertEqual( cb.inputChecker( testData ), 1 )

if __name__ == '__main__':
	unittest.main()
	

