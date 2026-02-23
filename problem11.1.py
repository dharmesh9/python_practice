# Write a program that counts how many vowels are in a given string.

sentence = "a bcd e fh i jklmn o pqrst u vwxyz"
total = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in sentence.lower(): 
    if(char in vowels):
        total += 1

print(f"There are {total} vowels in this sentence")