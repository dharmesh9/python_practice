# Define a class
class class1:
    std = 9   # Class variable (shared by all objects)

    # Method to store student name and mark
    def student(self, name, mark):
        self.name = name   # Instance variable (specific to object)
        self.mark = mark   # Instance variable (specific to object)
        return self.name, self.mark   # Return name and mark as tuple


# Create first object of class
obj1 = class1()

# Call student method and print result
print(obj1.student('Dhams', 99))


# Create second object
obj2 = class1()

# Call student method and print result
print(obj2.student('Dharmesh', 999))


# Create third object
obj3 = class1()

# Call student method and print result
print(obj3.student('Makwana', 9999))


# Access class variable using objects
print(obj1.std)  # prints 9
print(obj2.std)  # prints 9
print(obj3.std)  # prints 9