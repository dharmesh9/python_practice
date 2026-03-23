# Import reduce function from functools
from functools import reduce

# Step 1: Original list of numbers
numbers = [1, 2, 3, 4, 5]
print("Original numbers:", numbers)

# Step 2: FILTER
# Keep only even numbers (numbers divisible by 2)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("After FILTER (keep even numbers):", evens)
# Explanation: 1, 3, 5 are removed → [2, 4]

# Step 3: MAP
# Square each remaining number
squares = list(map(lambda x: x * x, evens))
print("After MAP (square each number):", squares)
# Explanation: 2 → 4, 4 → 16 → [4, 16]

# Step 4: REDUCE
# Add all the squared numbers together
total = reduce(lambda a, b: a + b, squares)
print("After REDUCE (sum of squares):", total)
# Explanation: 4 + 16 = 20

# Summary
print("\nSummary:")
print("Original list:", numbers)
print("Even numbers:", evens)
print("Squares of even numbers:", squares)
print("Sum of squares:", total)