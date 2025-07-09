"""
  Convert between different units of measurement
  developer: Cristian
  date: 2025-07-09
  version: 1.0.0
  license: MIT License

  description: This module provides functions to convert between volume units such as
    liters, milliliters, cubic meters, and gallons.
"""
# Liters, milliliters and cubic meters
def liters2ml(liters):
    return liters * 1000    

def ml2liters(ml):
    return ml / 1000

def liters2cubicmeters(liters):
    return liters / 1000

def cubicmeters2liters(cubicmeters):
    return cubicmeters * 1000

def ml2cubicmeters(ml):
    return ml / 1000000

def cubicmeters2ml(cubicmeters):
    return cubicmeters * 1000000    

# Gallons, quarts, pints, cups, fluid ounces
def liters2gallons(liters):
    return liters / 3.785411784

def gallons2liters(gallons):
    return gallons * 3.785411784

def gallons2quarts(gallons):
    return gallons * 4

def quarts2gallons(quarts):
    return quarts / 4   

def gallons2pints(gallons): 
    return gallons * 8  

def pints2gallons(pints):
    return pints / 8    

def gallons2cups(gallons):
    return gallons * 16

def cups2gallons(cups):
    return cups / 16

def gallons2fluidounces(gallons):
    return gallons * 128    

def fluidounces2gallons(fluidounces):
    return fluidounces / 128    

def liters2fluidounces(liters):
    return liters * 33.8140226

def fluidounces2liters(fluidounces):
    return fluidounces / 33.8140226

def ml2fluidounces(ml):
    return ml / 29.5735296

def fluidounces2ml(fluidounces):
    return fluidounces * 29.5735296

# Cubic meters and imperial/US units
def cubicmeters2cubicfeet(cubicmeters):
    return cubicmeters * 35.3146667

def cubicfeet2cubicmeters(cubicfeet):
    return cubicfeet / 35.3146667

def cubicmeters2cubicinches(cubicmeters):
    return cubicmeters * 61023.7441 

def cubicinches2cubicmeters(cubicinches):
    return cubicinches / 61023.7441

# Cubic feet conversions
def cubicfeet2cubicinches(cubicfeet):
    return cubicfeet * 1728 

def cubicinches2cubicfeet(cubicinches):
    return cubicinches / 1728

def cubicfeet2gallons(cubicfeet):
    return cubicfeet * 7.48051948

def gallons2cubicfeet(gallons):
    return gallons / 7.48051948 

def cubicfeet2liters(cubicfeet):
    return cubicfeet * 28.3168466   

def liters2cubicfeet(liters):
    return liters / 28.3168466

def cubicfeet2ml(cubicfeet):
    return cubicfeet * 28316.8466

def ml2cubicfeet(ml):
    return ml / 28316.8466

def cubicfeet2fluidounces(cubicfeet):
    return cubicfeet * 957.5064935

def fluidounces2cubicfeet(fluidounces):
    return fluidounces / 957.5064935

def cubicfeet2cups(cubicfeet):
    return cubicfeet * 64

def cups2cubicfeet(cups):
    return cups / 64

def cubicfeet2pints(cubicfeet):
    return cubicfeet * 32

def pints2cubicfeet(pints):
    return pints / 32   

def cubicfeet2quarts(cubicfeet):
    return cubicfeet * 16

def quarts2cubicfeet(quarts):
    return quarts / 16

def cubicfeet2cubicyards(cubicfeet):
    return cubicfeet / 27

def cubicyards2cubicfeet(cubicyards):
    return cubicyards * 27

# Cubic yards conversions
def cubicyards2liters(cubicyards):
    return cubicyards * 764.554857984

def liters2cubicyards(liters):
    return liters / 764.554857984

def cubicyards2ml(cubicyards):
    return cubicyards * 764554.857984

def ml2cubicyards(ml):
    return ml / 764554.857984   

def cubicyards2fluidounces(cubicyards):
    return cubicyards * 25852.3465  

def fluidounces2cubicyards(fluidounces):
    return fluidounces / 25852.3465

def cubicyards2cups(cubicyards):
    return cubicyards * 4226.75284

def cups2cubicyards(cups):
    return cups / 4226.75284

def cubicyards2pints(cubicyards):
    return cubicyards * 2113.37642

def pints2cubicyards(pints):
    return pints / 2113.37642

def cubicyards2quarts(cubicyards):
    return cubicyards * 1056.68821

def quarts2cubicyards(quarts):
    return quarts / 1056.68821  

def cubicyards2gallons(cubicyards): 
    return cubicyards * 201.974026

def gallons2cubicyards(gallons):
    return gallons / 201.974026

def cubicyards2cubicinches(cubicyards):
    return cubicyards * 46656

def cubicinches2cubicyards(cubicinches):
    return cubicinches / 46656

def cubicyards2cubicmeters(cubicyards):
    return cubicyards * 0.764554857984

def cubicmeters2cubicyards(cubicmeters):
    return cubicmeters / 0.764554857984
