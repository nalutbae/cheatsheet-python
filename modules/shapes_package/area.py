"""Area calculations for 2D shapes."""

import math as _math


def circle(radius):
    """Calculate the area of a circle."""
    return _math.pi * radius ** 2


def rectangle(width, height):
    """Calculate the area of a rectangle."""
    return width * height


def triangle(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height


def square(side):
    """Calculate the area of a square."""
    return side ** 2


def trapezoid(base1, base2, height):
    """Calculate the area of a trapezoid."""
    return 0.5 * (base1 + base2) * height