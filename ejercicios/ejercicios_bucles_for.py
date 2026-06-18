# EJERCICIOS DE PRACTICA DEL BUCLE FOR

# Ejercicio 1 - Recorrer una lista de usuarios

# Crea una lista con 5 nombres de usuarios.

# Usa un bucle for para imprimir cada nombre.

# Ejemplo de salida
# Ana
# Pedro
# Juan
# Maria
# Carlos

usuarios = ["Ana", "Pedro", "Juan", "Maria", "Carlos"]

for usuario in usuarios:
    print(usuario)

# Ejercicio 2 - Imprimir números del 1 al 10

# Utiliza range() y un bucle for para imprimir los números del 1 al 10.

# Salida esperada
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

for i in range(1, 11):
    print(i)

# Ejercicio 3 - Mostrar solo números pares

# Utiliza un bucle for para recorrer los números del 1 al 20.

# Imprime únicamente los números pares.

# Salida esperada
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

for i in range(2, 21, 2):
    print(i)

# Ejercicio 4 - Simulación de validación de Status Codes

# Crea la siguiente lista:

# status_codes = [200, 404, 500, 201, 403]

# Recórrela con un for.

# Para cada código:

# 200 → imprimir "OK"
# 201 → imprimir "Creado"
# 404 → imprimir "No encontrado"
# 500 → imprimir "Error interno"
# Cualquier otro → imprimir "Código no manejado"

status_codes = [200, 404, 500, 201, 403]

for status_code in status_codes:
    if status_code == 200:
        print("OK")
    elif status_code == 201:
        print("Creado")
    elif status_code == 404:
        print("No encontrado")
    elif status_code == 500:
        print("Error interno")
    else:
        print("Código no manejado")

# Ejercicio 5 - Contar usuarios activos

# Crea la siguiente lista:

# usuarios_activos = [True, False, True, True, False]

# Usa un for para contar cuántos usuarios activos existen.

# Salida esperada
# Usuarios activos: 3

# Pista: necesitarás una variable contador.

usuarios_activos = [True, False, True, True, False]
contador = 0

for usuario_activo in usuarios_activos:
    if usuario_activo == True:
        contador += 1

print(f"Usuarios activos: {contador}")

# Ejercicio 6 - Validación de tiempos de respuesta

# Crea esta lista:

# response_times = [1.2, 2.5, 0.8, 3.1, 1.9]

# Recórrela con un for.

# Para cada tiempo:

# Si es menor o igual a 2 segundos:
# imprimir "Performance OK"
# Si es mayor a 2 segundos:
# imprimir "Performance lenta"

response_times = [1.2, 2.5, 0.8, 3.1, 1.9]

for response_time in response_times:
    if response_time <= 2:
        print("Performance OK")
    else:
        print("Performance lenta")

# Ejercicio 7 - Mini Caso QA Automation

# Imagina que una API devuelve la siguiente lista de usuarios:

# usuarios = [
#     {"nombre": "Ana", "activo": True},
#     {"nombre": "Pedro", "activo": False},
#     {"nombre": "Juan", "activo": True},
#     {"nombre": "Maria", "activo": False}
# ]

# Recorre la lista y muestra:

# Ana - Activo
# Pedro - Inactivo
# Juan - Activo
# Maria - Inactivo

usuarios = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Pedro", "activo": False},
    {"nombre": "Juan", "activo": True},
    {"nombre": "Maria", "activo": False}
]

for usuario in usuarios:
    if usuario["activo"] == True:
        print(f"{usuario["nombre"]} - Activo")
    else:
        print(f"{usuario["nombre"]} - Inactivo")

# Desafío adicional (nivel entrevista)

# Sin ejecutar el código, indica qué imprimirá:

# for numero in range(1, 6):

#     if numero == 4:
#         break

#     print(numero)

# El bloque de codigo anterior imprime hasta el número 3, luego termina el bucle for debido a la sentencia break

usuarios = ["Carlos", "Ana", "Carmelina", "Patricia"]

print(f"Existen un total de {len(usuarios)} usuarios.")