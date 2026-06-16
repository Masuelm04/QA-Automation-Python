# 🎯 Objetivo
# Simular datos típicos que un QA Automation usaría en pruebas (usuarios, APIs y validaciones).

# 🧩 Parte 1 - Declaración de variables

# Declara las siguientes variables:

# nombre (string)
# edad (int)
# correo (string)
# status_code (int)
# response_time (float)
# usuario_activo (bool)

nombre = "Antonio"
edad = 25
correo = "antonio2001@gmail.com"
status_code = 200
response_time = 1.25
usuario_activo = True

# 🧪 Parte 2 - Impresión de datos

# Imprime cada variable junto con su tipo usando type().

print(nombre)
print(type(nombre))

print(edad)
print(type(edad))

print(correo)
print(type(correo))

print(status_code)
print(type(status_code))

print(response_time)
print(type(response_time))

print(usuario_activo)
print(type(usuario_activo))

# 🔍 Parte 3 - Simulación QA (muy importante)

# Imagina que estás validando una respuesta de API:

# status_code = 200
# response_time = 1.25

# Debes crear las siguientes validaciones:

# Validación 1

# Si status_code es 200 → imprimir:

# Prueba exitosa
# Validación 2

# Si response_time es menor o igual a 2.0 → imprimir:

# Performance OK

# Si no:

# Performance lenta

if status_code == 200:
    print("Prueba exitosa.")

if response_time <= 2.0:
    print("Performance OK.")
else:
    print("Performance lenta.")

# 🧠 Parte 4 - Conversión de tipos (casting)

# Haz lo siguiente:

# Convierte edad a string.
# Convierte "100" a entero.
# Convierte response_time a string.

# Imprime el resultado de type() después de cada conversión.

edad = str(edad)

numero = "100"
numero = int(numero)

response_time = str(response_time)

# 🚀 Bonus (nivel entrevista)

# Crea una variable llamada:

# datos_usuario = {
#     "nombre": "Ana",
#     "edad": 28,
#     "activo": True
# }

# Luego imprime:

# nombre del usuario
# edad del usuario

# Usando el diccionario.

datos_usuario = {
    "nombre": "Ana",
    "edad": 28,
    "activo": True
}

print(datos_usuario["nombre"])
print(datos_usuario["edad"])