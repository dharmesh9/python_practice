# Start a 'try' block to catch potential errors
try:
    # INPUT: Get the first number from the user and convert to float
    num1 = float(input("Enter first number: ")) 

    # INPUT: Get the second number from the user and convert to float
    num2 = float(input("Enter second number: ")) 

    # ADDITION
    print(f"Add: {num1 + num2}") 

    # SUBTRACTION
    print(f"Subtract: {num1 - num2}") 

    # MULTIPLICATION
    print(f"Multiply: {num1 * num2}") 

    # DIVISION with an internal check for Zero
    if num2 != 0:
        print(f"Divide: {num1 / num2}")
        print(f"Modulo: {num1 % num2}")
    else:
        print("Divide/Modulo: Error (Cannot divide by zero)")

    # PERCENTAGE: Calculate num1% of num2
    print(f"Percentage: {(num1 / 100) * num2}")

# ERROR: This runs if the user enters text instead of a number
except ValueError:
    print("Invalid Input: Please enter numeric values only.")

# ERROR: This catches any other unexpected errors
except Exception as e:
    print(f"An unexpected error occurred: {e}")