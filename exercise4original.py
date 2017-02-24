#/bin/python3

# TODO; there are more exercises in section 4.3 page 31.
# TODO; A 2 monitor system gets the previous centered on the 2 monitor break; move it.

import polygon
import turtle

print("Exercise 4.1")
# download http://greenteapress.com/thinkpython2/code/polygon.py
# http://web.cecs.pdx.edu/~lmd/cs161/turtle-excerpt.htm (not everything works with Dale's version of turtle.
# https://docs.python.org/3/library/turtle.html#module-turtle

bob = turtle.Turtle()

#bob.reset()
#bob.screen.setworldcoordinates(100,100,250,207.5)
#bob.screen.setworldcoordinates(-50,-7.5,50,7.5)
#for _ in range(72):
#     left(10)
#for _ in range(8):
#     left(45); fd(2)   # a regular octagon
#reply = input("Tap ENTER to continue...")

#bob.reset()
bob.penup()
#bob.setx(100)
#bob.sety(100)
radius = 20
bob.pendown()
polygon.circle(bob, radius)
reply = input("Tap ENTER to continue...")
