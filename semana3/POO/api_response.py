# Ejercicio 7 - Clase orientada a QA

# Crea una clase:

# ApiResponse

# Que reciba:

# status_code
# response_time

# Agrega un método:

# es_exitosa()

# Reglas:

# status 200 → True
# cualquier otro → False

# Ejemplo:

# response = ApiResponse(200, 1.5)

# print(response.es_exitosa())

# Salida:

# True

class ApiResponse:

    def __init__(self, status_code, response_time):
        self.status_code = status_code
        self.response_time = response_time

    def es_exitosa(self):
        return self.status_code == 200
    
response = ApiResponse(200, 1.5)
print(response.es_exitosa())

# Ejercicio 8 - Múltiples métodos QA

# Partiendo de la clase anterior:

# ApiResponse

# Agrega:

# validar_performance()

# Reglas:

# response_time <= 2 → "Performance OK"
# response_time > 2 → "Performance lenta"

# Ejemplo:

# response = ApiResponse(200, 3.5)

# print(response.validar_performance())

# Salida:

# Performance lenta

class ApiResponse:

    def __init__(self, status_code, response_time):
        self.status_code = status_code
        self.response_time = response_time

    def validar_performance(self):
        if self.response_time <= 2:
            return "Performance OK"
        else:
            return "Performance lenta"

response = ApiResponse(200, 3.5)
print(response.validar_performance())