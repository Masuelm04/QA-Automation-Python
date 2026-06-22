# Ejercicio 1 - Capturar ValueError

# Solicita al usuario una edad utilizando input().

# Convierte el valor a entero usando int().

# Si el usuario introduce un texto en lugar de un número:

# Debe ingresar una edad válida

# Utiliza:

# try
# except ValueError

try:
    edad = int(input("Ingrese una edad: "))
except ValueError:
    print("Debe ingresar una edad válida")

# Ejercicio 2 - División segura

# Solicita dos números al usuario.

# Realiza una división:

# numero1 / numero2

# Si el segundo número es cero:

# No se puede dividir entre cero

# Utiliza:

# ZeroDivisionError

try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    division = numero1 / numero2
except ZeroDivisionError:
    print("No se puede dividir entre cero")

# Ejercicio 3 - Múltiples excepciones

# Solicita:

# Un número
# Un divisor

# Valida:

# Si el número no es válido → mostrar un mensaje apropiado.
# Si el divisor es cero → mostrar un mensaje apropiado.

# Debes utilizar:

# except ValueError
# except ZeroDivisionError

try:
    numero = int(input("Ingrese un número: "))
    divisor = int(input("Ingrese un divisor: "))

    cociente = numero / divisor
except ValueError:
    input("Debe ingresar un número válido")
except ZeroDivisionError:
    print("No se puede dividir entre cero")

# Ejercicio 4 - Uso de else

# Solicita una edad.

# Si la conversión a entero es exitosa:

# Edad registrada correctamente

# Utiliza:

# else

# para imprimir el mensaje.

try:
    edad = int(input("Ingrese una edad: "))
except ValueError:
    print("Debe ingresar una edad válida")
else:
    print("Edad registrada correctamente")

# Ejercicio 5 - Uso de finally

# Solicita un número.

# Intenta convertirlo a entero.

# Independientemente de si ocurre error o no, imprime:

# Fin de la validación

# Utiliza:

# finally

try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("Debe ingresar un número válido")
finally:
    print("Fin de la validación")

# Ejercicio 6 - Capturar mensaje de error

# Solicita un número.

# Si ocurre un error al convertirlo:

# Imprime el mensaje real de la excepción.

# Ejemplo:

# invalid literal for int() with base 10: 'hola'

# Utiliza:

# except ValueError as error

try:
    numero = int(input("Ingrese un número: "))
except ValueError as error:
    print(error)

# Ejercicio 7 - Manejo de KeyError

# Tienes el siguiente diccionario:

# usuario = {
#     "nombre": "Antonio",
#     "edad": 25
# }

# Intenta acceder a:

# usuario["correo"]

# Como la clave no existe, captura el error e imprime:

# La clave solicitada no existe

# Utiliza:

# KeyError

usuario = {
    "nombre": "Antonio",
    "edad": 25
}

try:
    print(usuario["correo"])
except KeyError:
    print("La clave solicitada no existe")

# Ejercicio 8 - Manejo de IndexError

# Tienes:

# usuarios = ["Ana", "Pedro", "Juan"]

# Intenta imprimir:

# usuarios[5]

# Captura el error e imprime:

# Índice fuera de rango

# Utiliza:

# IndexError

usuarios = ["Ana", "Pedro", "Juan"]

try:
    print(usuarios[5])
except IndexError:
    print("Índice fuera de rango")

# Ejercicio 9 - Simulación QA API

# Tienes:

# response = {
#     "status_code": 200
# }

# Intenta acceder a:

# response["response_time"]

# Si la clave no existe:

# La respuesta de la API no contiene response_time

# Utiliza manejo de excepciones.

# Este es un caso extremadamente común en automatización de APIs.

response = {
    "status_code": 200
}

try:
    print(response["response_time"])
except KeyError:
    print("La respuesta de la API no contiene response_time")

# Ejercicio 10 - Crear y lanzar una excepción personalizada

# Crea una función:

# validar_edad(edad)

# Reglas:

# Si la edad es menor de 18:
# raise ValueError("Edad no permitida")
# Si la edad es 18 o más:
# Acceso permitido

# Luego llama la función dentro de un bloque:

# try
# except

# y captura el error.

def validar_edad(edad):
    if edad < 18:
        raise ValueError("Edad no permitida")
    else:
        (print("Acceso permitido"))

try:
    validar_edad(15)
except ValueError as error:
    print(error)

# Desafío de entrevista QA Junior

# Sin ejecutar el código:

# try:
#     print("Inicio")

#     numero = int("abc")

#     print("Fin try")

# except ValueError:
#     print("Error capturado")

# finally:
#     print("Finally")
# Preguntas
# ¿Qué imprime?
#   Inicio
#   Error capturado
#   Finally

# ¿Por qué no se ejecuta "Fin try"?
#   Porque se lanza la excepción antes de la intrucción que está predestinada a ejecutar print("Fin try"), por lo tanto
# este bloque de código no llega a ejecutarse 

# Desafío de entrevista QA Automation

# Sin ejecutar:

# usuario = {
#     "nombre": "Antonio"
# }

# try:
#     print(usuario["correo"])

# except KeyError:
#     print("Clave no encontrada")

# else:
#     print("Todo correcto")

# finally:
#     print("Proceso finalizado")
# Preguntas
# ¿Qué imprime?
#   Clave no encontrada
#   Proceso finalizado
# ¿Se ejecuta el bloque else?
#   No
# ¿Por qué?
#   Se llegaría a ejecutar si la instrucción dentro del bloque try fuese correcta y no lanzara una excepción