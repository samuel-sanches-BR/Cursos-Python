'''
WEEK 5: EXERCISE 2

Write the function 'high_prime' which receives an integer higher or equal to 2 and
returns the higher prime number less or equal to the number that the function receive.
'''

def high_prime(n):

    if (n >= 2):
        cont = 0
        i = 1
        test = 2
        while (test >= 2 and test <= n):
            while (i <= test):
                if (test % i == 0):
                    cont += 1
                i += 1
            if (cont == 2):
                prime = test
            test += 1
            i = 1
            cont = 0
        return prime
           

    else:
        print("n tem que ser > ou = a 2")
