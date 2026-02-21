# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.


num = int(input("Enter a number\n"))

match num:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")