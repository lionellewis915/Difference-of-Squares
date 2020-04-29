'''
Created by: Lionel Lewis

This algorithm takes a B value from the user 
and finds the difference of the squares.
'''

# Import the 'math' module to the project.
import math


# This function detects whether b is a square number, 
#calculates the value of B and formats the equation.
def is_square(b):
    if b ** 0.5 == int(b ** 0.5):
        b = int(math.sqrt(b))
        print("(x + {0})(x - {0})".format(SQUARE_ROOT + str(b)))

    else:
        b = b
        print("(x + {0})(x - {0})".format(SQUARE_ROOT + str(b)))

# Uni-Code characters for the Square Root and Sqyare sign.        
SQUARE_ROOT = u'\u221A'
SQUARED = u'\u00B2'

# Gets a value for B from the user and runs the 'is_square' function above.
if __name__ == "__main__":
    b = int(input('Enter b '))
    print('x', SQUARED, '-', b)
    is_square(b)