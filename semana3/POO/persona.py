# # Ejercicio 1 - Primera herencia

# # Crea una clase:

# # class Persona

# # Con:

# # nombre

# # en el constructor.

# # Luego crea una clase:

# # class Tester(Persona)

# # sin agregar nada más.

# # Crea un objeto:

# # tester = Tester("Antonio")

# # Imprime:

# # Antonio

# class Persona:

#     def __init__(self, nombre):
#         self.nombre = nombre

# class Tester(Persona):
#     pass

# tester = Tester("Antonio")
# print(tester.nombre)

# # Ejercicio 2 - Herencia con nuevo atributo

# # Partiendo de:

# # class Persona

# # crea:

# # class Tester(Persona)

# # que además reciba:

# # herramienta

# # Utiliza:

# # super().__init__()

# # para inicializar el nombre.

# # Prueba con:

# # Tester("Antonio", "Playwright")

# # Imprime:

# # Antonio
# # Playwright

# class Persona:

#     def __init__(self, nombre):
#         self.nombre = nombre

# class Tester(Persona):

#     def __init__(self, nombre, herramienta):
#         super().__init__(nombre)

#         self.herramienta = herramienta

# tester = Tester("Antonio", "Playwright")

# print(tester.nombre)
# print(tester.herramienta)

# # Ejercicio 3 - Método heredado

# # Crea:

# # class Usuario

# # Con un método:

# # saludar()

# # que imprima:

# # Hola usuario

# # Luego crea:

# # class Admin(Usuario)

# # sin agregar métodos.

# # Verifica que el objeto Admin pueda ejecutar:

# # admin.saludar()

# class Usuario:

#     def __init__(self, nombre):
#         self.nombre = nombre

#     def saludar(self):
#         print(f"Hola {self.nombre}")

# class Admin(Usuario):
#     pass

# admin = Admin("Masuel")
# admin.saludar()

# # Ejercicio 4 - Override (sobrescritura)

# # Partiendo del ejercicio anterior:

# # Haz que:

# # class Admin

# # sobrescriba:

# # saludar()

# # para imprimir:

# # Hola administrador

# class Usuario:

#     def __init__(self, nombre):
#         self.nombre = nombre

#     def saludar(self):
#         print(f"Hola {self.nombre}")

# class Admin(Usuario):

#     def saludar(self):
#         print("Hola administrador")

# admin = Admin("Masuel")
# admin.saludar()

# Ejercicio 5 - Encapsulación básica

# Crea una clase:

# class Usuario

# Con:

# self.__password

# igual a:

# "1234"

# Crea un método:

# obtener_password()

# que retorne la contraseña.

# Prueba:

# usuario.obtener_password()

class Usuario:

    def __init__(self):
        self.__password = "1234"

    def obtener_password(self):
        return self.__password
    
usuario = Usuario()
print(usuario.obtener_password())