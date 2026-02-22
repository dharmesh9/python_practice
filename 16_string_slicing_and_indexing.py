string1 = 'Dharmesh'

#     D  h  a  r  m  e  s  h
#     0  1  2  3  4  5  6  7


print(string1[0])
print(string1[1])
print(string1[2])
print(string1[3])
print(string1[4])
print(string1[5])
print(string1[6])
print(string1[7])



print(string1[0:8]) # Output 'Dharmesh' 
print(string1[2:6]) # Output 'arme'
print(string1[0:-1]) # Output 'Dharmes'
print(string1[:-1]) # Output 'Dharmes'
print(string1[3:]) # Output 'rmesh'
print(string1[-5:-1]) # Output ''rmes'
print(string1[0:8:2]) #  Output 'Dams', skips n-1 charaters, here n is 2 so it will skip 2-1=1 charater.


print(string1[::-1]) # Output 'hsermrahD' , Reverse String
print(string1[-8:-1]) # Output 'Dharmes'
print(string1[::-2]) # Output 'herh'
print(string1[::2])  # Output'Dams'