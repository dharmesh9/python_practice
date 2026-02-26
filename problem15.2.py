# Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.

def multiply(a, b):
    '''
    Multiply two numbers.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    '''
    return a * b


print(multiply(5, 3))   # 15
print(multiply(2.5, 4)) # 10.0
help(multiply)