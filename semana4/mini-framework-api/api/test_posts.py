from api_client import ApiClient
import json
from pathlib import Path

ruta_json = Path(__file__).parent.parent / "data" / "posts.json"

with open(ruta_json, "r") as archivo:
    posts = json.load(archivo)

client = ApiClient()

response_post = client.post("/posts", posts)

data_post = response_post.json()

assert response_post.status_code == 201

print("Post creado correctamente.")

keys = ["title", "body", "userId", "id"]

for key in keys:
    assert key in data_post, f"No existe el campo {key}"

assert data_post["title"] == "Mi primer Post", f"Title esperado: Mi primer Post. Obtenido: {data_post["title"]}"
assert data_post["body"] == "Aprendiendo QA Automation", f"Body esperado: Aprendiendo QA Automation. Recibido: {data_post["body"]}"
assert data_post["userId"] == 1, f"userId esperado: 1. Obtenido: {data_post["userId"]}"

print("Keys validadas correctamente.")

update_post = {
    "id": 1,
    "title": "Post actualizado",
    "body": "Contenido actualizado",
    "userId": 1
}

response_put = client.put("/posts/1", update_post)

data_put = response_put.json()

assert response_put.status_code == 200, "La solicitud actualización de datos ha fallado"
assert data_put["title"] == "Post actualizado"
assert data_put["body"] == "Contenido actualizado"
assert data_put["userId"] == 1

print("Datos actualizados correctamente.")