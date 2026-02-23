#String Format

string1 = 'Hello {}, Good Morning!!! Your age is {}.'


name1 = 'Dharmesh'
age1 = 24

name2 = 'Dhams'
age2 = 25

name3 = 'Dhams Mak'
age3 = 26

format_string1 = string1.format(name1,age1)
print(format_string1) 
format_string2 = string1.format(name2,age2)
print(format_string2) 
format_string3 = string1.format(name3,age3)
print(format_string3) 


# f-string

f_string1 = f'Hello {name1}, Good Morning!!! Your age is {age1}.'
f_string2 = f'Hello {name2}, Good Morning!!! Your age is {age2}.'
f_string3 = f'Hello {name3}, Good Morning!!! Your age is {age3}.'

print(f_string1)
print(f_string2)
print(f_string3)


text = "Dharmesh"
print(f"{text:>10}")  # Right align
print(f"{text:<10}")  # Left align
print(f"{text:^10}")  # Center align