# Ejercicio 10 - Mini Framework QA (Nivel entrevista)

# Crea una clase padre:

# TestCase

# Con un método:

# ejecutar()

# que imprima:

# Ejecutando prueba genérica

# Luego crea dos clases hijas:

# LoginTest
# ApiTest

# Cada una debe sobrescribir:

# ejecutar()

# para imprimir:

# Ejecutando prueba de Login

# y

# Ejecutando prueba de API

# respectivamente.

# Después:

# tests = [
#     LoginTest(),
#     ApiTest()
# ]

# Recórrelos con un for y ejecuta:

# ejecutar()

class TestCase:

    def __init__(self):
        pass

    def ejecutar(self):
        print("Ejecutando prueba genérica")

class LoginTest(TestCase):

    def ejecutar(self):
        print("Ejecutando prueba de Login")

class ApiTest(TestCase):

    def ejecutar(self):
        print("Ejecutando prueba de API")

tests = [LoginTest(), ApiTest()]

for test in tests:
    test.ejecutar()