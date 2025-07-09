"""
  Convert between different units of measurement
  developer: Cristian
  date: 2025-07-09
  version: 1.0.0
  license: MIT License

  description: This module provides functions to convert between time units 
  such as seconds, minutes, hours, days, and weeks.
"""
#convert seconds to minutes
def sec2min(seconds):
    return seconds / 60

#convert minutes to seconds
def min2sec(minutes):
    return minutes * 60

#convert seconds to hours
def sec2hours(seconds):
    return seconds / 3600

#convert hours to seconds
def hours2sec(hours):
    return hours * 3600

#convert minutes to hours
def min2hours(minutes):
    return minutes / 60

#convert hours to minutes
def hours2min(hours):
    return hours * 60

#convert seconds to days
def sec2days(seconds):
    return seconds / 86400

#convert days to seconds
def days2sec(days): 
    return days * 86400

#convert minutes to days
def min2days(minutes):
    return minutes / 1440

#convert days to minutes
def days2min(days):
    return days * 1440

#convert hours to days
def hours2days(hours):
    return hours / 24

#convert days to hours
def days2hours(days):
    return days * 24

#convert seconds to weeks
def sec2weeks(seconds):
    return seconds / 604800

#convert weeks to seconds
def weeks2sec(weeks):
    return weeks * 604800

#convert minutes to weeks
def min2weeks(minutes):
    return minutes / 10080

#convert weeks to minutes
def weeks2min(weeks):
    return weeks * 10080

#convert hours to weeks
def hours2weeks(hours):
    return hours / 168

#convert weeks to hours
def weeks2hours(weeks):
    return weeks * 168

#convert days to weeks
def days2weeks(days):
    return days / 7

#convert weeks to days
def weeks2days(weeks):
    return weeks * 7
