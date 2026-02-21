for i in range(9):
    if i == 5:
        break # cancel execution at here
    print(i)  # Output: 0, 1, 2, 3, 4



for i in range(9):
    if i == 5:
        continue # skips current place and continue
    print(i)  # Output: 0, 1, 2, 3, skips 5, 6, 7, 8



for i in range(9):
    if i == 5:
        pass #  does nothing
    print(i)  # Output: 0, 1, 2, 3, 4, 5, 6, 7, 8