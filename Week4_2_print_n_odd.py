'''
WEEK 4: EXERCISE 2

Receive a positive integer and prints the 'n' firsts odd numbers.
'''

n = int(input("Entry the integer n: "))
m = 0
counter = 0

while (counter != n):
    if m % 2 != 0:
        print(m)
        counter =  + 1
    m = m + 1
