# Write a loop that goes through numbers 1 to 5, but does nothing for number 2 (use pass).

for i in range(1, 6):
    match i:
        case 1:
            print(1)
        case 2:
            pass
        case 3:
            print(3)
        case 4:
            print(4)
        case 5:
            print(5)