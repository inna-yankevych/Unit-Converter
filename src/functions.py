# Units I want to convert:

# TEMPERATURE:
# Celsius
# Farenheit
# Kelvin

# LENGTH / DISTANCE:
# millimeters
# centimeters
# meters
# kilometers
# inches
# feet
# yards
# miles

# the distionary key corresponds to 1 unit of that measurement (eg. 1 millimeter), and the corresponding value is how many meters is in that 1 unit.
lengths_distances = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34
}

def convert_length():
    value = float(input('Please enter a value to convert: '))
    from_unit = input('Please enter the unit to convert from: ')
    to_unit = input('Please enter the unit to convert to: ')
    # firsly I want to convert the value into meters:
    meters = value * lengths_distances[from_unit]

    # then back into the result unit:
    converted_value = meters / lengths_distances[to_unit]

    print(f'Your value of {value} in {from_unit}s was converted to {to_unit}s with a value of {converted_value}')

# WEIGHT / MASS:
# milligrams
# grams
# kilograms
# ounces
# pounds
# tons

# VOLUME / CAPACITY:
# milliliters
# liters
# cups
# pints
# quarts
# gallons
# fluid ounces

# TIME:
# seconds
# minutes
# hours
# days
# weeks
# months
# years

time_units = {
    "second": 0.000277778,
    "minute": 0.0166667,
    "hour": 1,
    "day": 24,
    "week": 168,
    "month": 730.001,
    "year": 8760
}

# SPEED:
# meters per second
# kilometers per hour
# miles per hour

# AREA:
# square meter
# square kilometer
# square mile
# square yard
# square foot
# hectare
# acre