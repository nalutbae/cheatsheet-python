# Packages: organizing modules into directories

import os
import sys

# Add this module's directory to path for sibling imports
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 5, "What is a package?", "=" * 5)

# A package is a directory containing Python modules and an __init__.py file.
# __init__.py can be empty or contain package-level initialization code.

# Importing from our sample package
from shapes_package import area, perimeter

print(f"area.circle(5): {area.circle(5):.2f}")  # 78.54
print(f"area.rectangle(3, 4): {area.rectangle(3, 4)}")  # 12
print(f"area.triangle(6, 4): {area.triangle(6, 4)}")  # 12.0

print(f"perimeter.circle(5): {perimeter.circle(5):.2f}")  # 31.42
print(f"perimeter.rectangle(3, 4): {perimeter.rectangle(3, 4)}")  # 14

print("=" * 5, "Import styles for packages", "=" * 5)

# Import entire module from package
import shapes_package.area as sa

print(f"sa.square(4): {sa.square(4)}")  # 16

# Import specific function from submodule
from shapes_package.area import circle

print(f"circle(3): {circle(3):.2f}")  # 28.27

# Import using alias
from shapes_package import perimeter as sp

print(f"sp.square(4): {sp.square(4)}")  # 16

# Access package-level constants from __init__.py
from shapes_package import PACKAGE_NAME, VERSION

print(f"Package: {PACKAGE_NAME}, Version: {VERSION}")  # shapes_package, 1.0.0

print("=" * 5, "sys.path and module search", "=" * 5)

# Python searches for modules in sys.path directories
print("sys.path entries:")
for p in sys.path[:5]:
    print(f"  {p}")

# Adding a custom directory to sys.path
custom_path = "/tmp/my_modules"
# sys.path.append(custom_path)  # uncomment to add at end
# sys.path.insert(0, custom_path)  # uncomment to add at beginning (higher priority)

print("=" * 5, "Package __init__.py behavior", "=" * 5)

# __init__.py runs when the package is first imported
# It can define what is available at the package level

# The shapes_package __init__.py imports area and perimeter modules
# so they are available as shapes_package.area and shapes_package.perimeter

import shapes_package

# Package-level attributes defined in __init__.py
print(f"Package name: {shapes_package.PACKAGE_NAME}")  # shapes_package
print(f"Version: {shapes_package.VERSION}")  # 1.0.0

# List names available in the package
print(f"Package contents: {[n for n in dir(shapes_package) if not n.startswith('_')][:10]}")

print("=" * 5, "Relative imports within packages", "=" * 5)

# The shapes_package modules use relative imports internally:
# from .area import circle  — imports from the same package
# from .. import something  — imports from the parent package
# These only work inside packages, not when running a module directly

# Demonstrate that relative imports work when imported from outside
from shapes_package.shapes_3d import volume

print(f"volume.sphere(5): {volume.sphere(5):.2f}")  # 523.60
print(f"volume.cube(3): {volume.cube(3)}")  # 27