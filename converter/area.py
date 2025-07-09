"""
  Convert between different units of measurement
  developer: Cristian
  date: 2025-07-09
  version: 1.0.0
  license: MIT License

  description: This module provides functions to convert between area units 
  such as square meters, square kilometers, acres, and hectares.
"""
#convert square meters to square kilometers
def sqm2sqkm(sqm):
    return sqm / 1e6

#convert square kilometers to square meters
def sqkm2sqm(sqkm):
    return sqkm * 1e6

#convert square meters to square feet
def sqm2sqfeet(sqm):
    return sqm * 10.7639

#convert square feet to square meters
def sqfeet2sqm(sqfeet):
    return sqfeet / 10.7639

#convert square meters to square yards
def sqm2sqyards(sqm):
    return sqm * 1.19599

#convert square yards to square meters
def sqyards2sqm(sqyards):
    return sqyards / 1.19599

#convert square meters to acres
def sqm2acres(sqm):
    return sqm / 4046.86

#convert acres to square meters
def acres2sqm(acres):
    return acres * 4046.86

#convert square meters to hectares
def sqm2hectares(sqm):
    return sqm / 10000

#convert hectares to square meters
def hectares2sqm(hectares):
    return hectares * 10000

#convert square kilometers to square feet
def sqkm2sqfeet(sqkm):
    return sqkm * 1.07639e7

#convert square feet to square kilometers
def sqfeet2sqkm(sqfeet):
    return sqfeet / 1.07639e7

#convert square kilometers to square yards
def sqkm2sqyards(sqkm):
    return sqkm * 1.19599e6

#convert square yards to square kilometers
def sqyards2sqkm(sqyards):
    return sqyards / 1.19599e6

#convert square kilometers to acres
def sqkm2acres(sqkm):
    return sqkm * 247.105

#convert acres to square kilometers
def acres2sqkm(acres):
    return acres / 247.105

#convert square kilometers to hectares
def sqkm2hectares(sqkm):
    return sqkm * 100   

#convert hectares to square kilometers
def hectares2sqkm(hectares):
    return hectares / 100

#convert square feet to square yards
def sqfeet2sqyards(sqfeet):
    return sqfeet / 9

#convert square yards to square feet
def sqyards2sqfeet(sqyards):
    return sqyards * 9

#convert square feet to acres
def sqfeet2acres(sqfeet):
    return sqfeet / 43560

#convert acres to square feet
def acres2sqfeet(acres):
    return acres * 43560

#convert square feet to hectares
def sqfeet2hectares(sqfeet):
    return sqfeet / 107639

#convert hectares to square feet
def hectares2sqfeet(hectares):
    return hectares * 107639

