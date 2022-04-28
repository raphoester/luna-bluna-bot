from terra_sdk.core import Coin 

def emptyCoin():
    return Coin(denom="", amount=0)

def fromMicroAmount(number):
    return float(number)/1000000

def toMicroAmount(number):
    return int(number*1000000)

def percentageGain(fromValue, toValue):
    return ((toValue - fromValue) / fromValue) * 100

def price(lunaValue, bLunaValue):
    return lunaValue/bLunaValue

def toLuna(bLunaValue: float, price: float):
    return bLunaValue/price

def tobLuna(lunaValue: float, price: float):
    return lunaValue*price