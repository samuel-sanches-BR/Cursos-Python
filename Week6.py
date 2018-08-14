'''
WEEK 6:

EXERCISE 1
Write the function 'soma_lista(lista)' which receives a list of integers
and returns the number corresponding the sum of the elements. Use recursion.

EXERCISE 2
Write the function 'encontra_impares(lista)' which receives a list of integers
and returns another list only with the odd elements. Use recursion.

EXERCISE 3
Este exercício tem duas partes:

Implemente a função 'incomodam(n)' que devolve uma string contendo "incomodam "
(a palavra seguida de um espaço) n vezes. Se n não for um inteiro estritamente
positivo, a função deve devolver uma string vazia. Essa função deve ser implementada
utilizando recursão.

Utilizando a função acima, implemente a função elefantes(n) que devolve uma string
contendo a letra da música "Um elefante incomoda muita gente" de 1 até n elefantes.
Se n não for maior que 1, a função deve devolver uma string vazia. Essa função
também deve ser implementada utilizando recursão.
Observe que, para um elefante, você deve escrever por extenso e no singular
("Um elefante..."); para os demais, utilize números e o plural ("2 elefantes...").

elefantes(4):

Um elefante incomoda muita gente
2 elefantes incomodam incomodam muito mais
2 elefantes incomodam muita gente
3 elefantes incomodam incomodam incomodam muito mais
3 elefantes incomodam muita gente
4 elefantes incomodam incomodam incomodam incomodam muito mais


EXTRA EXERCISE 1
Wirte the funcion 'fibonacci(n)' which receives an integer and returns
the n element of Fibonacci sequence. Use recursion.

EXTRA EXERCISE 2
wirte the function 'fatorial(x)' which receives an integer and returns
the factorial of x. Use recursion.
'''

def soma_lista(lista):
    if len(lista) == 0 :
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])
# END OF EXERCISE 1


def encontra_impares(lista, lista2=[]):
    if len(lista) == 0:
        return lista2
    else:
        if lista[0] % 2 == 1:
            lista2 = lista2.append(lista[0])
            return encontra_impares(lista[1:])
        else:
            return encontra_impares(lista[1:])
# END OF EXERCISE 2


def incomodam(n):
    if type(n) != int or n <= 0:
        return ''
    else:
        if n == 1:
            return 'incomodam '
        else:
            return 'incomodam ' + incomodam(n - 1)

def elefantes(n, first = True):
    if n < 0:
        return ''
    elif n == 1:
        return 'Um elefante incomoda muita gente\n'
    elif first:
        return elefantes(n - 1, False) \
               + str(n) + ' elefantes ' + incomodam(n) + 'muito mais'
    else:
        return elefantes(n - 1, False) \
              + str(n) + ' elefantes ' + incomodam (n) + 'muito mais\n' \
              + str(n) + ' elefantes ' + incomodam (n) + 'muita gente\n'
# END OF EXERCISE 3

            
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# END OF EXTRA EXERCISE 1


def fatorial(x):
    if x < 1:
        return 1
    else:
        return x * fatorial(x - 1)
# END OF EXTRA EXERCISE 2
