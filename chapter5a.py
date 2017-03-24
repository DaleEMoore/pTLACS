#/bin/python3

import datetime
import math
import sys
import time
import tkinter
import turtle


def draw(t, length, n):
    print("draw " + str(t) + ", " + str(length) + ", " + str(n))
    if n <= 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


def check_fermat(a, b, c, n):
    """Check Fermat's Last Theorem
    a^n + b^n = c^n
    :param a: 
    :param b: 
    :param c: 
    :param n: """
    z = math.pow(a,n) + math.pow(b,n)
    c2 = math.pow(c,n)
    if n > 2 and c2 == z:
        print ("Equal; Holy smokes, Fermat was wrong!")
    else:
        print ("Not equal; No, that doesn't work.")


def is_triangle(a, b, c):
    """Could lengths A, B and C be a triangle's 3 sides?
    :param a: 
    :param b: 
    :param c: 
    """
    print("is_triangle("+str(a)+", "+str(b)+", "+str(c)+")?")
    unhu = "Yes"
    if not a+b >= c: unhu = "No"
    if not b+c >= a: unhu = "No"
    if not a+c >= b: unhu = "No"
    print(unhu)


def recurse(n, s):
    """Given 'recurse(n, s)'; **Onanisticly** calculate n-1 and n+s.
    :param n:
    :param s:
    """
    if n <= 0:
    #if n == 0: # This might be broken... This was a BUG!
        print(s)
    else:
        try:
            recurse(n - 1, n + s)
            # RecursionError: maximum recursion depth exceeded in comparison
        except RecursionError:
            print("RecursionError: ")
            #print(str(sys.exc_info()[2]))
            #print(sys.exec_info()[2])


def main() -> object:
    """
    These are in chapter5.py because of the input needed for triangle testing.

    print("Exercise 5.1")
    # Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds,
    # plus the number of days since the epoch.
    right_now = datetime.datetime.utcnow()
    the_epoch = datetime.datetime(1970, 1, 1)
    print ("       Right now: " + str(right_now))
    print ("           Epoch: " + str(the_epoch))
    print ("Days since epoch: " + str((right_now - the_epoch).days))


    print("Exercise 5.2")
    # Check Fermat's Last Theorem
    # a^n + b^n = c^n
    check_fermat(1, 2, 3, 4)


    print ("Exercise 5.3")
    # check that 3 stick lengths are a triangle
    is_triangle(1, 2, 3)
    is_triangle(1, 2, 10)
    print("HEY YOU; Enter numbers for the following 3 items.")
    a = int(input("Length of side A:"))
    b = int(input("Length of side B:"))
    c = int(input("Length of side C:"))
    is_triangle(a, b, c)
    """

    print ("Exercise 5.4")
    #a = input("Tap ENTER to continue.")
    recurse(3,0)
    # 6

    try:
        recurse(-1,0)
        # RecursionError: maximum recursion depth exceeded in comparison
    except RecursionError:
        print("RecursionError: ")
        #print(str(sys.exc_info()[2]))
        #print(sys.exec_info()[2])

    print ("Exercise 5.5")
    #a = input("Tap ENTER to continue.")
    # Read the code, figure it out then try it here.

    root = tkinter.Tk()
    root.title("Draw!")
    cv = tkinter.Canvas(root, width=600, height=600)
    cv.pack(side=tkinter.LEFT)

    # This is how we create a turtle to draw
    # on the canvas we created above.
    t2 = turtle.RawTurtle(cv)
    screen = t2.getscreen()
    center_position = t2.position()

    #t2 = turtle.Turtle()
    draw(t2, 10, 4)

    print ("Exercise 5.6")
    a = input("Tap ENTER to continue.")
    t2.reset()
    length=10
    n2=10/3
    t2.fd(length*n2)
    t2.lt(60)
    t2.fd(length*n2)
    t2.lt(120)
    t2.fd(length*n2)
    t2.lt(60)
    t2.fd(length*n2)

    a = input("Tap ENTER to continue.")
    print ("Exercise 5.6")
    t2.reset()

    # TODO; more stuff for this section need doing!
    pass

# Python jumps right here after executing the def main() line. These two lines tell
# Python to jump to the first line of the main function above. Seems a little strange,
# but there are good reasons for this which you'll learn if you take some computer
# science.
if __name__ == "__main__":
    main()
