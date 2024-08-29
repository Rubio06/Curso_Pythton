## METODOS DE CADENA


## capitalize(): Convierte el primer carácter de la cadena a mayúscula.
"hello".capitalize()  # 'Hello'

## casefold(): Convierte la cadena a minúsculas, más agresivamente que lower().
"HELLO".casefold()  # 'hello'

## center(width[, fillchar]): Centra la cadena en un campo de longitud width, llenando con fillchar (por defecto, espacios).
"hello".center(10, '-')  # '--hello---'


## count(sub[, start[, end]]): Devuelve el número de ocurrencias de sub en la cadena, opcionalmente restringido por los índices start y end.
"hello world".count("o")  # 2


## endswith(suffix[, start[, end]]): Devuelve True si la cadena termina con el sufijo suffix.
"hello".endswith("lo")  # True


## find(sub[, start[, end]]): Devuelve el índice más bajo en el que se encuentra sub. Devuelve -1 si no se encuentra.
"hello".find("e")  # 1


## format(*args, **kwargs): Formatea la cadena usando los argumentos posicionales y de palabra clave.
"Hello, {}!".format("world")  # 'Hello, world!'


## index(sub[, start[, end]]): Como find(), pero lanza una excepción ValueError si sub no se encuentra.
"hello".index("e")  # 1


## isalnum(): Devuelve True si todos los caracteres de la cadena son alfanuméricos
"hello123".isalnum()  # True




## isalpha(): Devuelve True si todos los caracteres de la cadena son letras.
"hello".isalpha()  # True


## isdigit(): Devuelve True si todos los caracteres de la cadena son dígitos.
"123".isdigit()  # True


## islower(): Devuelve True si todos los caracteres están en minúsculas.
"hello".islower()  # True


## isspace(): Devuelve True si todos los caracteres de la cadena son espacios en blanco.
"   ".isspace()  # True

## istitle(): Devuelve True si la cadena está en formato de título (primera letra en mayúscula).
"Hello World".istitle()  # True


# isupper(): Devuelve True si todos los caracteres están en mayúsculas.
hello_2 = "Hdd"
"HELLO".isupper()  # True

print("El dato está en mayúscula") if hello_2.isupper() else print("El dato está en minúscula")




##join(iterable): Une los elementos de iterable con la cadena como delimitador.
"-".join(["hello", "world"])  # 'hello-world'


## lower(): Convierte todos los caracteres de la cadena a minúsculas.
"HELLO".lower()  # 'hello'


## lstrip([chars]): Elimina los caracteres a la izquierda de la cadena (por defecto, espacios).
"   hello".lstrip()  # 'hello'


## replace(old, new[, count]): Reemplaza las ocurrencias de old por new. Opcionalmente, se puede limitar el número de reemplazos con count.
"hello world".replace("world", "Python")  # 'hello Python'


## split(sep=None, maxsplit=-1): Divide la cadena en una lista de subcadenas usando sep como delimitador.
"hello world".split()  # ['hello', 'world']


## splitlines([keepends]): Divide la cadena en una lista de líneas, manteniendo los caracteres de fin de línea si keepends es True.
"hello\nworld".splitlines()  # ['hello', 'world']


## startswith(prefix[, start[, end]]): Devuelve True si la cadena comienza con el prefijo prefix.
"hello".startswith("he")  # True


## strip([chars]): Elimina los caracteres a ambos lados de la cadena (por defecto, espacios).
"   hello   ".strip()  # 'hello'


## swapcase(): Cambia las mayúsculas a minúsculas y viceversa.
"Hello".swapcase()  # 'hELLO'


## title(): Convierte la primera letra de cada palabra a mayúscula.
"hello world".title()  # 'Hello World'


## upper(): Convierte todos los caracteres de la cadena a mayúsculas.
"hello".upper()  # 'HELLO'


## zfill(width): Rellena la cadena con ceros a la izquierda para que tenga una longitud de width.
"42".zfill(5)  # '00042'











