# DICTIONARY PROGRAM WITH COMMENTS

# Creating a dictionary
student = {
    "name": "Dhams",
    "age": 24,
    "course": "Python"
}

# Printing dictionary
print(student)
# Output: {'name': 'Dhams', 'age': 24, 'course': 'Python'}


# Accessing values using keys
print(student["name"])
# Output: Dhams

print(student["age"])
# Output: 24


# Adding new key-value pair
student["grade"] = "A"
print(student)
# Output: {'name': 'Dhams', 'age': 24, 'course': 'Python', 'grade': 'A'}


# Updating value
student["age"] = 25
print(student)
# Output: {'name': 'Dhams', 'age': 25, 'course': 'Python', 'grade': 'A'}


# Removing element
student.pop("course")
print(student)
# Output: {'name': 'Dhams', 'age': 25, 'grade': 'A'}


# Dictionary Methods
print(student.keys())
# Output: dict_keys(['name', 'age', 'grade'])

print(student.values())
# Output: dict_values(['Dhams', 25, 'A'])

print(student.items())
# Output: dict_items([('name', 'Dhams'), ('age', 25), ('grade', 'A')])


# Length of dictionary
print(len(student))
# Output: 3


# Looping through dictionary
for key, value in student.items():
    print(key, value)

# Output:
# name Dhams
# age 25
# grade A