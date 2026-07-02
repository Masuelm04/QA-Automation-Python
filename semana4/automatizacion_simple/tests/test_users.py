from semana4.automatizacion_simple.services.user_service import UserService

user = UserService()

response = user.obtener_usuario(1)

data = response.json()

keys = ["id", "name"]

for key in keys:
    assert key in data

assert response.status_code == 200, "GET fallido"
assert data["id"] == 1, f"Id esperado: 1. Obtenido: {data["id"]}"
assert data["name"] == "Leanne Graham", f"Name esperado: Leanne Graham. Obtenido: {data["name"]}"