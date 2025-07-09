from converter import area,distance,pressure,temperature,time_converter,volume,weight
# Example usage of the converter modules
def main():
    # Area conversions
    sqm = 1000
    print(f"{sqm} square meters is {area.sqm2sqkm(sqm)} square kilometers")
    
    # Distance conversions
    km = 5
    print(f"{km} kilometers is {distance.km2miles(km)} miles")
    
    # Pressure conversions
    pascals = 101325
    print(f"{pascals} pascals is {pressure.pascals2bars(pascals)} bars")
    
    # Temperature conversions
    celsius = 25
    print(f"{celsius} degrees Celsius is {temperature.celsius2fahrenheit(celsius)} degrees Fahrenheit")
    
    # Time conversions
    seconds = 3600
    print(f"{seconds} seconds is {time_converter.sec2hours(seconds)} hours")
    
    # Volume conversions
    liters = 10
    print(f"{liters} liters is {volume.liters2gallons(liters)} gallons")
    
    # Weight conversions
    kilograms = 70
    print(f"{kilograms} kilograms is {weight.kg2pounds(kilograms)} pounds")

main()