from semana4.automatizacion_simple.services.user_service import UserService

service = UserService()

response, usuario = service.get_usuario(1)

assert response.status_code == 200, "GET fallido"
assert usuario.id == 1, f"Id esperado: 1. Obtenido: {usuario.id}"
assert usuario.name == "Leanne Graham", f"Name esperado: Leanne Graham. Obtenido: {usuario.name}"
assert usuario.username == "Bret", f"Usuario esperado: Bret. Obtenido: {usuario.username}"
assert usuario.email == "Sincere@april.biz"

print("Usuario validado correctamente.")