'''
Exercise 8:
Create a Python module named math_operations that contains functions to calculate the area of a circle,
the area of a rectangle and the area of a triangle. Write a program to use this module to perform area calculations.
'''
#creating the module
from math import pi
def circle_area(r):
    'r=radius of circle'
    a=round(pi*r*r,2)
    return a
def rect_area(x,y):
    'x&y are the sides of rectangle'
    a=x*y
    return a
def tri_area(b,h):
    'b&h are the base and height of triangle'
    a=0.5*b*h
    return a
