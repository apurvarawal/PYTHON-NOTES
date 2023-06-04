import random  # random is a STL

import math

import datetime

import calendar

import os  # gives access to operating system files, and files can be added or deleted using this STL

courses = ['hindi', 'english', 'maths', 'physics', 'biology', 'chem']

random_course = random.choice(courses)

print(random_course)

rads = math.radians(90)   # converts degree to randians

print(rads)

print(math.sin(rads))     # gives sine of an angle

today = datetime.date.today()    # gives today's date
print(today)

leap = calendar.isleap(2023)     # checks if a year is a leap year
print(leap)

print(os.getcwd())               # prints the location of the folder

print(os.__file__)               # prints the location of the file
