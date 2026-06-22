def validar_api(response):
    if response["status_code"] == 200:
        return "Prueba aprobada"
    
    return "Prueba fallida"

def validate_status_code(status_code):
    return status_code == 200