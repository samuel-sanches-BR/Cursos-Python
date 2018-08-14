'''
WEEK 3:

EXERCISE 1
Define the class 'Triangle' which the constructor receives 3 integers
corresponding the 'a', 'b' and 'c' sides of a triangle. With the method
'perimeter()' which returns an integer corresponding the triangle's perimeter.

EXERCISE 2
Write the method 'side_type()' that returns a string saying if the triangle is
'isosceles' or 'equilateral' or 'scalene'

EXTRA EXERCISE 1
Write the method 'right()' that returns 'True' if the is a right triangle or 'False' if not.

EXTRA EXERCISE 2
Write the method 'similar(triangle)' which receives a Triangle object and verify
if the actual triangle is similar to the last triangle passed as a parameter. If yes
returns 'True', otherwise 'False'.
'''

class Triangle:
    
    def __init__(self, sideA, sideB, sideC):
        self.a = sideA
        self.b = sideB
        self.c = sideC

    def perimeter(self):
        return self.a + self.b + self.c

# END OF EXERCISE 1


    def side_type(self):
        if (self.a != self.b and self.a != self.c and self.b != self.c):
            return 'scalene'
        elif (self.a == self.b and self.a == self.c):
            return 'equilateral'
        else:
            return 'isosceles'

# END OF EXERCISE 2


    def right(self):
        if (self.a ** 2 == self.b ** 2 + self.c ** 2 or
            self.b ** 2 == self.a ** 2 + self.c ** 2 or
            self.c ** 2 == self.b ** 2 + self.a ** 2):
            return True
        else:
            return False

# END OF EXTRA EXERCISE 1


    def similar(self, triangle):
        if (self.a / triangle.a == self.b / triangle.b and
            self.a / triangle.a == self.c / triangle.c):
            return True
        else:
            return False
        
# END OF EXTRA EXERCISE 2
