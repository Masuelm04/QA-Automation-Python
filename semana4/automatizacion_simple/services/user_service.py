from semana4.automatizacion_simple.api.api_client import ApiClient

class UserService:

    def __init__(self):
        self.client = ApiClient()

    def obtener_usuario(self, id_usuario):
        return self.client.get(f"/users/{id_usuario}")