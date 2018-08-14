'''
WEEK 5: EXTRA EXERCISE 2

Rewrite the function 'max' from the other exercise, now the function receives 3
integers and returns the higher.
'''

def max(a, b, c):
    
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c
