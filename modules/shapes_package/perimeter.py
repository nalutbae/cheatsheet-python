"""Perimeter calculations for 2D shapes."""

import math as _math


def circle(radius):
    """Calculate the circumference of a circle."""
    return 2 * _math.pi * radius


def rectangle(width, height):
    """Calculate the perimeter of a rectangle."""
    return 2 * (width + height)


def square(side):
    """Calculate the perimeter of a square."""
    return 4 * side


def triangle(a, b, c):
    """Calculate the perimeter of a triangle."""
    return a + b + c