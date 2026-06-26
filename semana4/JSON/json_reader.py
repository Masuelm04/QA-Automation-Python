import json

with open("semana4/JSON/usuario.json", "r") as archivo:
    datos = json.load(archivo)

print(datos)
print(datos['nombre'])

if datos['activo'] == True:
    print(f"El usuario {datos['nombre']} está activo")
    
if datos['status_code'] == 200:
    print("Status OK")

print(datos['usuario']['nombre'])
print(datos['usuario']['edad'])

for cliente in datos['clientes']:
    print(cliente['nombre'])

for empleado in datos['empleados']:
    if empleado['activo'] == True:
        print(empleado['nombre'])