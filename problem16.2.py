# Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.

def safe_divide(a, b):
    '''
    Safely divide a by b.

    Parameters:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        float or str: The result of division, or an error message if b is 0.
    '''
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(safe_divide(10, 2))  # 5.0
print(safe_divide(7, 0))   # Cannot divide by zero
