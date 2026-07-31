# random: pseudo-random number generation

import random

print("=" * 5, "Basic random numbers", "=" * 5)

# Seed for reproducibility
random.seed(42)
a = random.random()  # float in [0.0, 1.0)
print(f"random(): {a:.6f}")  # 0.639426...

# Without seed: different results each time
random.seed()  # reset to system-based seed

# Random float in range
print(f"uniform(1, 10): {random.uniform(1, 10):.4f}")  # float in [1.0, 10.0]
print(f"uniform(0, 1): {random.uniform(0, 1):.6f}")  # same as random()

# Random integer
print(f"randint(1, 6): {random.randint(1, 6)}")  # int in [1, 6] (inclusive both ends)
print(f"randint(0, 100): {random.randint(0, 100)}")  # int in [0, 100]

# randrange: integer with step
print(f"randrange(10): {random.randrange(10)}")  # int in [0, 10)
print(f"randrange(1, 11): {random.randrange(1, 11)}")  # int in [1, 11)
print(f"randrange(0, 10, 2): {random.randrange(0, 10, 2)}")  # even number in [0, 10)

# getrandbits: random integer with given number of bits
print(f"getrandbits(8): {random.getrandbits(8)}")  # 0-255
print(f"getrandbits(4): {random.getbitbits(4)}" if False else "")  # placeholder

print("=" * 5, "Random choices and sampling", "=" * 5)

# random.choice: pick one random element
colors = ["red", "green", "blue", "yellow", "orange"]
print(f"choice(colors): {random.choice(colors)}")

# random.choices: pick multiple elements WITH replacement
dice = [1, 2, 3, 4, 5, 6]
rolls = random.choices(dice, k=5)
print(f"5 dice rolls: {rolls}")  # e.g., [3, 1, 6, 2, 5]

# Weighted choices
population = ["A", "B", "C"]
weights = [50, 30, 20]
results = random.choices(population, weights=weights, k=10)
print(f"Weighted choices: {results}")  # more A's than B's, more B's than C's

# random.sample: pick multiple elements WITHOUT replacement
deck = list(range(1, 53))  # 52 cards
hand = random.sample(deck, 5)
print(f"Poker hand: {sorted(hand)}")  # 5 unique cards

lottery = random.sample(range(1, 46), 6)
print(f"Lottery numbers: {sorted(lottery)}")  # 6 unique numbers from 1-45

# Sample can also work with strings
sampled_chars = random.sample("abcdefghij", 3)
print(f"Sampled chars: {sampled_chars}")

print("=" * 5, "Shuffling", "=" * 5)

# random.shuffle: shuffle a list in place
numbers = list(range(1, 11))
print(f"Before shuffle: {numbers}")
random.shuffle(numbers)
print(f"After shuffle: {numbers}")

# Shuffle with a copy (don't modify original)
original = [1, 2, 3, 4, 5]
shuffled = original[:]  # make a copy
random.shuffle(shuffled)
print(f"Original: {original}")  # [1, 2, 3, 4, 5]
print(f"Shuffled: {shuffled}")  # random order

print("=" * 5, "Statistical distributions", "=" * 5)

# Normal (Gaussian) distribution
mu, sigma = 0, 1
normal_value = random.gauss(mu, sigma)
print(f"gauss(0, 1): {normal_value:.4f}")  # random from N(0,1)

# Generate multiple normal values
normal_samples = [random.gauss(100, 15) for _ in range(5)]
print(f"5 normal samples (mean=100, std=15): {[f'{x:.1f}' for x in normal_samples]}")

# Other distributions
print(f"lognormvariate(0, 1): {random.lognormvariate(0, 1):.4f}")
print(f"expovariate(1): {random.expovariate(1):.4f}")  # exponential with rate 1
print(f"betavariate(2, 5): {random.betavariate(2, 5):.4f}")
print(f"gammavariate(2, 2): {random.gammavariate(2, 2):.4f}")
print(f"triangular(0, 10, 5): {random.triangular(0, 10, 5):.4f}")  # low, high, mode

# Uniform on a circle (random angle)
angle = random.uniform(0, 2 * math.pi) if (math := __import__('math')) else 0
print(f"Random angle: {angle:.4f} radians")

print("=" * 5, "Practical examples", "=" * 5)

# Random password generator
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(alphabet, k=length))

for _ in range(3):
    print(f"Password: {generate_password(16)}")

# Random color generator
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

print(f"Random colors: {[random_color() for _ in range(5)]}")

# Weighted random selection (like a weighted lottery)
def weighted_select(items, weights):
    total = sum(weights)
    r = random.uniform(0, total)
    cumulative = 0
    for item, weight in zip(items, weights):
        cumulative += weight
        if r <= cumulative:
            return item
    return items[-1]

prizes = ["Gold", "Silver", "Bronze", "Try Again"]
prize_weights = [1, 5, 10, 84]
results = [weighted_select(prizes, prize_weights) for _ in range(20)]
from collections import Counter
print(f"Prize distribution: {Counter(results)}")

# Monte Carlo estimation of pi
def estimate_pi(num_points=100000):
    inside = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / num_points

pi_estimate = estimate_pi(100000)
print(f"Pi estimate (Monte Carlo): {pi_estimate:.4f} (actual: 3.1416)")

# Random matrix generation
def random_matrix(rows, cols, low=0, high=10):
    return [[random.randint(low, high) for _ in range(cols)] for _ in range(rows)]

matrix = random_matrix(3, 3)
print("Random matrix:")
for row in matrix:
    print(f"  {row}")