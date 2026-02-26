# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

def sum_of_digits(n):
    if n == 0:
        return 0
    
    return n%10 + sum_of_digits(n//10)

print(sum_of_digits(1111))