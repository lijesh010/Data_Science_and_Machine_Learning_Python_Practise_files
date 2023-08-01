'''
Exercise 5:
Create a Python module named calculator that
contains functions to add, subtract, multiply and divide two numbers. Write a program to use this module to perform calculations.
'''
#creating a module named calculator
def sum(x,y):
    s=x+y
    return s
def sub(x,y):
    s=x-y
    return s
def pro(x,y):
    s=x*y
    return s

def div(x,y):
    try:
        s=x/y
        return s
    except:
        print("Divide by zero is not possible")
