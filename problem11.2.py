# Take a user input string and check if it is a palindrome (same forwards and backwards).

string1 = "922229"

if(string1 == string1[::-1]):
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")