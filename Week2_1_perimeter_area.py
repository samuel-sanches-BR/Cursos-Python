'''
WEEK 2: EXERCISE 1

Make a program in Python that receives (data entry) the corresponding value corresponding
to the side of a square, calculate and print (data output) its perimeter and its area.

OBS.: the output must be: "perimeter: x - area: y"

Example - Data entry: "Entry the value corresponding to the side of a square: 3"
          Data output: "perimeter: 12 - area: 9"
'''

x = float(input("Entry the value corresponding to the side of a square: "))
perimeter = x*4
area = x**2
print("perimeter:", perimeter, "-", "area:",area)
