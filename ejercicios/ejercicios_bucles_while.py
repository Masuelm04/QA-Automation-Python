# Ejercicio 1 - Contador del 1 al 10

# Utiliza un bucle while para imprimir los números del 1 al 10.

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

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

while True:
    if contador >= 11:
        break

    print(contador)
    contador += 1

# Ejercicio 2 - Cuenta regresiva

# Utiliza un bucle while para imprimir los números del 10 al 1.

# Al finalizar, imprime:

# Despegue!
# Salida esperada
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Despegue!

cuenta_regresiva = 10

while cuenta_regresiva >= 0:
    print(cuenta_regresiva)

    if cuenta_regresiva <= 1:
        print("Despegue!")
        break

    cuenta_regresiva -= 1

# Ejercicio 3 - Validación de contraseña

# Solicita al usuario una contraseña.

# Mientras la contraseña sea diferente de:

# admin123

# debe seguir solicitándola.

# Cuando sea correcta, mostrar:

# Acceso concedido.

password = ""

while password != "admin123":
    password = input("Ingrese una contraseña: ")

print("Acceso concedido.")

# Ejercicio 4 - Menú interactivo (while True)

# Crea un programa que muestre continuamente:

# 1. Consultar saldo
# 2. Transferir fondos
# 3. Salir

# Si el usuario selecciona:

# 3

# debe salir utilizando break.

# Antes de salir debe imprimir:

# Gracias por utilizar el sistema.

while True:
    print("Seleccione una de las siguientes opciones del menú:")
    print("1. Consultar saldo")
    print("2. Transferir fondos")
    print("3. Salir")

    opcion = input("Opción: ")

    if opcion == "3":
        print("Gracias por utilizar el sistema.")
        break

# Ejercicio 5 - Sumar números

# Solicita al usuario 5 números utilizando un while.

# Al final muestra la suma total.

# Ejemplo

# Entrada:

# 5
# 10
# 15
# 20
# 25

# Salida:

# La suma es: 75

contador = 1
total = 0

while True:
    numero = input(f"Ingrese el número #{contador} a sumar: ")
    numero = int(numero)

    total += numero
    contador += 1
    
    if contador == 6:
        print(f"La suma es: {total}")
        break

# Ejercicio 6 - Ignorar números negativos (continue)

# Solicita 5 números al usuario.

# Si el número es negativo:

# Ignóralo usando continue.
# No debe sumarse al total.

# Al final muestra la suma de los números válidos.

contador = 0
total = 0

while contador <= 4:
    numero = input("Ingrese un número a sumar: ")
    numero = int(numero)

    if numero < 0:
        contador += 1
        continue
    
    total += numero

print(f"El total de la suma es de: {total}")

# Ejercicio 7 - Validación de Status Codes

# Tienes:

# status_codes = [200, 404, 500, 201, 403]

# Recórrela utilizando un while.

# Imprime:

# "OK" para 200
# "Creado" para 201
# "No encontrado" para 404
# "Error interno" para 500
# "Código no manejado" para cualquier otro

# ⚠️ No uses for.

status_codes = [200, 404, 500, 201, 403]
contador = len(status_codes)
indice = 0

while contador >= 1:
    if status_codes[indice] == 200:
        print("OK")
    elif status_codes[indice] == 201:
        print("Creado")
    elif status_codes[indice] == 404:
        print("No encontrado")
    elif status_codes[indice] == 500:
        print("Error interno")
    else:
        print("Codigo no manejado")
    
    contador -= 1
    indice += 1

# Ejercicio 8 - Buscar un usuario (break)

# Tienes:

# usuarios = ["Ana", "Pedro", "Juan", "Maria"]

# Solicita al usuario un nombre.

# Recorre la lista usando while.

# Si encuentras el nombre:

# Usuario encontrado.

# y termina inmediatamente usando break.

# Si termina el recorrido sin encontrarlo:

# Usuario no encontrado.

usuarios = ["Ana", "Pedro", "Juan", "Maria"]
contador = len(usuarios)
indice = 0
usuario = input("Ingresa un nombre: ")

while contador >= 1:
    if usuario == usuarios[indice]:
        print("Usuario encontrado.")
        break

    if contador == 1:
        print("Usuario no encontrado.")
    contador -= 1
    indice += 1

# Ejercicio 9 - Simulación de reintentos QA

# Imagina que una API falla varias veces antes de responder correctamente.

# Variables iniciales:

# status_code = 500
# intentos = 0

# Usa un while para simular hasta 3 intentos.

# En cada intento imprime:

# Intento #1
# Intento #2
# Intento #3

# Cuando llegue al tercer intento, cambia:

# status_code = 200

status_code = 500
intentos = 0

while intentos <= 3:
    intentos += 1

    if intentos == 3:
        status_code = 200
        print(f"Intento #{intentos}: status code {status_code}")
        print("Prueba exitosa.")
        break

    print(f"Intento #{intentos}: status code {status_code}")

# Ejercicio 10 - Desafío QA Automation

# Tienes:

# usuarios = [
#     {"nombre": "Ana", "activo": True},
#     {"nombre": "Pedro", "activo": False},
#     {"nombre": "Juan", "activo": True},
#     {"nombre": "Maria", "activo": False},
#     {"nombre": "Carlos", "activo": True}
# ]

# Recórrela utilizando while.

# Reglas:

# Si el usuario está inactivo, usar continue.
# Si está activo, imprimir:
# Validando usuario: Ana

# (reemplazando por el nombre correspondiente).

# Salida esperada
# Validando usuario: Ana
# Validando usuario: Juan
# Validando usuario: Carlos

usuarios = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Pedro", "activo": False},
    {"nombre": "Juan", "activo": True},
    {"nombre": "Maria", "activo": False},
    {"nombre": "Carlos", "activo": True}
]

contador = len(usuarios)
indice = 0

while contador >= 1:
    usuario = usuarios[indice]

    if usuario["activo"] == False:
        contador -= 1
        indice += 1
        continue

    print(f"Validando usuario: {usuario['nombre']}")

    contador -= 1
    indice += 1

# Desafío de razonamiento (nivel entrevista)

# Sin ejecutar el código, indica qué imprimirá:

# contador = 1

# while contador <= 5:

#     if contador == 3:
#         contador += 1
#         continue

#     print(contador)

#     contador += 1

# Explica paso a paso qué ocurre en cada iteración.

# El ejercicio anterior imprimirá los números del 1 al 5, omitiendo el número 3