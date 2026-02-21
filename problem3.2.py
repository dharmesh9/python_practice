# Print the multiplication table of a number (entered by user).

n = int(input("Enter your number: "))

for i in range (1, 11): 
    print(n, "X", i, "=", n*i) 