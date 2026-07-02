import requests

class ApiClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get(self, endpoint):
        return requests.get(f"{self.BASE_URL}{endpoint}", verify=False)
    
    def post(self, endpoint, data):
        return requests.post(f"{self.BASE_URL}{endpoint}", json=data, verify=False)
    
    def put(self, endpoint, data):
        return requests.put(f"{self.BASE_URL}{endpoint}", json=data, verify=False)
    
    def patch(self, endpoint, data):
        return requests.patch(f"{self.BASE_URL}{endpoint}", json=data, verify=False)
    
    def delete(self, endpoint):
        return requests.delete(f"{self.BASE_URL}{endpoint}", verify=False)