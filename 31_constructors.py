
# Create a class called Cat (a blueprint for creating cat objects)
class Cat:
    # __init__ is a constructor, it runs automatically when we create an object
    def __init__(self, name, color):
        self.name = name      # save the cat's name
        self.color = color    # save the cat's color

# Create a cat object with name "Milo" and color "Black"
my_cat = Cat("Milo", "Black")

# Create the Cat class again but with default values
class Cat:
    # If no values are given, Python will use these default values
    def __init__(self, name="Unknown", color="White"):
        self.name = name      # store the cat's name
        self.color = color    # store the cat's color


# Create an object without giving values
# It will use default values: name="Unknown", color="White"
cat1 = Cat()

# Create an object giving only the name
# color will use the default value "White"
cat2 = Cat("Luna")

# Create an object giving both name and color
cat3 = Cat("Kitty", "Brown")

# Create an object giving both name and color
cat4 = Cat("Billu","Badmosh")

# Print the name and color of each cat
print(my_cat)
print(cat1.name, cat1.color)
print(cat2.name, cat2.color)
print(cat3.name, cat3.color)
print(cat4.name, cat4.color)
