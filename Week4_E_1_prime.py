'''
WEEK 4: EXTRA EXERCISE 1

Write a program that receives a positive integer and verify if it is prime. If is, print
'prime'. Otherwise, print 'not prime'.
'''

i = 0
cont = 0

n = int(input("Entry an integer: "))

if (n == 0 or n == 1):
    print("not prime")
    i = n + 1

while i <= n:
    i += 1
    if (n % i == 0):
        cont += 1
        
if cont > 2:
    print("not prime")
    
elif cont == 2:
    print("prime")
