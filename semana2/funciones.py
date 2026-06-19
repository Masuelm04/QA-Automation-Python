# Ejercicio 1 - Primera función

# Crea una función llamada:

# saludar()

# que imprima:

# Bienvenido a QA Automation

# Luego llama la función.

def saludar():
    print("Bienvenido a QA Automation")

saludar()

# Ejercicio 2 - Función con un parámetro

# Crea una función:

# saludar_usuario(nombre)

# que reciba un nombre e imprima:

# Hola Antonio

# (reemplazando Antonio por el nombre recibido).

# Prueba la función con al menos 3 nombres distintos.

def saludar_usuario(nombre):
    print(f"Hola {nombre}")

saludar_usuario("Marcos")
saludar_usuario("Masuel")
saludar_usuario("Maria")

# Ejercicio 3 - Función con múltiples parámetros

# Crea una función:

# mostrar_usuario(nombre, edad)

# que imprima:

# Nombre: Antonio
# Edad: 25

# Prueba la función con diferentes valores.

def mostrar_usuario(nombre, edad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")

mostrar_usuario("Carlos", 50)
mostrar_usuario("Ramona", 60)
mostrar_usuario("Mariana", 22)

# Ejercicio 4 - Uso de return

# Crea una función:

# sumar(a, b)

# que retorne la suma de ambos números.

# Guarda el resultado en una variable e imprímelo.

# Ejemplo
# resultado = sumar(10, 5)
# print(resultado)

# Salida:

# 15

def sumar(a, b):
    return a + b

suma = sumar(10, 5)
print(suma)

# Ejercicio 5 - Retornar un booleano

# Crea una función:

# es_mayor_de_edad(edad)

# que retorne:

# True

# si la edad es 18 o más.

# y

# False

# en caso contrario.

# Prueba con varias edades.

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
    
print(es_mayor_de_edad(20))
print(es_mayor_de_edad(5))
print(es_mayor_de_edad(17))
print(es_mayor_de_edad(18))

# Ejercicio 6 - Validación de Status Code (QA)

# Crea una función:

# validar_status_code(status_code)

# Reglas:

# Si el código es 200 → retornar True
# Si no → retornar False

# Luego utiliza:

# if validar_status_code(200):
#     print("Prueba aprobada")

def validad_status_code(status_code):
    if status_code == 200:
        return True
    else:
        return False
    
if validad_status_code(200):
    print("Prueba aprobada")

print(validad_status_code(200))
print(validad_status_code(404))

# Ejercicio 7 - Función que recibe una lista

# Tienes:

# usuarios = ["Ana", "Pedro", "Juan", "Maria"]

# Crea una función:

# mostrar_usuarios(lista_usuarios)

# que recorra la lista e imprima cada usuario.

usuarios = ["Ana", "Pedro", "Juan", "Maria"]

def mostrar_usuario(lista_usuarios):
    for usuario in lista_usuarios:
        print(usuario)

mostrar_usuario(usuarios)

# Ejercicio 8 - Función que recibe un diccionario

# Tienes:

# usuario = {
#     "nombre": "Antonio",
#     "edad": 25,
#     "activo": True
# }

# Crea una función:

# mostrar_datos_usuario(usuario)

# que imprima:

# Nombre: Antonio
# Edad: 25
# Activo: True

usuario = {
    "nombre": "Antonio",
    "edad": 25,
    "activo": True
}

def mostrar_datos_usuario(usuario):
        print(f"Nombre: {usuario['nombre']}")
        print(f"Edad: {usuario['edad']}")
        print(f"Activo: {usuario['activo']}")

mostrar_datos_usuario(usuario)

# Ejercicio 9 - Simulación QA API

# Tienes:

# response = {
#     "status_code": 200,
#     "response_time": 1.5
# }

# Crea una función:

# validar_api(response)

# Reglas:

# Si status_code es 200 y response_time <= 2:
# Prueba aprobada
# Si status_code es 200 y response_time > 2:
# Prueba aprobada con observaciones
# Si el status es diferente de 200:
# Prueba fallida

response = {
    "status_code": 200,
    "response_time": 1.5
}

def validar_api(response):
    if response['status_code'] == 200 and response['response_time'] <= 2:
        return "Prueba aprobada"
    elif response['status_code'] == 200 and response['response_time'] > 2:
        return "Prueba aprobada con observaciones"
    else:
        return "Prueba fallida"
    
print(validar_api(response))

# Ejercicio 10 - Lista de diccionarios (Nivel QA Junior)

# Tienes:

# usuarios = [
#     {"nombre": "Ana", "activo": True},
#     {"nombre": "Pedro", "activo": False},
#     {"nombre": "Juan", "activo": True},
#     {"nombre": "Maria", "activo": False}
# ]

# Crea una función:

# mostrar_usuarios_activos(usuarios)

# que imprima únicamente:

# Ana
# Juan

usuarios = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Pedro", "activo": False},
    {"nombre": "Juan", "activo": True},
    {"nombre": "Maria", "activo": False}
]

def mostrar_usuarios_activo(usuarios):
    for usuario in usuarios:
        if usuario['activo']:
            print(usuario['nombre'])
        
mostrar_usuarios_activo(usuarios)

# Desafío de entrevista QA

# Sin ejecutar el código, indica qué imprimirá:

# def obtener_status():
#     return 200

# resultado = obtener_status()

# print(resultado)

# Este imprimirá el valor 200

# Y ahora este:

# def obtener_status():
#     print(200)

# resultado = obtener_status()

# print(resultado)

# Este imprimirá el valor 200 y None

# Pregunta

# ¿Por qué las salidas son diferentes?

# Porque en el segundo la función termina y al no tener un return retorna automáticamente None y es lo que imprimirá