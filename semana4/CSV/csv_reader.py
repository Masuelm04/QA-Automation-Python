import csv

with open("semana4/CSV/usuario.csv", "r") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        if fila["activo"] == "True": 
            print(fila["nombre"])

with open("semana4/CSV/empleados.csv", "r") as file:
    lector1 = csv.DictReader(file)

    for fila in lector1:
        if fila["activo"] == "True":
            print(fila["nombre"])

with open("semana4/CSV/empleados_activos.csv", "a") as file1:
    lector2 = csv.DictWriter(file1)

    for fila in lector2:
        if fila["activo"] == "True":
            print(fila["nombre"])