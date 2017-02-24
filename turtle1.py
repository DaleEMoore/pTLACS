#/bin/python3

# https://michael0x2a.com/blog/turtle-examples

# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: Create a new turtle. We'll call it "bob"
bob = turtle.Turtle()
# How do I position and scale the tkinter.Canvas that turtle draws on?
#bob.screen.setworldcoordinates(-150,-7.5,150,7.5) # From: https://docs.python.org/3.1/library/turtle.html#turtle.setworldcoordinates


# Step 3: Move in the direction Bob's facing for 50 pixels
bob.forward(50)

# Step 4: We're done!
turtle.done() # pauses until you "X" the program.