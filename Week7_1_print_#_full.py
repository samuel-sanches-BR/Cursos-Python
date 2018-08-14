'''
WEEK 7: EXERCISE 1

Write a program that receives in entry two integers corresponding to width and height
of a rectangle. The program must prints the characters '#' to form the rectangle.
'''

width_inp = int(input("entry the width: "))
height_inp = int(input("entry the height: "))

height = height_inp
width = width_inp

while (height_inp > 0):
    while (width_inp > 0):
        print("#", end = "")
        width_inp -= 1
    print()
    width_inp = width
    height_inp -= 1
