from semana4.automatizacion_simple.api.api_client import ApiClient
from semana4.automatizacion_simple.models.post import Post

class PostService:

    def __init__(self):
        self.client = ApiClient()

    def get_post(self, id_post):
        response = self.client.get(f"/post/{id_post}")

        post = Post(response.json())

        return response, post
    
    def post_post(self, data):
        response = self.client.post(f"/post", data)

        post = Post(response.json())

        return response, post
    
    def put_post(self, id_post, data):
        response = self.client.put(f"/post/{id_post}", data)

        post = Post(response.json())

        return response, post
    
    def patch_post(self, id_post, data):
        response = self.client.patch(f"/post/{id_post}", data)

        post = Post(response.json())

        return response, post
    
    def delete_post(self, id_post):
        response = self.client.delete(f"/post/{id_post}")

        return response