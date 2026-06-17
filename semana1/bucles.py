usuarios = ["Ana", "Pedro", "juan"]

for usuario in usuarios:
    print(usuario)

for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(11, 20, 2):
    print(i)

status_codes = [200, 404, 500, 201]

for codigo in status_codes:

    if codigo == 200:
        print("OK")

    elif codigo == 201:
        print("Creado")

    elif codigo == 404:
        print("No encontrado")

    elif codigo == 500:
        print("Error")

usuarios = ["Ana", "Pedro", "Juan"]

for indice, usuario in enumerate(usuarios):
    print(indice, usuario)