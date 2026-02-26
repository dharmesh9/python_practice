''' 
Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

Both length and width
Only length (use default width)
'''
def calculate_area(length, width=10):
    return length * width


print(f"The area of this rectangle is {calculate_area(9, 27)}")
print(calculate_area(18))