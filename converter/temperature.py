"""
  Convert between different units of measurement
  developer: Cristian
  date: 2025-07-09
  version: 1.0.0
  license: MIT License

  description: This module provides functions to convert between temperature units such as
    Celsius, Fahrenheit, and Kelvin.
"""
#convert farenheit to celsius
def fahrenheit2celsius(farenheit):
    return (farenheit - 32) * 5 / 9

#convert celsius to farenheit
def celsius2fahrenheit(celsius):
    return (celsius * 9 / 5) + 32   

#convert celsius to kelvin
def celsius2kelvin(celsius):
    return celsius + 273.15

#convert kelvin to celsius
def kelvin2celsius(kelvin):
    return kelvin - 273.15  
