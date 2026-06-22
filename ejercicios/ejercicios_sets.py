# Ejercicio 5 - Eliminar duplicados

# Tienes:

# usuarios = [
#     "Ana",
#     "Pedro",
#     "Ana",
#     "Juan",
#     "Pedro",
#     "Maria"
# ]

# Convierte la lista a un Set.

# Imprime el resultado.

# Pregunta:

# ¿Cuántos usuarios únicos quedaron?

# Utiliza:

# set()
# len()

usuarios = [
    "Ana",
    "Pedro",
    "Ana",
    "Juan",
    "Pedro",
    "Maria"
]

usuarios = set(usuarios)
print(f"Quedaron {len(usuarios)} usuarios únicos")

# Ejercicio 6 - Agregar roles

# Crea un Set:

# roles = {"admin", "user"}

# Agrega:

# tester

# mediante:

# add()

# Luego imprime el Set.

roles = {"admin", "user"}
roles.add("tester")

print(roles)

# Ejercicio 7 - Validar permisos

# Tienes:

# roles = {
#     "admin",
#     "user",
#     "tester"
# }

# Solicita un rol mediante input().

# Valida:

# Si existe → "Rol encontrado"
# Si no existe → "Rol no encontrado"

# Utiliza:

# in

roles = {
    "admin",
    "user",
    "tester"
}

rol = input("Ingrese un rol: ")

if rol in roles:
    print("Rol encontrado")
else:
    print("Rol no encontrado")

# Ejercicio 8 - Eliminar rol

# Tienes:

# roles = {
#     "admin",
#     "user",
#     "tester"
# }

# Elimina:

# user

# utilizando:

# remove()

# Luego imprime el Set resultante.

roles = {
    "admin",
    "user",
    "tester"
}

roles.remove("user")

print(roles)

# Ejercicio 9 - Usuarios comunes entre sistemas

# Imagina que dos APIs devuelven:

# api_1 = {
#     "Ana",
#     "Pedro",
#     "Juan"
# }
# api_2 = {
#     "Pedro",
#     "Juan",
#     "Maria"
# }

# Obtén los usuarios que aparecen en ambas APIs.

# Utiliza:

# &

# Salida esperada:

# {'Pedro', 'Juan'}

api_1 = {
    "Ana",
    "Pedro",
    "Juan"
}
api_2 = {
    "Pedro",
    "Juan",
    "Maria"
}

usuarios = api_1 & api_2

print(usuarios)

# Ejercicio 10 - Usuarios únicos entre sistemas

# Utilizando los mismos Sets:

# api_1 = {
#     "Ana",
#     "Pedro",
#     "Juan"
# }
# api_2 = {
#     "Pedro",
#     "Juan",
#     "Maria"
# }

# Obtén todos los usuarios sin duplicados.

# Utiliza:

# |

# Salida esperada:

# {
#     'Ana',
#     'Pedro',
#     'Juan',
#     'Maria'
# }

api_1 = {
    "Ana",
    "Pedro",
    "Juan"
}
api_2 = {
    "Pedro",
    "Juan",
    "Maria"
}

usuarios = api_1 | api_2

print(usuarios)

# Sin ejecutar:

# roles = {
#     "admin",
#     "user",
#     "tester",
#     "admin"
# }

# print(len(roles))
# Preguntas
# ¿Qué imprime?
#   Imprime 3
# ¿Por qué el resultado no es 4?
#   Porque imprime la cantidad de elementos existentes sin duplicados