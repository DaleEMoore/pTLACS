#/bin/python3
# 2nd Edition, Version 2.2.20

# 1.9 Exercises
# Exercise 1.1
print("Hello, world!")

# NameError: name 'pirnt' is not defined
#pirnt("Hello, world!")

# Exercise 1.1 1
# SyntaxError: Missing parentheses in call to 'print'
#print "Hello, world!"

# Exercise 1.1 2
# SyntaxError: EOL while scanning string literal
#print ("Hello, world!)

# Exercise 1.1 3
i2 = 2++2
print(i2)
# prints 4.

# Exercise 1.1 4
# SyntaxError: invalid token
#i2 = 02

# Exercise 1.1 5
# SyntaxError: invalid syntax
#i2 = 2 2

# Exercise 1.2

# 1.2 1
# How many seconds in 42 minutes and 42 seconds?
i2 = 42*60 + 42
print("Seconds: " + str(i2))

# 1.2 2
# How many miles in 10 kilometers at 1.61 kilometers per mile?
KMpM = 1.61
i2 = 10 / KMpM
print("Miles: " + str(i2))

# 1.2 3
# If you run a 10 kilometer race in 42 minutes and 42 seconds,
raceSeconds = 42*60 + 42
print("Race seconds: " + str(raceSeconds))
seconds_per_kilometer = raceSeconds / 10
print("Seconds per KM: " + str(seconds_per_kilometer))
seconds_per_mile = seconds_per_kilometer * KMpM
print("Seconds per mile: " + str(seconds_per_mile))
m, s = divmod(seconds_per_mile, 60) # pull out the minutes
h, m = divmod(m, 60)                # pull out the hours
d, h = divmod(h, 24)                # pull out the days
minutes_and_seconds_per_mile=str(m) + ":" + str(s)
#minutes_and_seconds_per_mile="Days: " + str(d) + ", Hours: " + str(h) + ", Minutes: " + str(m) + ", Seconds: " + str(s)
print("Average pace (minutes and seconds per mile): " + str(minutes_and_seconds_per_mile))
# 2562 seconds / 1 mile; x miles per 1 hour
seconds_per_hour = 60*60 # 3600
average_miles_per_hour=seconds_per_hour / raceSeconds
print("Average speed in miles per hour: " + str(average_miles_per_hour))



# what is your average pace (time per mile in minutes and seconds)?
# What is your average speed in miles per hour?
