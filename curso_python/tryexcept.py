# try:
#     resultado = 10 / 0
# except ZeroDivisionError:
#     print("Error: No se puede dividir por cero.")



# try:
#     numero = int("abc")
# except ValueError:
#     print("Error: No se puede convertir 'abc' en un número entero.")
    


# try:
#     resultado = 10 / 0
# except Exception as e:
#     print(f"Ocurrió un error: {e}")
    




def reciveValues(val1: int, val2: int):
    
    result: int = val1 / val2
    return result

print(reciveValues(12, 2))
