from api_client import ApiClient

client = ApiClient()

response = client.get("/users/1") 

datos = response.json()

assert response.status_code == 200
assert datos["id"] == 1

print("Prueba completada.")
print(datos)

assert datos["name"] == "Leanne Graham", "Name es incorrecto"
assert datos["username"] == "Bret", "Username es incorrecto"
assert datos["email"] == "Sincere@april.biz", "Email es incorrecto"
assert datos["address"]["street"] == "Kulas Light", "Street address es incorrecto"
assert datos["address"]["suite"] == "Apt. 556", "Suite address es incorrecto"
assert datos["address"]["city"] == "Gwenborough", "City address es incorrecto"
assert datos["address"]["zipcode"] == "92998-3874", "Zipcode address es incorrecto"
assert datos["phone"] == "1-770-736-8031 x56442", "Phone es incorrecto"
assert datos["website"] == "hildegard.org", "El website es incorrecto"
assert datos["company"]["name"] == "Romaguera-Crona", "Company name es incorrecto"

print("Prueba completada.")