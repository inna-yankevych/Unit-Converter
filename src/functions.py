# Units I want to convert:

# TEMPERATURE:
# Celsius
# Farenheit
# Kelvin

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

def convert_length(value, from_unit, to_unit):
    # firsly I want to convert the value into meters:
    meters = value * lengths_distances[from_unit]

    # then back into the result unit:
    converted_value = meters / lengths_distances[to_unit]

    print(f'{value} {from_unit}s equals to {converted_value} {to_unit}s')


weight_mass = {
    "milligram": 0.001,
    "gram": 1,
    "kilogram": 1000,
    "ounce": 28.3495,
    "pound": 453.592,
    "tonne": 1000000
}

def convert_weight(value, to_unit, from_unit):
    #firstly we convert the value into grams:
    grams = value * weight_mass[from_unit]
    #then into the desired unit:
    converted_value = grams / weight_mass[to_unit]
    print(f'{value} {from_unit}s equals to {converted_value} {to_unit}s')
    return converted_value


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