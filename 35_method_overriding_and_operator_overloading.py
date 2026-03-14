
# Define the parent class Vehicle
class Vehicle:

    # Constructor to initialize the vehicle name
    def __init__(self, name):
        # Store the vehicle name in an instance variable
        self.name = name

    # Method to start engine
    def start_engine(self):
        # Print a general message
        print("Vehicle engine starts")


# Define a child class Car that inherits from Vehicle
class Car(Vehicle):

    # Override the start_engine method
    def start_engine(self):
        # Print a car specific message
        print(self.name + " car engine starts with a key")


# Define another child class Bike that inherits from Vehicle
class Bike(Vehicle):

    # Override the start_engine method
    def start_engine(self):
        # Print a bike specific message
        print(self.name + " bike engine starts with a button")


# Create an object of Car class
car1 = Car("Toyota")

# Create an object of Bike class
bike1 = Bike("Yamaha")

# Call the start_engine method for car
car1.start_engine()

# Call the start_engine method for bike
bike1.start_engine()


# Define a class to demonstrate Operator Overloading
class Number:

    # Constructor to initialize number value
    def __init__(self, value):
        # Store the value
        self.value = value

    # Overload + operator using __add__ method
    def __add__(self, other):
        # Return the sum of two Number objects
        return Number(self.value + other.value)

    # Define how the object is printed
    def __str__(self):
        # Convert the value to string
        return str(self.value)


# Create first Number object
num1 = Number(10)

# Create second Number object
num2 = Number(20)

# Use overloaded + operator
result = num1 + num2

# Print the result
print("Sum is:", result)
