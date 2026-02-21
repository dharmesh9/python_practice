'''
Write a program using match case that simulates a simple calculator.
    Ask the user for two numbers and an operation (+, -, *, /).
    Perform the operation using match case.
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Choose operation: ")

match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)