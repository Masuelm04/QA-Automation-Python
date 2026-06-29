# Escribe al menos 10 assert para validar (url = https://jsonplaceholder.typicode.com/users/1):
# 1. status_code == 200
# 2. id == 1
# 3. name == "Leanne Graham"
# 4. username == "Bret"
# 5. email == "Sincere@april.biz"
# 6. address["city"] == "Gwenborough"
# 7. address["zipcode"] == "92998-3874"
# 8. company["name"] == "Romaguera-Crona"
# 9. company["bs"] == "harness real-time e-markets"
# 10. Que el campo "phone" exista y no esté vacío.

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1", verify=False)

assert response.status_code == 200

datos = response.json()

assert datos["id"] == 1, "El ID del usuario no es el esperado."

assert datos["name"] == "Leanne Graham", "Name incorrecto"

assert datos["username"] == "Bret", "Username incorrecto"

assert datos["email"] == "Sincere@april.biz", "Email incorrecto"

assert datos["address"]["city"] == "Gwenborough", "Address city incorrecto"

assert datos["address"]["zipcode"] == "92998-3874", "Address zipcode incorrecto"

assert datos["company"]["name"] == "Romaguera-Crona", "Company name incorrecto"

assert datos["company"]["bs"] == "harness real-time e-markets", "Company bs incorrecto"

assert "phone" in datos, "El campo phone no existe"

assert datos["phone"].strip() != "", "Phone vacío"

print("Campos validados exitosamente!")