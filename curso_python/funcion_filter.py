# Ejemplo con una lista de números
# numeros = [1, 2, 3, 4, 5, 6]

# # Filtramos los números pares
# pares = filter(lambda x: x % 2 == 0, numeros)

# # Convertimos el resultado a una lista para ver los elementos filtrados
# print(list(pares))  # Salida: [2, 4, 6]

# array = ["Enoc", "Carlos", "Roberto", "Alberto", "Carlos"]
# array_minusculas = [elemento.lower() for elemento in array]
# print(array_minusculas)  # ['enoc', 'carlos', 'roberto', 'alberto', 'carlos']

# array = ["Enoc", "Carlos", "Roberto", "Alberto", "Carlos"]
# array_minusculas = list(map(str.lower, array))
# print(array_minusculas)  # ['enoc', 'carlos', 'roberto', 'alberto', 'carlos']




# def convert_data(value):
#     array = []
#     for i in range(value):
#         add_value = input(f"Ingrese el valor {i + 1} del arreglo: ")
#         array.append(add_value)
        
#     convert_mayus = list(map(str.lower, array))
    
#     for x in convert_mayus:
#         if convert_mayus[x].startswith('c') == True:
#             covert = convert_mayus[x]
#     return covert

# print("El valor es: ", convert_data(int(input("¿Ingrese la dimension del array?: "))))

def convert_data(value, letter):
    array = []
    
    for i in range(value):
        add_value = input(f"Ingrese el valor {i + 1} del arreglo: ")
        array.append(add_value)
        
    convert_mayus = list(map(str.lower, array))    
    result = [item for item in convert_mayus if item.startswith(letter)]    
    return result


value_input = input("Ingrese la cantidad de valores a ingresar: ")
try:
    value_int = int(value_input)
except ValueError:
    print("El valor ingresado no es un entero válido.")
    exit(1)

letter = input("Ingrese una sola letra: ")
if len(letter) == 1 and letter.isalpha():
    print(convert_data(value_int, letter))
else:
    print("La letra ingresada no cumple con los requisitos.")
    exit(1)

    

