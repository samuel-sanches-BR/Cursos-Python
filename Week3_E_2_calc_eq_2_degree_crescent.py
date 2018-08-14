'''
WEEK 3: EXTRA EXERCISE 2

As requested in this week's video lessons, write a program that calculates the
roots of a second degree equation. The program must receive the parameters a, b,
and c of the equation ax ^ 2 + bx + c, respectively, and print the result on output
as follows: When there are no real roots print: 'this equation has no real roots'
When there is only one real root print: 'The root of this equation is X'
where X is the value of the root. When there are two real roots print:
'the roots of the equation are X and Y' where X and Y are the root values.
In addition, if there are 2 real roots, they must be printed in ascending order,
that is, X must be less than Y.
'''

import math

print("Roots of the second degree equation")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

raizdelta = b ** 2 - 4 * a * c 
    
if (raizdelta == 0):
    x = (- (b) + math.sqrt(raizdelta)) / (2 * a)
    print("the root of this equation is",x)
else:
    if (raizdelta < 0):
      print("this equation has no real roots")
    else:
      x = (- (b) + math.sqrt(raizdelta)) / (2 * a)
      y = (- (b) - math.sqrt(raizdelta)) / (2 * a)
      if (x > y):
        print("the roots of this equation are",y,"and",x)
      else:
        print("the roots of this equation are",x,"and",y)

print("End of calculation")
