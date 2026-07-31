# math: mathematical functions and constants

import math

print("=" * 5, "Math constants", "=" * 5)

print(f"pi: {math.pi}")  # 3.141592653589793
print(f"e: {math.e}")  # 2.718281828459045
print(f"tau: {math.tau}")  # 6.283185307179586 (2 * pi)
print(f"inf: {math.inf}")  # inf
print(f"-inf: {-math.inf}")  # -inf
print(f"nan: {math.nan}")  # nan

print("=" * 5, "Rounding functions", "=" * 5)

print(f"ceil(3.2): {math.ceil(3.2)}")  # 4
print(f"ceil(-3.2): {math.ceil(-3.2)}")  # -3
print(f"floor(3.8): {math.floor(3.8)}")  # 3
print(f"floor(-3.8): {math.floor(-3.8)}")  # -4
print(f"trunc(3.8): {math.trunc(3.8)}")  # 3
print(f"trunc(-3.8): {math.trunc(-3.8)}")  # -3

# Difference between trunc and floor for negative numbers
print(f"floor(-2.3): {math.floor(-2.3)}")  # -3
print(f"trunc(-2.3): {math.trunc(-2.3)}")  # -2

print("=" * 5, "Power and logarithmic functions", "=" * 5)

print(f"sqrt(16): {math.sqrt(16)}")  # 4.0
print(f"pow(2, 10): {math.pow(2, 10)}")  # 1024.0
print(f"exp(1): {math.exp(1)}")  # 2.718281828459045 (e^1)
print(f"exp(0): {math.exp(0)}")  # 1.0
print(f"log(e): {math.log(math.e)}")  # 1.0 (natural log)
print(f"log2(8): {math.log2(8)}")  # 3.0
print(f"log10(1000): {math.log10(1000)}")  # 3.0
print(f"log(256, 2): {math.log(256, 2)}")  # 8.0 (log base 2)

# hypot: sqrt(x^2 + y^2)
print(f"hypot(3, 4): {math.hypot(3, 4)}")  # 5.0

print("=" * 5, "Trigonometric functions", "=" * 5)

# Angles in radians!
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(f"45 degrees = {angle_rad:.4f} radians")
print(f"pi/4 radians = {math.degrees(math.pi / 4):.1f} degrees")

print(f"sin(pi/2): {math.sin(math.pi / 2)}")  # 1.0
print(f"cos(0): {math.cos(0)}")  # 1.0
print(f"tan(pi/4): {math.tan(math.pi / 4)}")  # 1.0

# Inverse trig
print(f"asin(1): {math.asin(1)}")  # 1.570796... (pi/2)
print(f"acos(0): {math.acos(0)}")  # 1.570796... (pi/2)
print(f"atan(1): {math.atan(1)}")  # 0.785398... (pi/4)

# atan2(y, x): angle of vector (x, y)
print(f"atan2(1, 1): {math.degrees(math.atan2(1, 1)):.1f}")  # 45.0 degrees
print(f"atan2(1, 0): {math.degrees(math.atan2(1, 0)):.1f}")  # 90.0 degrees

print("=" * 5, "Absolute value and sign", "=" * 5)

print(f"fabs(-5.5): {math.fabs(-5.5)}")  # 5.5 (always returns float)
print(f"fabs(3): {math.fabs(3)}")  # 3.0
print(f"copysign(5, -1): {math.copysign(5, -1)}")  # -5.0 (magnitude of first, sign of second)
print(f"copysign(-5, 1): {math.copysign(-5, 1)}")  # 5.0

print("=" * 5, "Combinatorial and number theory", "=" * 5)

print(f"factorial(5): {math.factorial(5)}")  # 120
print(f"factorial(0): {math.factorial(0)}")  # 1
# math.factorial(-1)  # ValueError

# Combinatorics: n choose k
print(f"comb(10, 3): {math.comb(10, 3)}")  # 120 (10! / (3! * 7!))
print(f"comb(52, 5): {math.comb(52, 5)}")  # 2598960 (poker hands)

# Permutations: n! / (n-k)!
print(f"perm(10, 3): {math.perm(10, 3)}")  # 720
print(f"perm(5, 5): {math.perm(5, 5)}")  # 120 (same as 5!)

# Greatest common divisor
print(f"gcd(12, 8): {math.gcd(12, 8)}")  # 4
print(f"gcd(100, 75): {math.gcd(100, 75)}")  # 25

# Least common multiple (Python 3.9+)
print(f"lcm(4, 6): {math.lcm(4, 6)}")  # 12
print(f"lcm(3, 5, 7): {math.lcm(3, 5, 7)}")  # 105

print("=" * 5, "Special functions", "=" * 5)

# erf and erfc: error function (used in statistics)
print(f"erf(0): {math.erf(0)}")  # 0.0
print(f"erf(1): {math.erf(1):.6f}")  # 0.842701
print(f"erfc(0): {math.erfc(0)}")  # 1.0

# gamma function
print(f"gamma(1): {math.gamma(1)}")  # 1.0 (0! = 1)
print(f"gamma(5): {math.gamma(5)}")  # 24.0 (4! = 24)

# lgamma: log of absolute value of gamma
print(f"lgamma(5): {math.lgamma(5)}")  # 3.1780538... (ln(24))

print("=" * 5, "Floating point utilities", "=" * 5)

# Check for special values
print(f"isinf(inf): {math.isinf(math.inf)}")  # True
print(f"isinf(1.0): {math.isinf(1.0)}")  # False
print(f"isnan(nan): {math.isnan(math.nan)}")  # True
print(f"isnan(1.0): {math.isnan(1.0)}")  # False
print(f"isfinite(inf): {math.isfinite(math.inf)}")  # False
print(f"isfinite(1.0): {math.isfinite(1.0)}")  # True

# fmod: floating-point remainder (same sign as dividend)
print(f"fmod(10, 3): {math.fmod(10, 3)}")  # 1.0
print(f"fmod(-10, 3): {math.fmod(-10, 3)}")  # -1.0
# Compare with %
print(f"10 % 3: {10 % 3}")  # 1
print(f"-10 % 3: {-10 % 3}")  # 2 (different from fmod!)

# frexp: normalized fraction and exponent
m, e = math.frexp(8.0)
print(f"frexp(8.0): mantissa={m}, exponent={e}")  # mantissa=0.5, exponent=4 (0.5 * 2^4 = 8)
# ldexp: inverse of frexp
print(f"ldxp(0.5, 4): {math.ldexp(0.5, 4)}")  # 8.0

# modf: fractional and integer parts
frac, integer = math.modf(3.14)
print(f"modf(3.14): fractional={frac}, integer={integer}")  # fractional=0.14, integer=3.0

# nextafter: next representable float
print(f"nextafter(1.0, 2.0): {math.nextafter(1.0, 2.0)}")  # 1.0000000000000002
print(f"nextafter(0.0, 1.0): {math.nextafter(0.0, 1.0)}")  # 5e-324 (smallest positive float)

# ulp: unit in the last place
print(f"ulp(1.0): {math.ulp(1.0)}")  # 2.220446049250313e-16