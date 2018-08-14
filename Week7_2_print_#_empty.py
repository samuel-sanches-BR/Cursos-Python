'''
WEEK 7: EXERCISE 2

Rewrite exercise 1 by printing the unfilled rectangles so that the characters
that are not on the edge of the rectangle are spaces.
'''

width_inp = int(input("entry the width: "))
height_inp = int(input("entry the height: "))

height = height_inp
width = width_inp

while (height_inp > 0):
    while (width_inp > 0):
        if (height_inp == height or height_inp == 1):
            print("#", end = "")
        elif (height_inp != height or height_inp != 1):
            if (width_inp == width or width_inp == 1):
                print("#", end = "")
            else:
                print(" ", end = "")
        width_inp -= 1            
    print()
    width_inp = width
    height_inp -= 1
