"""
  Convert between different units of measurement
  developer: Cristian
  date: 2025-07-09
  version: 1.0.0
  license: MIT License

  description: This module provides functions to convert between pressure units such as
    pascals, bars, psi, and atmospheres.
"""
#convert pascals to bars
def pascals2bars(pascals):
    return pascals / 100000

#convert bars to pascals
def bars2pascals(bars):
    return bars * 100000

#convert atmospheres to bars
def atmospheres2bars(atmospheres):
    return atmospheres * 1.01325

#convert bars to atmospheres
def bars2atmospheres(bars):
    return bars / 1.01325

#convert pascals to atmospheres
def pascals2atmospheres(pascals):  
    return pascals / 101325

#convert atmospheres to pascals
def atmospheres2pascals(atmospheres):
    return atmospheres * 101325

#convert bars to millimeters of mercury
def bars2mmhg(bars):
    return bars * 750.062

#convert millimeters of mercury to bars 
def mmhg2bars(mmhg):
    return mmhg / 750.062

#convert pascals to millimeters of mercury
def pascals2mmhg(pascals):
    return pascals / 133.322

#convert millimeters of mercury to pascals
def mmhg2pascals(mmhg):
    return mmhg * 133.322

#convert atmospheres to millimeters of mercury
def atmospheres2mmhg(atmospheres):
    return atmospheres * 760

#convert millimeters of mercury to atmospheres
def mmhg2atmospheres(mmhg):
    return mmhg / 760   

#convert bars to pounds per square inch
def bars2psi(bars):
    return bars * 14.5037738

#convert pounds per square inch to bars
def psi2bars(psi):
    return psi / 14.5037738 

#convert pascals to pounds per square inch
def pascals2psi(pascals):
    return pascals / 6894.76    

#convert pounds per square inch to pascals
def psi2pascals(psi):
    return psi * 6894.76

#convert atmospheres to pounds per square inch
def atmospheres2psi(atmospheres):
    return atmospheres * 14.696 

#convert pounds per square inch to atmospheres
def psi2atmospheres(psi):
    return psi / 14.696 

#convert millimeters of mercury to pounds per square inch
def mmhg2psi(mmhg):
    return mmhg / 51.7149   

#convert pounds per square inch to millimeters of mercury       
def psi2mmhg(psi):
    return psi * 51.7149    
