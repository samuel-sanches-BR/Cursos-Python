'''
WEEK 7: EXTRA EXERCISE 1

Write the function 'n_prime' that receives an integer greater than or equal to 2
as a parameter and returns the number of prime numbers that exist between 2 and 'n'
(including 2 and, if appropriate, n).
'''

def isPrime(n):

    if (n == 0 or n == 1):
        return False

    i = 1
    cont = 0
    while i <= n:
        if (n % i == 0):
            cont += 1
        i += 1
        
    if cont > 2:
        return False
    
    elif cont == 2:
        return True

##########################################

def n_prime(x):

    qtd = 0
    
    while (x > 0):
        
        if (isPrime(x)):
            qtd += 1

        x -= 1

    return qtd

##########################################

x = int(input("Entry an integer: "))

while (x >= 0):
    print(n_prime(x))
    x = int(input("Entry an integer: "))
