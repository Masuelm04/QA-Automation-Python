from api_client import ApiClient
import json
from pathlib import Path

ruta_json = Path(__file__).parent.parent / "data" / "posts.json"

with open(ruta_json, "r") as archivo:
    posts = json.load(archivo)

client = ApiClient()

response = client.post("/posts", posts)

data = response.json()

print(f"Data post: {data}")

assert response.status_code == 201

print("POST completado correctamente.")

keys = ["title", "body", "userId", "id"]

for key in keys:
    assert key in data, f"No existe el campo {key}"

assert data["title"] == "Mi primer Post", f"Title esperado: Mi primer Post. Obtenido: {data["title"]}"
assert data["body"] == "Aprendiendo QA Automation", f"Body esperado: Aprendiendo QA Automation. Recibido: {data["body"]}"
assert data["userId"] == 1, f"userId esperado: 1. Obtenido: {data["userId"]}"

print("Keys validadas correctamente.")

data = {
    "id": 1,
    "title": "Post actualizado",
    "body": "Contenido actualizado",
    "userId": 1
}

response = client.put("/posts/1", data)

datos = response.json()

print(f"Data put: {data}")

assert response.status_code == 200, "La solicitud actualización de datos ha fallado"
assert data["title"] == "Post actualizado"
assert data["body"] == "Contenido actualizado"
assert data["userId"] == 1

print("PUT completado correctamente.")

data = {
    "title": "Nuevo título"
}

response = client.patch("/posts/1", data)

datos = response.json()

print(f"Data patch: {data}")

assert datos["title"] == "Nuevo título"

print("PATCH completado correctamente.")

response = client.delete("/posts/1")

assert response.status_code == 200, "El registro no pudo ser eliminado"

print("DELETE completado correctamente.")