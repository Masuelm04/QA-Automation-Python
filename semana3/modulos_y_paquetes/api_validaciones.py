def validar_estado(status_code):
    return status_code == 200

def validar_tiempo(response_time):
    return response_time <= 2