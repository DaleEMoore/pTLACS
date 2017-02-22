#/bin/python3

# Exercise 2.1
n = 1
# SyntaxError: can't assign to literal
#42 = n

x = y = 1
print (x, y)
# printed "1 1"

n = 1;

n = 1. # Not an error, the value "1.0"
# SyntaxError: invalid syntax
#a = n.

x = 2
y = 4
# NameError: name 'xy' is not defined
#print(xy)
print(x*y) # 8


# Exercise 2.2
radius = 5
volume_of_a_sphere = (4/3) * 3.1415926 * (radius ^ 3)
print("Volume of a sphere: " + str(volume_of_a_sphere))
# Volume of a sphere: 25.132740799999997

cover_price = 24.95
discount_rate = .40
discount = cover_price * discount_rate
unit_cost = cover_price - discount
first_shipping_cost = 3
rest_shipping_cost = .75
copies = 60
total_shipping = first_shipping_cost + ((copies - 1) * rest_shipping_cost)
total_cost = copies * unit_cost
print("Cost: " + str(total_cost) + ", Shipping: " + str(total_shipping) + ", Total: " + str(total_shipping + total_cost))
# Cost: 898.1999999999999, Shipping: 47.25, Total: 945.4499999999999


# Do some research into time calculations to do the following.
# Perhaps something like this http://stackoverflow.com/questions/2788871/python-date-difference-in-minutes
# Well... it turned out to be lots more research to tune up the date math.

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
# what time do I get home for breakfast?

import datetime
import time

year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day
leave_time = datetime.datetime(year, month, day, 6, 52, 4)
print("Leave time: " + str(leave_time))
# Leave time: 2017-02-22 06:52:04

minimum_time = datetime.datetime(year, month, day, 0, 0, 0)
eazy_mile_pace_time = datetime.datetime(year, month, day,0,8,15)
eazy_mile_pace_delta = eazy_mile_pace_time - minimum_time

tempo_time = datetime.datetime(year, month, day,0,7,12)
tempo_delta = tempo_time - minimum_time

get_home = leave_time + eazy_mile_pace_delta + (tempo_delta + tempo_delta + tempo_delta) + eazy_mile_pace_delta
print("Get home: " + str(get_home))
# Get home: 2017-02-22 07:30:10
