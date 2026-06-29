# Quiero que escribas un archivo api_test.py donde:

# Importes requests.

# Hagas un GET a:

# https://jsonplaceholder.typicode.com/users/1
# Imprimas:
# response.status_code
# response.headers["Content-Type"]
# response.elapsed
# Conviertas la respuesta con response.json().
# Imprimas:
# name
# email
# company["name"]
# address["city"]
# Valides:
# Si el status_code es 200, imprime "Status OK".
# Si la ciudad es "Gwenborough", imprime "Ciudad correcta".

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1", verify=False)

print(f"Status code: {response.status_code}")
print(f"Headers: {response.headers['Content-Type']}")
print(f"Response elapsed: {response.elapsed}")

datos = response.json()

print(f"Name: {datos['name']}")
print(f"Email: {datos['email']}")
print(f"Company name: {datos['company']['name']}")
print(f"Address city: {datos['address']['city']}")

if response.status_code == 200:
    print("Status OK")

if datos['address']['city'] == "Gwenborough":
    print("Ciudad correcta")