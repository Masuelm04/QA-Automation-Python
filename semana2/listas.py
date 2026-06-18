# Ejercicio 1 - Crear y recorrer una lista

# Crea una lista llamada:

# navegadores

# que contenga:

# Chrome
# Firefox
# Edge
# Safari

# Recórrela con un for e imprime cada navegador.

# Salida esperada
# Chrome
# Firefox
# Edge
# Safari

navegadores = ["Chrome", "Firefox", "Edge", "Safari"]

for navegador in navegadores:
    print(navegador)

# # Ejercicio 2 - Agregar elementos con append()

# # Crea una lista vacía:

# # status_codes = []

# # Agrega utilizando append() los siguientes códigos:

# # 200
# # 404
# # 500
# # 201

# # Luego imprime la lista completa.

# # Salida esperada
# # [200, 404, 500, 201]

status_codes = []

status_codes.append(200)
status_codes.append(404)
status_codes.append(500)
status_codes.append(201)

print(status_codes)

# Ejercicio 3 - Validar existencia con in

# Tienes la siguiente lista:

# usuarios = ["Ana", "Pedro", "Juan", "Maria"]

# Solicita un nombre mediante input().

# Valida:

# Si existe en la lista → imprimir:
# Usuario encontrado
# Si no existe → imprimir:
# Usuario no encontrado

# Utiliza el operador:

# in

usuarios  = ["Ana", "Pedro", "Juan", "Maria"]

nombre = input("Ingresa un nombre: ")

if nombre in usuarios:
    print("Usuario encontrado")
else:
    print("Usuario no encontrado")

# Ejercicio 4 - Eliminar elementos

# Tienes:

# errores = [
#     "Timeout",
#     "404",
#     "500",
#     "ConnectionError"
# ]

# Elimina el elemento:

# 404

# usando remove().

# Luego imprime la lista resultante.

# Salida esperada
# ['Timeout', '500', 'ConnectionError']

errores = ["Timeout", "404", "500", "ConnectionError"]
errores.remove("404")

print(errores)

# Ejercicio 5 - Contar respuestas exitosas

# Tienes:

# status_codes = [
#     200,
#     404,
#     200,
#     500,
#     200,
#     201,
#     200
# ]

# Utiliza:

# count()

# para mostrar cuántas veces aparece:

# 200
# Salida esperada
# Respuestas exitosas: 4

status_codes = [200, 404, 200, 500, 200, 201, 200]

print(f"Respuestas exitosas: {status_codes.count(200)}")

# Ejercicio 6 - Simulación QA API

# Tienes la siguiente respuesta simulada:

# usuarios = [
#     {"nombre": "Ana", "activo": True},
#     {"nombre": "Pedro", "activo": False},
#     {"nombre": "Juan", "activo": True},
#     {"nombre": "Maria", "activo": False}
# ]

# Recorre la lista e imprime únicamente los usuarios activos.

# Salida esperada
# Ana
# Juan

usuarios = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Pedro", "activo": False},
    {"nombre": "Juan", "activo": True},
    {"nombre": "Maria", "activo": False}
]

for usuario in usuarios:
    if usuario["activo"]:
        print(usuario['nombre'])

# Desafío adicional (nivel entrevista)

# Sin ejecutar el código, indica qué imprimirá:

# status_codes = [200, 404, 500]

# status_codes.append(201)

# status_codes.pop(1)

# print(status_codes)

# Explica paso a paso qué ocurre con la lista después de cada instrucción.

# Imprimirá [200, 404, 500]. Primero agrega el 201 a la lista con el método append, luego elimina el 201
# de la lista con el método pop, luego imprime los valores restantes de la lista