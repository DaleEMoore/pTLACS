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


# TODO; Dale - check this out... not sure if it is working right.

# Dale has to do some research into time calculations to do the following.
# Perhaps something like this http://stackoverflow.com/questions/2788871/python-date-difference-in-minutes

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
# what time do I get home for breakfast?

leave = "6:52 am"
easy_mile_pace = "8:15 minutes"
tempo_mile = "7:12 minutes"

get_home = leave + easy_mile_pace + (3 * tempo_mile) + easy_mile_pace
print("Get home: " + str(get_home))

from datetime import datetime
import time

fmt = '%Y-%m-%d %H:%M:%S'
d1 = datetime.strptime('2010-01-01 17:31:22', fmt)
d2 = datetime.strptime('2010-01-03 20:15:14', fmt)

# convert to unix timestamp
d1_ts = time.mktime(d1.timetuple())
d2_ts = time.mktime(d2.timetuple())

# they are now in seconds, subtract and then divide by 60 to get minutes.
print (str((d2_ts - d1_ts) / 60))
# 3043  # much better

