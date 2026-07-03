def validar_status(status_code):
    return status_code == 200

def validar_login(usuario, password):
    return usuario == "admin" and password == "1234"

def usuario_activo(usuario):
    return usuario["activo"]