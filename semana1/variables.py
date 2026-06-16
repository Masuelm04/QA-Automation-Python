nombre = "Masuel"
correo = "masuelm04@gmail.com"
edad = 22
peso = 172.5
usuario_activo = True

print(nombre)
print(type(nombre))

print(correo)
print(type(correo))

print(edad)
print(type(edad))

print(peso) 
print(type(peso))

print(usuario_activo)
print(type(usuario_activo))

base_url = "https://api.test.com"
endpoint = "/users"
status_code = 200
token = "abc123"
request = (base_url + endpoint)

print(request)

edad_next_year = "23"
edad_next_year = int(edad_next_year)

print(edad_next_year)
print(edad + edad_next_year)

edad_string = str(edad)
print("Mi edad es: " + edad_string + " años.")

edad_decimal = float(edad_next_year) + 0.5 
print(edad_decimal)

encendido = 1
encendido = bool(encendido)
print(encendido)

nombre_completo = input("Ingrese su nombre completo: ")
print("Bienvenido al sistema: " + nombre_completo)
print(len(nombre_completo))

edad_actualizada = input("Ingrese su edad: ")
print(int(edad_actualizada) + edad)