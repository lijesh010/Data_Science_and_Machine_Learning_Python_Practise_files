'''
Exercise 10:
Create a Python module named temperature_conversion that contains functions to
convert Celsius to Fahrenheit and Fahrenheit to Celsius. Write a program to use this module to perform temperature conversions.
'''
#creating the module named temperature_conversion.
def celsius(fahrenheit):
    "This will convert the temperature from fahrenheit to celsius."
    cel=(fahrenheit-32) * 5/9
    return round(cel,2)
def fahrenheit(celsius):
    "This will convert the temperature from celsius to fahrenheit."
    fah=(celsius * 9/5) +32
    return fah
