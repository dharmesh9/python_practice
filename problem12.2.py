# Create a list [9,99,999,9999,99999] and use map() with a lambda function to get their squares.

square = lambda x: x*x
list1 = [9,99,999,9999,99999]

print(list(map(square, list1)))