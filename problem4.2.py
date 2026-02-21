#   Write a program that keeps asking the user to enter a password until they enter the correct one.


password = "Dh4m5"
entered_pass = input("Enter Password: ")

while (entered_pass != password):
    entered_pass = input("Wrong Password! Try again and enter Password: ")

print("Success! You are logged in")
