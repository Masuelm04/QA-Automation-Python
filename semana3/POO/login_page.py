# Ejercicio 9 - Simulación LoginPage

# ⚠️ Este ejercicio ya se parece a Playwright.

# Crea una clase:

# LoginPage

# Con un método:

# login(usuario, password)

# Reglas:

# Si:

# usuario == "admin"
# password == "1234"

# Imprimir:

# Login exitoso

# En caso contrario:

# Credenciales incorrectas

# Ejemplo:

# pagina = LoginPage()

# pagina.login("admin", "1234")

class LoginPage:

    def __init__(self):
        pass

    def login(self, usuario, password):
        if usuario == "admin" and password == "1234":
            print("Login exitoso")
        else:
            print("Credenciales incorrectas")

pagina = LoginPage()
pagina.login("admin", "1234")