"""
  Convert between different units of measurement
  developer: Cristian
  date: 2025-07-09
  version: 1.0.0
  license: MIT License

  description: This module provides functions to convert between weight units such as
    kilograms, grams, pounds, and ounces.
"""
#convert kilograms to grams
def kg2grams(kilograms):
    return kilograms * 1000

#convert grams to kilograms    
def grams2kg(grams):
    return grams / 1000

#convert kilograms to pounds
def kg2pounds(kilograms):   
    return kilograms * 2.2046244

#convert pounds to kilograms
def pounds2kg(pounds):
    return pounds / 2.2046244 
