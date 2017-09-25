"""
Zachary Bedrosian
Session 7 Exercises
9.26.2017
"""

"""
Copy the loop from above and encapsulate it in a function called mysqrt that takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a.
To test it, write a function named test_square_root that prints a table like this:
"""

import math

# Define mysqrt in its own function
def mysqrt(x, a):
    y = x
    while True:
        y = (x + a/x) / 2
        if y == x:
            a = x
            return a
            break
        x = y


def test_square_root(x):
    iteration = 1

    # Table Headers
    print('a    mysqrt(a)     math.sqrt(a)  diff')
    print('-    ---------     ------------  ----')
    while iteration <= x:
        # create variables based on the math.sqrt and mysqrt functions
        math_output = math.sqrt(iteration)
        my_output = mysqrt(x, iteration)

        # Print the table
        print(float(iteration), '',my_output , '',math_output , '', float(abs(math_output-my_output)))
        iteration += 1


test_square_root(9)