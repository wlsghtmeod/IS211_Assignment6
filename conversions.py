def convertCelsiusToKelvin(celsius):
    return celsius + 273.15
    
def convertCelsiusToFahrenheit(celsius):    
    return celsius * (9/5) + 32

def convertFahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) / (9/5)

def convertFahrenheitToKelvin(fahrenheit):
    return (fahrenheit + 459.67) * (5/9)

def convertKelvinToFahrenheit(kelvin):
    return kelvin * (9/5) - 459.67

def convertKelvinToCelsius(kelvin):
    return kelvin - 273.15