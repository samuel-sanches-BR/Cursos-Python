'''
WEEK 1: EXTRA EXERCISE 1

As proposal on the video lesson, write the function 'print_matrix(matrix)',
which receives a matrix and prints, line by line
'''

def print_matrix(matrix):
    l = 0
    c = 0
    while (l <= (len(matrix) - 1)):
        while (c <= (len(matrix[0]) - 1)):
            if (c == (len(matrix[0]) - 1)):
                print(matrix[l][c], end='')
                c += 1
            else:
                print(matrix[l][c], end=' ')
                c += 1
        print('')
        l += 1
        c = 0
    
    return 
