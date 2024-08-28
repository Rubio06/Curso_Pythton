## DICCIONARIOS
## values(): recorre los valores de un diccionario o una lista
## keys(): recorre las clavez de un diccionario
## items(): devuelve los datos tanto clave como valor
diccionario = {"2": "dos", "5": "cinco"}
diccionario_two = dict(((2, "dos"), (4, "cuatro"),(6,"cinco")))

print("--------DICCIONARIOS ----------")
for result in diccionario_two.items():
    print(result)

