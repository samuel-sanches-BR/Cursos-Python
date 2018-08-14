'''
WEEK 2: EXTRA EXERCISE 2

Write the function 'first_lex(lista)' which receives a list of strings and returns
the first string in lexicographical order. Consider the capital letters.
'''

def first_lex(lista):
    first = lista[0]
    for x in range(0, len(lista)):
        if (first > lista[x]):
            first = lista[x]

    return first
        
