"""Volume calculations for 3D shapes."""

import math as _math


def sphere(radius):
    """Calculate the volume of a sphere."""
    return (4 / 3) * _math.pi * radius ** 3


def cube(side):
    """Calculate the volume of a cube."""
    return side ** 3


def cuboid(length, width, height):
    """Calculate the volume of a cuboid."""
    return length * width * height


def cylinder(radius, height):
    """Calculate the volume of a cylinder."""
    return _math.pi * radius ** 2 * height


def cone(radius, height):
    """Calculate the volume of a cone."""
    return (1 / 3) * _math.pi * radius ** 2 * height