
# print("========== EXERCIE 1 =========")
# ## Escribe un programa que recorra los números del 1 al 50 e imprima si cada número es par o impar.

# inicio: int = int(input("Ingrese el rango de inicio: "))
# final: int = int(input("Ingrese el final del numero: "))

# for value in range(inicio, final,1):
#     if value % 2:
#         print(f"{value} es impar")
#     else:
#         print(f"{value} es par")


# print("========== EXERCIE 2 =========")

# ## Crea una lista de números y escribe un programa que calcule la suma de todos los números en la lista.

# def sumar(a, b, c):
#     return a + b + c

# numeros = [1, 2, 3]
# resultado = sumar(*numeros)  # Desempaqueta la lista en los argumentos de la función
# print(resultado)  # Output: 6

# def num_list(tamano_lista):
#     lista = []
#     suma_total = 0

#     for valor in range(tamano_lista):
#         valores = int(input(f"Inrese el valor {valor + 1} de la lista: "))
#         lista.append(valores)
#         suma_total += valores
    
#     return suma_total

# print("La suma total de los valores es:", num_list(int(input("Ingrese la dimensión de la lista: "))))


# Escribe un programa que imprima la tabla de multiplicar del 1 al 10 para un número ingresado por el usuario.


# print("========== EXERCIE 3 =========")
# valor = int(input("Ingrese un valor a multiplicar: "))

# for i in range(10):
#     print(f"{i} * {valor} = { i * valor }")
    

# Verificar que valor de un array es par o impart

lista_par_impart = [38, 22,12,17,25,22]

for i in range(len(lista_par_impart)):
    if lista_par_impart[i] % 2:
        print(f"{lista_par_impart[i]} impart")
    else:
        print(f"{lista_par_impart[i]} par")




