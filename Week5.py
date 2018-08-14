'''
WEEK 5:

EXERCISE 1
Write the function 'busca(lista,elemento)' which searchs an element on the list
and returns the index of that. Use the Binary Search. If the element not exist
returns 'False'.
In addition, it should print each of the indexes tested by the algorithm.

EXERCISE 2
Write the function 'bubble_sort(lista)' which receives a list with integers
and returns a ordered list. Utilize Bubble Sort.
In addition, throughout processing the function should print the current
state of the list every time you make a change to its elements.

EXTRA EXERCISE 1
Write the function 'insertion_sort(lista)' which receives a list with integers
and returns an ordered list. Utilize Insertion Sort.
'''

def busca(lista, elemento):
    first = 0
    last = len(lista) - 1

    while first <= last:
        half = (first + last) // 2
        if lista[half] == elemento:
            return half
        elif elemento < lista[half]:
            last = half - 1
        else:
            first = half + 1
        print(half)

    return False
# END OF EXERCISE 1


def bubble_sort(lista):
    end = len(lista)
    first = False

    for i in range(end - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                if first:
                    print(lista)
                lista[j], lista[j + 1] = lista[j+1], lista[j]
                first = True
    return lista
# END OF EXERCISE 2


def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        k = i
        while k > 0 and key < lista[k - 1]:
            lista[k] = lista[k - 1]
            k -= 1
        lista[k] = key
    return lista
# END OF EXTRA EXERCISE 1

