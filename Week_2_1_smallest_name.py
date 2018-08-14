'''
WEEK 2: EXERCISE 2

Write the function 'smallest(names)' which receives a list of strings
with names and returns the smallest.
'''

def smallest(names):
    lista_Strip=[]
    tamCada = []
    for x in range(0, len(names)):
        lista_Strip.append(names[x].strip().capitalize())
    for x in range(0, len(lista_Strip)):
        tamCada.append(len(lista_Strip[x]))
    return lista_Strip[tamCada.index(min(tamCada))]
        

