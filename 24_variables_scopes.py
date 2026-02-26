x = 99  # Global variable

def function1():
    x = 9  # Local variable
    print(x)  # Output: 9

function1()
print(x)  # Output: 99 (global x remains unchanged)



x = 99  # Global variable

def modify_global():
    global x
    x = 9  # Modifies the global x

modify_global()
print(x)  # Output: 9



# (__doc__) Docstrings - Writing Function Documentation
def add(a, b):
    """Returns this sentence."""
    return a + b

print(add.__doc__)  # Output: Returns this sentence.
    