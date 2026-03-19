class SmartList:

    # Object creation
    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        return super().__new__(cls)

    # Initialization
    def __init__(self, data):
        print("__init__ called")
        self.data = list(data)   # store data as list

    # String representation
    def __str__(self):
        return f"{self.data}"   # user-friendly

    def __repr__(self):
        return f"SmartList({self.data})"  # developer view

    # Operator overloading
    def __add__(self, other):
        return SmartList(self.data + other.data)  # +

    def __eq__(self, other):
        return self.data == other.data  # ==

    def __lt__(self, other):
        return len(self.data) < len(other.data)  # <

    # Attribute handling
    def __getattr__(self, name):
        return f"{name} not found"  # missing attribute

    def __setattr__(self, name, value):
        # small validation example
        if name == "data" and not isinstance(value, list):
            raise ValueError("data must be a list")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print(f"Deleted attribute: {name}")
        super().__delattr__(name)

    # Callable object
    def __call__(self):
        return f"Called! Length is {len(self.data)}"

    # Container behavior
    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        print(f"Deleting index {index}")
        del self.data[index]

    def __contains__(self, item):
        return item in self.data

    # Context manager
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


# Testing

obj = SmartList([1, 2, 3])
obj2 = SmartList([4, 5, 6, 7])

print(obj)              # __str__
print(repr(obj))        # __repr__

print(obj + obj2)       # __add__
print(obj == obj2)      # __eq__
print(obj < obj2)       # __lt__

print(len(obj))         # __len__
print(obj[0])           # __getitem__

obj[1] = 10             # __setitem__
print(obj)

del obj[0]              # __delitem__
print(obj)

print(10 in obj)        # __contains__

print(obj())            # __call__

print(obj.xyz)          # __getattr__

del obj.data            # __delattr__

with SmartList([9, 8]) as s:   # __enter__, __exit__
    print(s)