def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


boiling_c = 100
boiling_f = celsius_to_fahrenheit(boiling_c)
print(f"{boiling_c}°C = {boiling_f}°F")

freezing_f = 32
freezing_c = fahrenheit_to_celsius(freezing_f)
print(f"{freezing_f}°F = {freezing_c}°C")
