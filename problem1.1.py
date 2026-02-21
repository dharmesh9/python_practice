# Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

num = int(input("Enter a number: "))
print(num)

if(num<0):
    print("Number is negative!")

elif(num>0):
    print("Number is positive!")
    
else:
    print("Number is 0")


