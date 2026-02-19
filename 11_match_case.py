# match value:
#     case pattern1:
#         Code to execute if value matches pattern1
#     case pattern2:
#         Code to execute if value matches pattern2
#     case _:
#         Default case (if no patterns match)


value1 = 999


match value1:
    case 9:
        print('Value is 9.')
    case 99:
        print('Value is 99.')
    case 999:
        print('Value is 999.')
    case _:
        print('Unknown Value.')




value2 = int(input('Enter random number to win gifts.'))


match value2:
    case 5:
        print('You won £5 gift voucher.')
    case 7:
        print('You won 70% off coupen on spending above £999.')
    case 9:
        print('You won life.')