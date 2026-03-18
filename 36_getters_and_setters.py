# Define a class named Customer
class Perosn:
    
    # Constructor to initialize private variables
    def __init__(self):
        self.__first_name = ""   # private variable for first name
        self.__last_name = ""    # private variable for last name

    # Setter method to set first name
    def set_first_name(self, first_name):
        self.__first_name = first_name

    # Setter method to set last name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    # Getter method to get first name
    def get_first_name(self):
        return self.__first_name

    # Getter method to get last name
    def get_last_name(self):
        return self.__last_name


# Create an object of Customer class
obj1 = Customer()

# Set values using setter methods (no user input)
obj1.set_first_name("Dharmesh")
obj1.set_last_name("Makwana")

# Display the stored values using getter methods
print("\n--- Person Details ---")
print("First Name:", obj1.get_first_name())
print("Last Name:", obj1.get_last_name())