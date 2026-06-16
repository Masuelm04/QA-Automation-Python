# Ejercicio 1: Mayor de edad

# Crea una variable:

# edad = 20

# Imprime:

# "Mayor de edad" si la edad es 18 o más.
# "Menor de edad" en caso contrario.

edad = input("Ingrese su edad: ")
edad = int(edad)

if edad >= 18:
    print("Mayor de edad.")
else:
    print("Menor de edad.")

# Ejercicio 2: Validación de Status Code

# Crea una variable:

# status_code = 200

# Imprime:

# "Prueba exitosa" si es 200.
# "Prueba fallida" si es diferente de 200.

status_code = input("Ingrese el código de estado obtenido: ")
status_code = int(status_code)

if status_code == 200:
    print("Prueba exitosa.")
else:
    print("Prueba fallida.")

# Ejercicio 3: Usuario activo

# Crea una variable:

# usuario_activo = True

# Imprime:

# "Usuario activo" si es True.
# "Usuario inactivo" si es False.

usuario_activo = input("Está el usuario activo o inactivo? False - inactivo, True - activo ")

if usuario_activo == "True":
    print("Usuario activo.")
elif usuario_activo == "False":
    print("Usuario inactivo.")
else:
    print("Error. Ha ingresado una opción inválida.")

# Nivel 2 - Uso de elif
# Ejercicio 4: Respuesta HTTP

# Crea una variable:

# status_code = 404

# Valida:

# 200 → "OK"
# 404 → "Recurso no encontrado"
# 500 → "Error interno del servidor"
# Cualquier otro → "Código desconocido"

status_code = input("Ingrese el código de estado obtenido: ")
status_code = int(status_code)

if status_code == 200:
    print("OK")
elif status_code == 404:
    print("Recurso no encontrado")
elif status_code == 500:
    print("Error interno del servidor")
else:
    print("Codigo desconocido")

# Ejercicio 5: Calificación

# Crea una variable:

# nota = 85

# Valida:

# 90 o más → "A"
# 80 a 89 → "B"
# 70 a 79 → "C"
# Menos de 70 → "Reprobado"

nota = input("Ingrese una nota: ")
nota = int(nota)

if nota >= 90:
    print("A")
elif nota >= 80 and nota < 90:
    print("B")
elif nota >= 70 and nota < 80:
    print("C")
else:
    print("Reprobado")

# Nivel 3 - Operadores lógicos
# Ejercicio 6: Login

# Crea:

# usuario = "admin"
# password = "1234"

# Imprime:

# "Login exitoso" si ambos son correctos.
# "Credenciales incorrectas" si alguno falla.

# Usa and.

usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

if usuario == "admin" and password == "1234":
    print("Login exitoso.")
else:
    print("Credenciales incorrectas.")

# Ejercicio 7: Status exitosos

# Crea:

# status_code = 201

# Considera exitosos:

# 200
# 201

# Para cualquier otro código imprime:

# Operación fallida

# Usa or.

status_code = input("Ingrese el status code obtenido: ")
status_code = int(status_code)

if status_code == 201 or status_code == 200:
    print("Operación exitosa.")
else:
    print("Operación fallida.")

# Ejercicio 8: Cuenta bloqueada

# Crea:

# cuenta_bloqueada = False

# Imprime:

# Acceso permitido

# solo si la cuenta NO está bloqueada.

# Usa not.

cuenta_bloqueada = False

if not cuenta_bloqueada:
    print("Acceso permitido.")
else:
    print("Acceso denegado.")

# Nivel 4 - QA Automation
# Ejercicio 9: Validación de API

# Crea:

# status_code = 200
# response_time = 1.2

# Reglas:

# Si el status es 200 y el tiempo es menor o igual a 2 segundos:
# "Prueba aprobada"
# Si el status es 200 pero el tiempo es mayor a 2 segundos:
# "Prueba aprobada con observaciones"
# Si el status no es 200:
# "Prueba fallida"

status_code = 200

response_time = 1.2

if status_code == 200 and response_time <= 2:
    print("Prueba aprobada.")
elif status_code == 200 and response_time > 2:
    print("Prueba aprobada con observaciones.")
elif not status_code == 200:
    print("Prueba fallida.")

# Ejercicio 10: Validación de Usuario

# Crea:

# usuario = "Antonio"
# edad = 25
# activo = True

# Permitir acceso únicamente si:

# activo es True
# edad es mayor o igual a 18

# En cualquier otro caso:

# Acceso denegado

usuario = "Antonio"

edad = input("Ingrese la edad del usuario: ")
edad = int(edad)

activo = input("Ingrese el estado del usuario: ")

if activo == "True" and edad >= 18:
    print("Acceso permitido.")
else:
    print("Accedo denegado.")

# Nivel 5 - Desafío
# Ejercicio 11: Simulador de Canje de Puntos

# (Algo parecido a los defectos que has estado trabajando)

# Variables:

# puntos = 5000
# tarjeta_activa = True

# Reglas:

# Si la tarjeta está activa y tiene 1000 puntos o más:
# "Canje permitido"
# Si la tarjeta está activa pero tiene menos de 1000 puntos:
# "Puntos insuficientes"
# Si la tarjeta está inactiva:
# "Tarjeta no disponible para canje"

puntos = input("Ingrese los puntos a canjear: ")
puntos = int(puntos)

tarjeta_activa = input("La tarjeta está activa? ")

if tarjeta_activa == "True" and puntos >= 1000:
    print("Canje permitido.")
elif tarjeta_activa == "True" and puntos < 1000:
    print("Puntos insuficientes.")
elif not tarjeta_activa == "True":
    print("Tarjeta no disponible para canje.")

# Nivel Entrevista QA Junior
# Ejercicio 12

# Sin ejecutar el código, indica qué imprimirá:

# status_code = 201

# if status_code == 200:
#     print("A")

# elif status_code == 201:
#     print("B")

# elif status_code == 404:
#     print("C")

# else:
#     print("D")

# y explica por qué.

# El código imprimirá: B

# Porque la validación indica que si el status code es 201 el cuál es el caso el valor a imprimir es B.