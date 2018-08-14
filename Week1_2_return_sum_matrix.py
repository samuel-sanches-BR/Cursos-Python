'''
WEEK 1: EXERCISE 1

Write the function 'sum_matrix(m1, m2)' which receives two matrix and returns
the sum of them, if the dimension are equals. Otherwise, return 'False'.
'''

def sum_matrix(m1,m2):
    if (len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
        l = 0
        c = 0
        mSumTot = []
        while (l <= (len(m1) - 1)):
            mSumLin = []
            while (c <= (len(m1[0]) - 1)):
                x = m1[l][c] + m2[l][c]
                mSumLin.append(x)
                c += 1
            mSumTot.append(mSumLin)
            l += 1
            c = 0
    else:
        mSumTot = False
    return mSumTot
