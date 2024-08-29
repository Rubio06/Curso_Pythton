##LISTAS 
lista_one = ["enoc","carlos","roberto","alberto", "carlos", "Arnaldo","Caemo", "Celso", "Ernesto", "men"]
print("---como se recorre tradicionalmente una lista---")
for valor in lista_one:
    print(valor)

# range(start, stop, step)
#len(): devuelve el numero de elementos o la dimensión de la lista
print("--- recorriendo con range, len ---")
for i in range(len(lista_one)):
    print(lista_one[i])

#la funcion enumerate() itera sobre una secuencia, lista, tuplas, dicionarios
print("--- utilizando la funcion enumarate ---")
for indice, valor in enumerate(lista_one, 8):
    print(f'Índice: {indice}, Valor: {valor}')


print("--- Uniendo estructuras de datos con zip() ---")
lista_dos = [1, 2, 3, 4, 5]
lista_tree = [5, 26, 55, 87, 44]
for valor_one, valor_two, valor_treee in zip(lista_one, lista_dos, lista_tree):
    print(f'[{valor_one}] - [{valor_two}] - [{valor_treee}]')
    
    
print("--- Utilizando el reserved()---")
for valor in reversed(lista_one):
    print(valor)


print("--- La funcion fiter(bool, iterable) sirve para filtrar y mostrar elementos  ---")
for valor in filter(lambda x: x.startswith('c'), lista_one):
    print(valor)




# for i in range(-len(lista_one), 0):
#     print(lista_one[i])


# for i in range(0, len(lista_one), 2):
#     print(lista_one[i])


# for valor in lista_one[:]:  # Usamos una copia con [:] para evitar modificar la lista durante la iteración
#     if valor == "carlos":
#         lista_one.remove(valor)
# print(lista_one)

# i = 0
# while i < len(lista_one):
#     print(lista_one[i])
#     i += 1


# [print(valor) for valor in lista_one]


# iterador = iter(lista_one)
# while True:
#     try:
#         valor = next(iterador)
#         print(valor)
#     except StopIteration:
#         break



