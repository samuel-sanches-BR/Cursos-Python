'''
WEEK 1: EXTRA EXERCISE 2

Write the function 'are_multipl(m1, m2)' which receives two matrix and returns
'True' if they can be multiplied (in the given order) or 'False' if not.
'''

def are_multipl(m1,m2):
    if (len(m1[0]) == len(m2)):
        return True
    else:
        return False
