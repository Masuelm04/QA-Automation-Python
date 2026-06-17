# Ejercicios para practicar enumerate()
# Ejercicio 4 - Numerar usuarios

# Tienes:

# usuarios = ["Ana", "Pedro", "Juan", "Maria"]

# Usa enumerate() para mostrar:

# Usuario #1: Ana
# Usuario #2: Pedro
# Usuario #3: Juan
# Usuario #4: Maria

# Pista: Usa start=1.

usuarios = ["Ana", "Pedro", "Juan", "Maria"]

for numero, usuario in enumerate(usuarios, start=1):
    print(f"Usuario #{numero}: {usuario}")

# Ejercicio 5 - Validación de Status Codes

# Tienes:

# status_codes = [200, 404, 500, 201]

# Usa enumerate() para imprimir:

# Prueba 1: 200
# Prueba 2: 404
# Prueba 3: 500
# Prueba 4: 201

status_codes = [200, 404, 500, 201]

for numero, status_code in enumerate(status_codes, start=1):
    print(f"Prueba {numero}: {status_code}")

# Ejercicio 6 - Simulación de ejecución de casos de prueba

# Tienes:

# casos_prueba = [
#     "Login",
#     "Registro",
#     "Canje de puntos",
#     "Consulta de balance"
# ]

# Usa enumerate() para mostrar:

# Ejecutando caso #1: Login
# Ejecutando caso #2: Registro
# Ejecutando caso #3: Canje de puntos
# Ejecutando caso #4: Consulta de balance

casos_prueba = [
    "Login",
    "Registro",
    "Canje de puntos",
    "Consulta de balance"
]

for numero, caso_prueba in enumerate(casos_prueba, start=1):
    print(f"Ejecutando caso #{numero}: {caso_prueba}")

# Desafío adicional (mezclando len() y enumerate())

# Tienes:

# usuarios = ["Ana", "Pedro", "Juan", "Maria"]

# Debes:

# Imprimir la cantidad total de usuarios usando len().
# Luego recorrerlos usando enumerate(start=1).
# Mostrar:
# Total de usuarios: 4

# Usuario #1: Ana
# Usuario #2: Pedro
# Usuario #3: Juan
# Usuario #4: Maria

usuarios = ["Ana", "Pedro", "Juan", "Maria"]

print(f"Total de usuarios: {len(usuarios)}")

for numero, usuario in enumerate(usuarios, start=1):
    print(f"Usuario #{numero}: {usuario}")