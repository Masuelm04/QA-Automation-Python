from semana4.automatizacion_simple.services.user_service import UserService
from semana4.automatizacion_simple.utils.validators import Validators

service = UserService()
validator = Validators()

response, usuario = service.get_usuario(1)

validator.validar_status_code(response, 200)
validator.validar_campo_igual("id", 1, usuario.id)
validator.validar_campo_igual("name", "Leanne Graham", usuario.name)
validator.validar_campo_igual("username", "Bret", usuario.username)
validator.validar_campo_igual("email", "Sincere@april.biz", usuario.email)

print("Usuario validado correctamente.")