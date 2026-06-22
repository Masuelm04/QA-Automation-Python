# Ejercicio 1 - Ambientes de prueba

# Crea una tupla llamada:

# ambientes = ("QA", "UAT", "PROD")

# Imprime:

# QA
# UAT
# PROD

# utilizando un for.

ambientes = ("QA", "UAT", "PROD")

for ambiente in ambientes:
    print(ambiente)

# Ejercicio 2 - Status exitosos

# Crea una tupla:

# status_exitosos = (200, 201, 204)

# Solicita un status code mediante input().

# Valida:

# Si existe en la tupla → "Status exitoso"
# Si no existe → "Status no exitoso"

# Utiliza:

# in

status_exitosos = (200, 201, 204)

status = int(input("Ingrese un status para validar: "))

if status in status_exitosos:
    print("Status exitoso")
else:
    print("Status no exitoso")

# Ejercicio 3 - Contar respuestas exitosas

# Tienes:

# status_codes = (200, 404, 200, 500, 200, 201)

# Utiliza:

# count()

# para mostrar cuántas veces aparece:

# 200

# Salida esperada:

# Cantidad de respuestas exitosas: 3

status_codes = (200, 404, 200, 500, 200, 201)

print(f"Cantidad de respuestas exitosas: {status_codes.count(200)}")

# Ejercicio 4 - Buscar posición

# Tienes:

# navegadores = (
#     "Chrome",
#     "Firefox",
#     "Edge",
#     "Safari"
# )

# Utiliza:

# index()

# para mostrar la posición de:

# Edge

navegadores = (
    "Chrome",
    "Firefox",
    "Edge",
    "Safari"
)

print(f"La posición de Edge es: {navegadores.index('Edge')}")

# Sin ejecutar:

# status_codes = (
#     200,
#     404,
#     500
# )

# print(status_codes[1])
# Preguntas
# ¿Qué imprime?
#   Imprime 404
# ¿Por qué?
#   Porque es el elemento que se encuentra en la segunda posición, recordando que a la primera posición se accede con [0]