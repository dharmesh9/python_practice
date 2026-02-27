# TUPLE PROGRAM WITH COMMENTS

# Creating tuples
tuple1 = (1, 2, 5, 4, 3)
tuple2 = ('dhams', 'mak', 'blah', 'blah', 'pokemon')
tuple3 = (9, 18, 'string', 'float', 3.6)

# Printing tuples
print(tuple1)
print(tuple2)
print(tuple3)

# Accessing elements using index
print(tuple1[0])   # First element of tuple1
print(tuple1[2])   # Third element of tuple1

print(tuple2[2])   # Third element of tuple2
print(tuple2[4])   # Fifth element of tuple2

print(tuple3[1])   # Second element of tuple3
print(tuple3[3])   # Fourth element of tuple3


# Tuple Methods (Only 2 methods available)

print(tuple1.count(4))   # Counts how many times 4 appears
print(tuple1.index(5))   # Returns index position of value 5


# Tuple Operations

# Concatenation (joining tuples)
new_tuple = tuple1 + tuple2
print(new_tuple)

# Adding elements (Tuples are immutable, so we create a new tuple)
tuple1 = tuple1 + (6, 99)
print(tuple1)

# Slicing
print(tuple1[1:4])   # Prints elements from index 1 to 3

# Length of tuple
print(len(tuple1))   # Prints total number of elements


# Combining all tuples (like extend in list)
combined = tuple1 + tuple2 + tuple3
print(combined)