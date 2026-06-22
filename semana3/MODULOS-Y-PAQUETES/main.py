import validaciones
from qa_utils import validar_response_time
from api_validaciones import validar_estado, validar_tiempo
import calculadora as calc
from datos import usuario
from api import validar_api, validate_status_code
from usuarios import user

print(validaciones.validar_status(200))
print(validaciones.validar_status(404))

print(validar_response_time(1.5))
print(validar_response_time(3.2))

print(validar_estado(200))
print(validar_tiempo(1.8))

print(calc.sumar(10, 5))
print(calc.restar(10, 5))

print(usuario["nombre"])
print(usuario["correo"])

print(validaciones.validar_login("admin", "1234"))

response = {
    "status_code": 200
}

print(validar_api(response))

print(validaciones.usuario_activo(user))
print(validate_status_code(200))