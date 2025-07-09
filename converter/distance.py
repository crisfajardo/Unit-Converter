"""
  Convert between different units of measurement
  developer: Cristian
  date: 2025-07-09
  version: 1.0.0
  license: MIT License

  description: This module provides functions to convert between distance units such as
    kilometers, miles, meters, and feet.
"""
#convert meters to kilometers
def meters2km(meters):
    return meters / 1000

#convert kilometers to meters
def km2meters(kilometers):
    return kilometers * 1000

#convert meters to milimeters 
def meters2mm(meters):
    return meters * 1000

#convert millimeters to meters
def mm2meters(millimeters):
    return millimeters / 1000

#convert kilometers to miles
def km2miles(kilometers):
    return kilometers / 1.609344

#convert miles to kilometers
def miles2km(miles):
    return miles * 1.609344

#convert meters to centimeters
def meters2cm(meters):
    return meters / 100

#convert centimeters to meters
def cm2meters(centimeters):
    return centimeters * 100

#convert centimeters to feet
def cm2feet(centimeters):
    return centimeters / 30.48

#convert feet to centimeters
def feet2cm(feet):
    return feet * 30.48

#convert centimeters to inches
def cm2inches(centimeters):
    return centimeters / 2.54

#convert inches to centimeters
def inches2cm(inches):
    return inches * 2.54

#convert inches to feet 
def inches2feet(inches):
    return inches / 12

#convert feet to inches
def feet2inches(feet):
    return feet * 12
