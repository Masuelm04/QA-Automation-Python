# Ejercicio 1 - Crear y acceder a un diccionario

# Crea el siguiente diccionario:

# usuario = {
#     "nombre": "Antonio",
#     "edad": 25,
#     "activo": True
# }

# Imprime:

# Antonio
# 25
# True

# Accediendo a cada valor mediante su clave.

usuario = {
    "nombre": "Antonio",
    "edad": 25,
    "activo": True
}

print(usuario['nombre'])
print(usuario['edad'])
print(usuario['activo'])

# Ejercicio 2 - Modificar valores

# Partiendo de:

# usuario = {
#     "nombre": "Antonio",
#     "edad": 25,
#     "activo": True
# }

# Modifica:

# edad → 26
# activo → False

# Luego imprime el diccionario completo.

usuario = {
    "nombre": "Antonio",
    "edad": 25,
    "activo": True
}

usuario["edad"] = 26
usuario["activo"] = False

print(usuario)

# Ejercicio 3 - Agregar nuevas claves

# Partiendo de:

# usuario = {
#     "nombre": "Antonio",
#     "edad": 25
# }

# Agrega:

# "correo": "antonio@test.com"
# "pais": "República Dominicana"

# Imprime el diccionario resultante.

usuario = {
    "nombre": "Antonio",
    "edad": 25
}

usuario["correo"] = "antonio@test.com"
usuario["pais"] = "República Dominicana"

print(usuario)

# Ejercicio 4 - Validar existencia de claves

# Tienes:

# usuario = {
#     "nombre": "Antonio",
#     "edad": 25
# }

# Valida:

# Si existe la clave "nombre" imprimir:
# La clave nombre existe.
# Si no existe la clave "telefono" imprimir:
# La clave telefono no existe.

# Utiliza:

# in

usuario = {
    "nombre": "Antonio",
    "edad": 25
}

if "nombre" in usuario:
    print("La clave nombre existe.")

if not "telefono" in usuario:
    print("La clave telefono no existe.")

# Ejercicio 5 - Uso de get()

# Tienes:

# usuario = {
#     "nombre": "Antonio"
# }

# Imprime:

# usuario.get("nombre")
# usuario.get("edad")
# usuario.get("correo", "No disponible")

# Observa qué devuelve cada caso.

# Luego explica con tus palabras por qué get() es más seguro que usar:

# usuario["correo"]

usuario = {
    "nombre": "Antonio"
}

print(usuario.get("nombre"))
print(usuario.get("edad"))
print(usuario.get("correo", "No disponible"))

# get() es más seguro que usar usuario["correo"] porque la segunda opción puede dar error si no se existe la key mencionada,
# en cambio el get da como
# resultado None, o un texto que podemos modificar en caso de que no exista la key específicada

# Ejercicio 6 - Recorrer un diccionario

# Tienes:

# usuario = {
#     "nombre": "Antonio",
#     "edad": 25,
#     "activo": True
# }

# Utiliza:

# items()

# para mostrar:

# nombre: Antonio
# edad: 25
# activo: True

usuario = {
    "nombre": "Antonio",
    "edad": 25,
    "activo": True
}

for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Ejercicio 7 - Simulación de respuesta API

# Tienes:

# response = {
#     "status_code": 200,
#     "response_time": 1.25,
#     "success": True
# }

# Valida:

# Si status_code es 200 imprimir:
# Status OK
# Si response_time es menor o igual a 2 imprimir:
# Performance OK
# Si success es True imprimir:
# Prueba exitosa

response = {
    "status_code": 200,
    "response_time": 1.25,
    "success": True
}

if response["status_code"] == 200:
    print("Status OK")

if response["response_time"] <= 2:
    print("Performance OK")

if response["success"]:
    print("Prueba exitosa")

# Ejercicio 8 - Lista de diccionarios (Muy importante)

# Tienes:

# usuarios = [
#     {
#         "nombre": "Ana",
#         "activo": True
#     },
#     {
#         "nombre": "Pedro",
#         "activo": False
#     },
#     {
#         "nombre": "Juan",
#         "activo": True
#     },
#     {
#         "nombre": "Maria",
#         "activo": False
#     }
# ]

# Recorre la lista e imprime únicamente:

# Ana
# Juan

# Es decir, solo los usuarios activos.

usuarios = [
    {
        "nombre": "Ana",
        "activo": True
    },
    {
        "nombre": "Pedro",
        "activo": False
    },
    {
        "nombre": "Juan",
        "activo": True
    },
    {
        "nombre": "Maria",
        "activo": False
    }
]

for usuario in usuarios:
    if usuario["activo"]:
        print(usuario["nombre"])

# Desafío QA Automation (Nivel entrevista)

# Sin ejecutar el código, indica qué imprimirá:

# response = {
#     "status": "success",
#     "data": {
#         "usuario": "Antonio",
#         "activo": True
#     }
# }

# print(response["data"]["usuario"])

# Imprimirá: Antonio

# Pregunta adicional

# ¿Qué diferencia habría entre:

# response["data"]["correo"]

# y

# response["data"].get("correo")

# ?

# Ambos buscan la key Correo anidada a la key data del diccionario response,
# si la key no existe, el primero da error y el segundo devolverá None