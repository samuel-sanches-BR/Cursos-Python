'''
WEEK 1: EXERCISE 1

Write the function 'dimension(matrix)' which receives a matrix and prints
their dimension, iXj.
'''

def dimension(matrix):
    col = len(matrix)
    lin = len(matrix[0])
    return print(col,"X",lin,sep='')
