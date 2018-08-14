'''
WEEK 4:

EXERCISE 1
Write the function 'ordenada(lista)' which receives a list with integers and returns
'True' if the list is ordered or 'False' if not.

EXERCISE 2
Write the function 'busca(lista, elemento)' that searchs an element and returns
the index corresponding to that, if the element does not exist return 'False'.

EXTRA EXERCISE 1
Write the function 'lista_grande(n)' which receives an integer 'n' and returns
a list with n random integers.

EXTRA EXERCISE 2
wirte the function 'ordenada(lista)' which receives a list with integers and
returns the list ordered. Use the Selection Sort.
'''

def ordenada(lista):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                return False
    return True
# END OF EXERCISE 1


def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False
# END OF EXERCISE 2


def lista_grande(n):
    import random
    l = []
    for i in range(n):
        l.append(random.randrange(9999))
    return l
# END OF EXTRA EXERCISE 1


def ordena(lista):
    fim = len(lista)
    for i in range(fim -1):
        minimo = i
        for j in range(i + 1, fim):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista
# END OF EXTRA EXERCISE 2
 
        
