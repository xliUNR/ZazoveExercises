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

class functionTests( unittest.TestCase ):
	# test singleCouponPayment function
	def test_singleCouponZeroFreq(self):
		self.assertEqual( cb.singleCouponPayment( 100.0, 0.01, 0 ), 0 )

	def test_singleCoupon(self):
		self.assertEqual( cb.singleCouponPayment( 100.0, 0.01, 5 ), 0.2 )
	
	# test coupon value function
	def test_couponValStart(self):
		self.assertEqual( '%.4f'%cb.couponVal( 15.0, 4, 0.01, 'start'), '59.1148' )
	

	def test_couponValEnd(self):
		self.assertEqual( '%.4f'%cb.couponVal( 15.0, 4, 0.01, 'end'), '58.5295' )
	

	def test_couponValZeroPeriodStart(self):
		self.assertEqual( '%.4f'%cb.couponVal(15.0, 0, 0.01, 'start'), '0.0000' )

	def test_couponValZeroPeriodEnd(self):
		self.assertEqual( '%.4f'%cb.couponVal(15.0, 0, 0.01, 'end'), '0.0000' )
	
	# test bondValCalc function

	# test dictToArr function

	# test bondYieldCalc function
	#def test_singleCouponPayment(self):
	#	self.assertEqual()

if __name__ == '__main__':
	unittest.main()
	

