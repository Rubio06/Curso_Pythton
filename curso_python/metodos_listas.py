## METODOS DE LAS LISTAS

# Agrega un elemento al final de la lista.
lista = [1, 2, 3]
lista.append(4)
print(lista)  # [1, 2, 3, 4]

# Extiende la lista agregando todos los elementos de un iterable (como otra lista).
lista = [1, 2, 3]
lista.extend([4, 5])
print(lista)  # [1, 2, 3, 4, 5]

#Inserta un elemento en una posición específica. i es el índice en el que se insertará x.
lista = [1, 2, 4]
lista.insert(2, 3)
print(lista)  # [1, 2, 3, 4]

#Elimina la primera ocurrencia del valor x de la lista. Si x no está en la lista, se produce un error ValueError.
lista = [1, 2, 3, 2, 4]
lista.remove(2)
print(lista)  # [1, 3, 2, 4]

# Elimina y devuelve el elemento en la posición i. Si no se especifica i, elimina y devuelve el último elemento.
lista = [1, 2, 3]
elemento = lista.pop(1)
print(elemento)  # 2
print(lista)    # [1, 3]


#Elimina todos los elementos de la lista, dejándola vacía.
lista = [1, 2, 3]
lista.clear()
print(lista)  # []

# Devuelve el índice de la primera ocurrencia de x en la lista. Puedes especificar un rango con start y end
lista = [1, 2, 3, 2, 4]
indice = lista.index(2)
print(indice)  # 1


lista = [1, 2, 2, 3, 2]
conteo = lista.count(2)
print(conteo)  # 3



lista = [3, 1, 4, 2]
lista.sort()
print(lista)  # [1, 2, 3, 4]


lista = [1, 2, 3]
lista.reverse()
print(lista)  # [3, 2, 1]


lista = [1, 2, 3]
lista_copia = lista.copy()
print(lista_copia)  # [1, 2, 3]


lista = [x**2 for x in range(5)]
print(lista)  # [0, 1, 4, 9, 16]



