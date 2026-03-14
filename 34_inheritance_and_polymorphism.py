
# Define the parent class called Vehicle
class Vehicle:

    # Constructor method that runs when an object is created
    def __init__(self, name):
        # Store the name of the vehicle in an instance variable
        self.name = name

    # Define a method that will be overridden by child classes
    def start_engine(self):
        # Print a general message for starting a vehicle
        print("Vehicle engine starts")


# Define a child class Car that inherits from Vehicle
class Car(Vehicle):

    # Override the start_engine method from the parent class
    def start_engine(self):
        # Print a specific message for starting a car
        print(self.name + " car engine starts with a key")


# Define another child class Bike that inherits from Vehicle
class Bike(Vehicle):

    # Override the start_engine method from the parent class
    def start_engine(self):
        # Print a specific message for starting a bike
        print(self.name + " bike engine starts with a button")


# Create an object of the Car class with name "Toyota"
car1 = Car("Toyota")

# Create an object of the Bike class with name "Yamaha"
bike1 = Bike("Yamaha")

# Call the start_engine method for the car object
car1.start_engine()

# Call the start_engine method for the bike object
bike1.start_engine()

# Print a blank line and message to separate output
print("\nUsing Polymorphism with a loop:\n")

# Create a list containing both vehicle objects
vehicles = [car1, bike1]

# Loop through each object in the vehicles list
for v in vehicles:

    # Call the same start_engine method for each object
    # Python automatically decides which version to run
    v.start_engine()
