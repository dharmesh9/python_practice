list1 = [1,2,5,4,3]
list2 = ['dhams', 'mak', 'blah', 'blah', 'pokemon']
list3 = [9,18, 'string', 'float', 3.6]  


print(list1)
print(list2)
print(list3)

print(list1[0])
print(list1[2])

print(list2[2])
print(list2[4])

print(list3[1])
print(list3[3])


list1.append(6)
list1.insert(6,99)
list1.reverse()
list1.sort()
list1.pop(0)
print(list1)



list1.extend(list2)
list1.extend(list3)

print(list1)