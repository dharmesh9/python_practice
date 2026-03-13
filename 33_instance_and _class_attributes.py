# Define a class
class class1:
    std = 9   # Class attribute (shared by all objects of the class)

    # Method to store student details
    def student(self, name, mark, std):
        self.name = name   # Instance attribute (unique for each object)
        self.mark = mark   # Instance attribute (unique for each object)
        self.std = std     # Instance attribute that overrides the class attribute for that object
        
        # Return instance attributes as a tuple
        return self.name, self.mark, self.std


# Create first object of the class
obj1 = class1()

# Call the method and assign values to instance attributes
print(obj1.student('Dhams', 99, 3))


# Create second object
obj2 = class1()

# Call the method for second object (creates separate instance attributes)
print(obj2.student('Dharmesh', 999, 6))


# Create third object
obj3 = class1()

# Call the method for third object
print(obj3.student('Makwana', 9999, 9))


# Accessing the 'std' attribute from objects
# Since self.std was assigned inside the method, it became an instance attribute
print(obj1.std)  # prints 3 (instance attribute)
print(obj2.std)  # prints 6 (instance attribute)
print(obj3.std)  # prints 9 (instance attribute)


# Accessing the class attribute directly from the class
print(class1.std)  # prints 9 (original class attribute)
