# Ejercicio 1 - Validar cantidad de usuarios

# Tienes la siguiente lista:

# usuarios = ["Ana", "Pedro", "Juan", "Maria", "Carlos"]

# Usa len() para validar si existen exactamente 5 usuarios

# Salida esperada
# Cantidad correcta de usuarios.

# o

# Cantidad incorrecta de usuarios.

usuarios = ["Ana", "Pedro", "Juan", "Maria", "Carlos"]

if len(usuarios) == 5:
    print("Cantidad correcta de usuarios.")
else:
    print("Cantidad incorrecta de usuarios.")

# Ejercicio 2 - Validar longitud de contraseña

# Solicita al usuario una contraseña mediante input().

# Usa len() para validar:

# Si tiene 8 caracteres o más → "Contraseña válida"
# Si tiene menos de 8 caracteres → "Contraseña demasiado corta"
# Ejemplo

# Entrada:

# abc123

# Salida:

# Contraseña demasiado corta

password = input("Ingrese una contraseña: ")

if len(password) >= 8:
    print("Contraseña válida")
else:
    print("Contraseña demasiado corta")

# Ejercicio 3 - Simulación QA API

# Imagina que una API devuelve:

# productos = [
#     {"id": 1},
#     {"id": 2},
#     {"id": 3},
#     {"id": 4}
# ]

# Usa len() para imprimir:

# La API devolvió 4 productos.

# Utiliza una f-string.

productos = [
    {"id": 1},
    {"id": 2},
    {"id": 3},
    {"id": 4}
]

print(f"La API devolvió {len(productos)} productos.")