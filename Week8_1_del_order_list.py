'''
WEEK 8: EXERCISE 1

Write the function 'remove_repetitions' that receives as a parameter a list with
integers, check if such a list has repeated elements and remove them. The function
should return a list corresponding to the first list, without repeated elements.
The returned list must be sorted.
'''

def remove_repetitions(list1):
    list1.sort()
    for x in list1:
        while (list1.count(x) > 1):
            list1.remove(x)
    return list1
