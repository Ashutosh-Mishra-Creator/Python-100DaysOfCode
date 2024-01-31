def square(number):
    # print(number)  # This leads to __doc__ to return "None"
    """Takes in a number n, returns the square of n"""
    return print(number * 2)


square(12)
print(square.__doc__)

import this  # ester egg