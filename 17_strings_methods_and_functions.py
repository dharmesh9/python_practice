string1 = 'Dharmesh Makwana'
string2 = ' Dharmesh Makwana '
string3 = 'Dhams Mak'
string4 = 'Dhams,mak,dham5,m4k'


print(len(string1)) # Output 16.

print(string1.upper()) # Output 'DHARMESH MAKWANA'
print(string1.lower()) # Output 'dharmesh makwana'
print(string1.title()) # Output 'Dharemsh Makwana'
print(string1.capitalize()) # Output 'Dahrmesh makwana'

print(string2.strip()) # Remove extra spaces.
print(string2.lstrip()) # Remove left side extra spaces.
print(string2.rstrip()) # Remove right side extra spaces.


print(string3.find('Dhams')) # Output 0.
print(string3.replace('Dhams', 'Dharmesh')) # Output 'Dharmesh Mak'


print(string4.split()) # Output ['Dhams','Mak','Dham5','M4k']

print(string1.isalpha()) # False cause of space. 
print(string1.isalnum()) 
print(string1.isspace()) 