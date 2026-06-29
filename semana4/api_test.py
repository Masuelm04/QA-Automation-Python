import requests

# Validar que la petición funcione
response = requests.get("https://jsonplaceholder.typicode.com", verify=False)
print(response)

response_user = requests.get("https://jsonplaceholder.typicode.com/users/1", verify=False)

# Obtener el Body
print(response_user.text)

# Convertir a JSON
datos = response_user.json() 
print(datos)

print(type(datos))

# Obtener el Status Code
print(response_user.status_code)

# Validar Status Code
if response_user.status_code == 200:

    datos_usuario = response_user.json()

    print(datos_usuario['name'])

    print(datos_usuario['email'])

    print(datos_usuario['username'])
else:
    print("Error")

# Validar un campo del JSON
print(datos['name'])

if datos['id'] == 1:
    print("Usuario correcto")