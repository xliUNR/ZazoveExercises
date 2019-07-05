#!/usr/bin/python3
import sys
import couponbond as cb


#####################  Main Function  ##########################################
def main():
    #with open( sys.argv[1] ) as jsonFile:
    #data = json.load( jsonFileName )
    #test_jsonFileOpen( sys.argv[1] )
    inputData = cb.jsonFileOpen( sys.argv[1] )
    # check valid inputs
    if cb.inputChecker( inputData ) > 0:
        return 1
        
    #first calculate coupon payment
    couponPay = cb.singleCouponPayment( inputData['parAmount'], inputData[ 'coupon' ], inputData[ 'couponFrequency' ] )
    # calculate total number of periods
    totalPeriods = inputData[ 'yearsUntilMaturity' ] * inputData[ 'couponFrequency' ]
    # convert yield curve to two arrays for yield interpolation/extrapolation
    tenorArr, yieldArr = cb.dictToArr( inputData[ 'yieldCurve' ] )
    # calculate bond yield from yield curve, return value in percentage.
    bondYield = cb.bondYieldCalc(tenorArr, yieldArr, inputData[ 'yearsUntilMaturity' ] )
    # convert bondYield to decimal value
    bondYield/=100
    # calculate discounted coupon value
    discountCouponTot = cb.couponVal( couponPay, totalPeriods, bondYield, inputData[ 'couponFrequency' ], inputData[ 'couponTiming' ] )
    # calculate discounted bond value
    discountBondVal = cb.bondValCalc( inputData[ 'parAmount' ], bondYield, inputData[ 'couponFrequency' ], totalPeriods )
    #add output of couponVal && bondVal to get present val
    presentVal = discountCouponTot + discountBondVal
    # print output
    print( float('%.4f'%presentVal ) )

if __name__ == '__main__':
    main()


# read json file in

# set values


