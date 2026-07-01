from api.api_client import ApiClient

class UserService:

    def __init__(self):
        self.client = ApiClient()

    def obtener_usuario(self, id_usuario):
        self.client.get(id_usuario)

service = UserService()
usuario = service.obtener_usuario(1)