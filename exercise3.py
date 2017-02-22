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

def do_twice(f, v):
    f(v)
    f(v)

def print_spam(v):
    print('spam ' + str(v))

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)

print("Exercise 3.1")
right_justify("right.")

print("Exercise 3.2")
# Exercise 3.2
# A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function
# that takes a function object...
do_twice(print_spam, 'pre-spam')
do_twice(print_twice,'spam')
do_four(print_spam,'4-spam')

print("Exercise 3.3")
n2 = 4
print("+", n2*'-', "+", n2*"-", "+")
for x in range(n2):
    print("|", n2*' ', "|", n2*" ", "|")
print("+", n2*'-', "+", n2*"-", "+")
for x in range(n2):
    print("|", n2*' ', "|", n2*" ", "|")
print("+", n2*'-', "+", n2*"-", "+")

# The book asks for
# Write a function that draws a similar grid with four rows and four columns.
# But you need 5 rows and 5 columns to get the repeating pattern and the following does that:
n2 = 1
print("+", n2*'-', "+", n2*"-", "+")
for x in range(n2):
    print("|", n2*' ', "|", n2*" ", "|")
print("+", n2*'-', "+", n2*"-", "+")
for x in range(n2):
    print("|", n2*' ', "|", n2*" ", "|")
print("+", n2*'-', "+", n2*"-", "+")


