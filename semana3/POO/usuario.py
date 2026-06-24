# Ejercicio 1 - Tu primera clase

# Crea una clase llamada:

# Usuario

# La clase puede estar vacía utilizando:

# pass

# Luego:

# Crea un objeto llamado usuario1
# Imprime el tipo del objeto usando type()
# Salida esperada (similar)
# <class '__main__.Usuario'>

class Usuario:
    pass

usuario1 = Usuario()

print(type(usuario1))

# Ejercicio 2 - Constructor básico

# Crea una clase:

# Usuario

# Con un constructor que imprima:

# Usuario creado correctamente

# Al crear un objeto.

# Luego:

# usuario = Usuario()

# Observa qué ocurre.

class Usuario:

    def __init__(self):
        print("Usuario creado correctamente.")

usuario = Usuario()

# Ejercicio 3 - Primer atributo

# Crea una clase:

# Usuario

# Con un constructor que asigne:

# self.nombre = "Antonio"

# Luego:

# Crea un objeto
# Imprime el atributo nombre
# Salida esperada
# Antonio

class Usuario:
    def __init__(self):
        self.nombre = "Antonio"

usuario = Usuario()
print(usuario.nombre)

# Ejercicio 4 - Constructor con parámetros

# Crea una clase:

# Usuario

# Que reciba:

# nombre
# edad

# y los guarde en atributos.

# Luego crea:

# usuario1 = Usuario("Ana", 25)
# usuario2 = Usuario("Pedro", 30)

# Imprime los datos de ambos objetos.

# Salida esperada
# Ana
# 25

# Pedro
# 30

class Usuario:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

usuario1 = Usuario("Ana", 25)
usuario2 = Usuario("Pedro", 30)

print(usuario1.nombre)
print(usuario1.edad)
print()
print(usuario2.nombre)
print(usuario2.edad)

# Ejercicio 5 - Primer método

# Crea una clase:

# Usuario

# Con:

# atributo nombre
# método saludar()

# El método debe imprimir:

# Hola Ana

# (o el nombre correspondiente).

# Ejemplo:

# usuario = Usuario("Ana")

# usuario.saludar()

class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola {self.nombre}")

usuario = Usuario("Ana")
usuario.saludar()

# Ejercicio 6 - Método con lógica

# Crea una clase:

# Usuario

# Con:

# nombre
# edad

# Agrega un método:

# es_mayor_de_edad()

# Debe retornar:

# True

# si la edad es 18 o más.

# False

# en caso contrario.

# Prueba con varios usuarios.

class Usuario:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor_de_edad(self):
        return self.edad >= 18

usuario1 = Usuario("Masuel", 22)
usuario2 = Usuario("Antonio", 14)
usuario3 = Usuario("Maria", 17)
usuario4 = Usuario("Mario", 18)

print(usuario1.es_mayor_de_edad())
print(usuario2.es_mayor_de_edad())
print(usuario3.es_mayor_de_edad())
print(usuario4.es_mayor_de_edad())

# Ejercicio 10 - Lista de objetos (Nivel QA Junior)

# Crea una clase:

# Usuario

# Con:

# nombre
# activo

# Crea los siguientes objetos:

# usuario1 = Usuario("Ana", True)
# usuario2 = Usuario("Pedro", False)
# usuario3 = Usuario("Juan", True)
# usuario4 = Usuario("Maria", False)

# Guárdalos en una lista.

# Luego recorre la lista e imprime únicamente los usuarios activos.

# Salida esperada
# Ana
# Juan

class Usuario:

    def __init__(self, nombre, activo):
        self.nombre = nombre
        self.activo = activo

usuario1 = Usuario("Ana", True)
usuario2 = Usuario("Pedro", False)
usuario3 = Usuario("Juan", True)
usuario4 = Usuario("Maria", False)

lista_usuarios = [usuario1, usuario2, usuario3, usuario4]

for usuario in lista_usuarios:
    if usuario.activo:
        print(usuario.nombre)

# Desafío de entrevista QA Automation

# Sin ejecutar el código:

# class Usuario:

#     def __init__(self, nombre):
#         self.nombre = nombre

#     def saludar(self):
#         print(f"Hola {self.nombre}")


# usuario = Usuario("Antonio")

# usuario.saludar()
# Preguntas
# ¿Qué imprimirá?
#   Hola Antonio
# ¿Qué representa self.nombre?
#   self.nombre es un atributo de instancia. Permite almacenar el valor del nombre dentro de cada objeto creado a partir de la clase.
# ¿Qué ocurriría si eliminas self del constructor?
#   Python no identifica el objeto al que se quiere especificar
# ¿Por qué saludar() puede acceder a nombre sin recibirlo como parámetro?
#   Porque el atributo fue almacenado previamente en la instancia mediante self.nombre, y cualquier método de la clase puede acceder a los atributos de esa misma instancia utilizando self.

# Desafío de entrevista QA Automation

# Sin ejecutar:

# class Usuario:

#     def __init__(self):
#         self.__password = "1234"

#     def obtener_password(self):
#         return self.__password

# usuario = Usuario()

# print(usuario.obtener_password())
# Preguntas
# ¿Qué imprime?
#   1234
# ¿Dónde está almacenada la contraseña?
#   La contraseña está almacenada en el atributo __password
# ¿Por qué funciona obtener_password() pero no usuario.__password?
#   Porque se usa la convención de private para el atributo y con el name mangling se limita directamente el acceso al atributo
# ¿Qué principio de POO se está utilizando?
#   Se está utilizando la encapsulación
# ¿Qué ventaja tiene esto en un framework de automatización?
#   Es una ventaja, ya que limita el acceso de informaciones sensibles que deben ser protegidas y accedidas
# en partes especificas de el aplicativo