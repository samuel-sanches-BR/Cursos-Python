'''
WEEK 4: EXTRA EXERCISE 2

Write a program that receives an integer and verify if the receive number have at least one
igual adjacent. If exists, print 'yes', if not, print 'no'.
'''

numEntry = int(input("Entry an integer: "))

former = numEntry % 10
n = numEntry // 10
aDigit = True

while n > 0 or aDigit:
    current = n % 10
    
    if (n == 0):
        print("no")
        aDigit = False
        
    if (current == former and numEntry != 0):
        print("yes")
        aDigit = False
        n = 0

    n = n // 10    
    former = current
    
