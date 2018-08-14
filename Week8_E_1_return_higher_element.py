'''
WEEK 8: EXTRA EXERCISE 1

Write the function 'major_element' that receives as a parameter a list with integers
and returns an integer corresponding to the highest value present in the list received.
'''

def major_element(list1):
    list1.sort()
    list1.reverse()
    return list1[0]
