'''
WEEK 8: EXERCISE 2

Write the function 'sum_elements' that receives as a parameter a list with integers
and returns an integer corresponding to the sum of the elements of the list received.
'''

def sum_elements(list1):
    sume = 0
    for x in list1:
        sume += x
    return sume
