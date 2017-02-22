#/bin/python3

# Exercise 3.1
# Write a function named right_justify that takes a string named s as a parameter and prints the string with enough
# leading spaces so that the last letter of the string is in column 70 of the display.

def right_justify(s):
    """
    :param s:
    :return:

    prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.
    """

    blanks = 70 - len(s)
    # for testing purposes I print the next two lines so it's easy to see if I did the correct calculation.
    print("         1         2         3         4         5         6         7")
    print("123456789.123456789.123456789.123456789.123456789.123456789.123456789.")
    print((blanks*" ") + s)

right_justify("right.")