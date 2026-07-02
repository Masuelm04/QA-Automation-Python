from semana4.automatizacion_simple.api.api_client import ApiClient
from semana4.automatizacion_simple.models.user import User

class UserService:

    def __init__(self):
        self.client = ApiClient()

    def get_usuario(self, id_usuario):
        response = self.client.get(f"/users/{id_usuario}")

        usuario = User(response.json())

        return response, usuario