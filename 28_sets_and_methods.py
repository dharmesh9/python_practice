# Creating a set
set1 = {6, 3, 9, 18, 27, 45}

# Printing set
print(set1)  
# Output: {3, 6, 9, 18, 27, 45}  (order may vary)


# Adding elements
set1.add(36)
print(set1)
# Output: {3, 6, 9, 18, 27, 45, 36}  (order may vary)

# Removing elements
set1.remove(45)
print(set1)
# Output: {3, 6, 9, 18, 27, 36}  (order may vary)

set1.discard(100)   # No error if element not found
print(set1)
# Output: {3, 6, 9, 18, 27, 36}  (order may vary)


# Set Operations

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
# Output: {1, 2, 3, 4, 5}

print(a.intersection(b))
# Output: {3}

print(a.difference(b))
# Output: {1, 2}

print(a.symmetric_difference(b))
# Output: {1, 2, 4, 5}


# Membership test
print(2 in a) # Output: True

# Length of set
print(len(a)) # Output: 3


# Looping through set
for i in a:
    print(i)
# Output:
# 1
# 2
# 3
# (order may vary)