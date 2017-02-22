#/bin/python3

import polygon

print("Exercise 4.1")
# download http://greenteapress.com/thinkpython2/code/polygon.py

bob = 3
radius = 2
# TODO; I don't have this setup correctly. Perhaps I should re-read chapter 4. I'm getting the error:
"""
Traceback (most recent call last):
  File "/home/dalem/PycharmProjects/pTLACS/exercise4.py", line 12, in <module>
    polygon.circle(bob, radius)
  File "/home/dalem/PycharmProjects/pTLACS/polygon.py", line 79, in circle
    arc(t, r, 360)
  File "/home/dalem/PycharmProjects/pTLACS/polygon.py", line 68, in arc
    t.lt(step_angle/2)
AttributeError: 'int' object has no attribute 'lt'
"""
polygon.circle(bob, radius)

