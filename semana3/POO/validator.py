# Ejercicio 9 - Polimorfismo

# Crea dos clases:

# ApiValidator

# y

# UiValidator

# Ambas deben tener:

# validar()

# pero cada una imprime algo distinto:

# Validando API
# Validando UI

# Luego:

# validadores = [
#     ApiValidator(),
#     UiValidator()
# ]

# Recórrelos con un for y ejecuta:

# validar()

class ApiValidator:

    def __init__(self):
        pass

    def validar(self):
        print("Validando API")

class UiValidator:

    def __init__(self):
        pass

    def validar(self):
        print("Validando UI")

validadores = [ApiValidator(), UiValidator()]

for validador in validadores:
    validador.validar()