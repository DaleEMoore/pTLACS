#/bin/python3

# TODO; there are more exercises in section 4.3 page 31.
# TODO; A 2 monitor system gets the previous centered on the 2 monitor break; move it.

import math
import polygon
import tkinter
import turtle

def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

def pass_bob(t,length):
    bob = t
    square(bob,length)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)
    #polygon(t,r,60)

def main():
    print("Exercise 4.1")
    # Here is the first line of the main function's code.
    root = tkinter.Tk()
    root.title("Draw!")
    cv = tkinter.Canvas(root, width=600, height=600)
    cv.pack(side=tkinter.LEFT)

    # This is how we create a turtle to draw
    # on the canvas we created above.
    t = turtle.RawTurtle(cv)
    screen = t.getscreen()
    center_position = t.position()

    t.penup(); t.setposition(0,100); t.pendown()
    t.write("Exercise 4.3.1a", font=("Arial", 16, "normal"))
    t.penup(); t.setposition(center_position); t.pendown()
    square(t,100)
    reply = input("Tap ENTER to continue...")
    t.reset()
    t.penup(); t.setposition(0,100); t.pendown()
    t.write("Exercise 4.3.1b", font=("Arial", 16, "normal"))
    t.penup(); t.setposition(center_position); t.pendown()
    pass_bob(t,20)
    reply = input("Tap ENTER to continue...")
    t.reset()
    t.penup(); t.setposition(-250,100); t.pendown()
    t.write("Exercise 4.3.2 already done in Exercise 4.3.1a and b.", font=("Arial", 16, "normal"))
    t.penup(); t.setposition(center_position); t.pendown()
    reply = input("Tap ENTER to continue...")
    t.reset()
    t.penup(); t.setposition(0,200); t.pendown()
    t.write("Exercise 4.3.3.", font=("Arial", 16, "normal"))
    t.penup(); t.setposition(center_position); t.pendown()
    polygon(t,5,100)
    reply = input("Tap ENTER to continue...")
    t.reset()
    t.penup(); t.setposition(0,200); t.pendown()
    t.write("Exercise 4.3.4 then 5.", font=("Arial", 16, "normal"))
    t.penup(); t.setposition(center_position); t.pendown()
    circle(t,100)
    reply = input("Tap ENTER to continue...")



    #t.done()
    #turtle.done()
    """
    # With the lines below, the "turtle" will look like a pencil.
    screen.register_shape("pencil.gif")
    t.shape("pencil.gif")

    # This sets the lower left corner to 0,0 and the upper right corner to 600,600.
    screen.setworldcoordinates(0, 0, 600, 600)
    screen.bgcolor("white")

    # A frame is an invisible widget that holds other widgets. This frame goes
    # on the right hand side of the window and holds the buttons and Entry widgets.
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

    pointLabel = tkinter.Label(frame, text="Width")
    pointLabel.pack()

    # This entry widget allows the user to pick a width for their lines.
    # With the pointSize variable below you can write pointSize.get() to to
    # the contents of the entry widget and pointSize.set(val) to set the value
    # of the entry widget to val. Initially the pointSize is set to 1. str(1) is needed because
    # the entry widget must be given a string.
    pointSize = tkinter.StringVar()
    pointEntry = tkinter.Entry(frame, textvariable=pointSize)
    pointEntry.pack()
    pointSize.set(str(1))

    # This is an event handler. Handling the quit button press results in destroying the window
    # and quitting the application.
    def quitHandler():
        root.destroy()
        root.quit()

        # This is how a button is created in the frame. The quitHandler is the event handler for button

    # presses of the "Quit" button.
    quitButton = tkinter.Button(frame, text="Quit", command=quitHandler)
    quitButton.pack()

    # Here is another event handler. This one handles mouse clicks on the screen.
    def clickHandler(x, y):
        # When a mouse click occurs, get the pointSize entry value and set the width of the
        # turtle called "t" to the pointSize value. The int(pointSize.get()) is needed because
        # the width is an integer, but the entry widget stores it as a string.
        t.width(int(pointSize.get()))
        t.goto(x, y)

    # Here is how we tie the clickHandler to mouse clicks.
    screen.onclick(clickHandler)

    # Finally, this code is last. It tells the application to enter its event processing loop
    # so the application will respond to events.
    tkinter.mainloop()

    #print("Exercise 4.1")
    ## download http://greenteapress.com/thinkpython2/code/polygon.py
    ## http://web.cecs.pdx.edu/~lmd/cs161/turtle-excerpt.htm (not everything works with Dale's version of turtle.
    ## https://docs.python.org/3/library/turtle.html#module-turtle

    #bob = turtle.Turtle()

    ## bob.reset()
    ## bob.screen.setworldcoordinates(100,100,250,207.5)
    ## bob.screen.setworldcoordinates(-50,-7.5,50,7.5)
    ## for _ in range(72):
    ##     left(10)
    ## for _ in range(8):
    ##     left(45); fd(2)   # a regular octagon
    ## reply = input("Tap ENTER to continue...")

    ## bob.reset()
    #bob.penup()
    ## bob.setx(100)
    ## bob.sety(100)
    #radius = 20
    #bob.pendown()
    #polygon.circle(bob, radius)
    #reply = input("Tap ENTER to continue...")
    """

# Python jumps right here after executing the def main() line. These two lines tell
# Python to jump to the first line of the main function above. Seems a little strange,
# but there are good reasons for this which you'll learn if you take some computer
# science.
if __name__ == "__main__":
    main()
