# Program of the Day: Temperature Unit Converter

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value  # No conversion needed

    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value + 459.67) * 5/9
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value * 9/5) - 459.67

    return "Invalid units. Supported units: Celsius, Fahrenheit, Kelvin."

# Example usage: Convert 25 degrees Celsius to Fahrenheit
temperature_value = 25
from_temperature_unit = "Celsius"
to_temperature_unit = "Fahrenheit"

converted_temperature = convert_temperature(temperature_value, from_temperature_unit, to_temperature_unit)
print(f"{temperature_value} degrees {from_temperature_unit} is equal to {converted_temperature} degrees {to_temperature_unit}.")
