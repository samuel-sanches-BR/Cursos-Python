'''
WEEK 3: EXTRA EXERCISE 1

Receive 4 numbers in the entry, one at a time. The first two must respectively
correspond to the x and y coordinates of a point in a Cartesian plane.
The last two must correspond, respectively, to the x and y coordinates of another
point in the same plane. Calculate the distance between the two points.
If the distance is greater than or equal to 10, print 'far' in the output. Otherwise,
when the distance is less than 10, print 'close'.
'''

from math import sqrt

x = float(input("Entry the x-coordinate: "))
y = float(input("Entry the y-coordinate: "))
x1 = float(input("Entry another x-coordinate: "))
y1 = float(input("Entry another y-coordinate: "))

distance = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)

if (distance >= 10):
    print("far")
else:
    print("close")
