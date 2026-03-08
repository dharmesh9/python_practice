# Define a decorator function
def decorator(func):
    
    # Wrapper function that adds extra behavior
    def wrapper():
        # Code that runs BEFORE the original function
        print('I will run.')
        
        # Call the original function passed to the decorator
        func()
        
        # Code that runs AFTER the original function
        print('I ran.')
    
    # Return the wrapper function instead of the original function
    return wrapper


# Apply the decorator to func1
# This is equivalent to: func1 = decortor(func1)
@decorator
def func1():
    # Original function logic
    print("I am running.")


# Call the decorated function
# Actually calls wrapper() which then calls func1()
func1()



# Manual way of applying decorator (without @ syntax)
# a = decortor(func1)   # decorator returns wrapper function
# a()                   # calling wrapper(), which runs extra code