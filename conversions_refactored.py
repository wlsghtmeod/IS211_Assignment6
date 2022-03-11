from logging import exception
import string

class ConversionNotPossible(Exception):
    pass


def convert(fromUnit=string, toUnit=string, value=float) -> float:
    if not fromUnit or not toUnit or not value:
        raise ValueError("Missing required values.")
    
    if fromUnit == toUnit:
        return value
    
    #Temperature Conversion
    #From C
    if fromUnit == 'C':
        if toUnit == 'F':
            return value * (9/5) + 32
        if toUnit == 'K':
            return value + 273.15
        else:
            raise ConversionNotPossible("Conversion Not Possible")
    
    #From F
    if fromUnit == 'F':
        if toUnit == 'C':
            return (value - 32) / (9/5)
        elif toUnit == 'K':
            return (value + 459.67) * (5/9)
        else:
            raise ConversionNotPossible("Conversion Not Possible")
    
    #From K
    if fromUnit == 'K':
        if toUnit == 'F':
            return (value * (9/5) - 459.67)
        elif toUnit == 'C':
            return (value - 273.15)
        else:
            raise ConversionNotPossible("Conversion Not Possible")
    
    #Distance Conversion
    #From Centimeter
    if fromUnit == 'M':
        if toUnit == 'Mi':
            return value * 0.0006213712
        elif toUnit == 'Y':
            return value * 1.0936132983
        else:
            raise ConversionNotPossible("Conversion Not Possible")

    if fromUnit == 'Mi':
        if toUnit == 'M':
            return value * 1609.344
        elif toUnit == 'Y':
            return value * 1760
        else:
            raise ConversionNotPossible("Conversion Not Possible")

    if fromUnit == 'Y':
        if toUnit == 'M':
            return value * 0.9144
        elif toUnit == 'Mi':
            return value * 0.0005681818
        else:
            raise ConversionNotPossible("Conversion Not Possible")
    else:
        raise Exception("Something went wrong")


