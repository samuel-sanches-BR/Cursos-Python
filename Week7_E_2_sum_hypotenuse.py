'''
WEEK 7: EXTRA EXERCISE 2

Write a function 'sum_hypotenuse' that receives as a parameter a positive integer 'n'
and return the sum of all integers between 1 and 'n' that are the length of the
hypotenuse of some triangle rectangle with integer legs.
'''

def sum_hypotenuse(n):

    leg1 = 1
    leg2 = 1
    hypo = n
    sumh = 0
    hypoTest = 0

    while (hypo >= 1):

        while (leg1 <= hypo):

            while (leg2 <= hypo):

                if (hypo ** 2 == leg1 ** 2 + leg2 ** 2):
                    if (hypoTest != hypo):
                        sumh += hypo
                        hypoTest = hypo
                    
                leg2 += 1
            
            leg1 += 1
            leg2 = 1
            
        hypo -= 1
        leg1 = 1

    return sumh
