'''
WEEK 3: EXERCISE 5

Receive 3 integers in the input and print 'crescent' if they are given in ascending order.
Otherwise, print 'is not in ascending order'.
'''

n1 = int(input("Entry an integer: "))
n2 = int(input("Entry another integer: "))
n3 = int(input("Entry one more integer: "))

if (n1 < n2 and n1 < n3):
    print("crescent")
else:
    print("is not in ascending order")
