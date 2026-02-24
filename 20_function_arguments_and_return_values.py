

def multiplication(b, c):
    a = b * c
    # print(a)  # This would print the result inside the function
    return a   # Return the result

# multiplication(18,18)  
# This will work, but it will not display anything unless we print it.

# Calling the function and storing its returned value in a variable
varibale1 = multiplication(9, 9)
print(varibale1)


# Positional Arguments
def add(a, b):
    return a + b

print(add(9,9))  # Output: 8

# Default Arguments
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!

# Keyword Arguments
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=24, name="Dharmesh")