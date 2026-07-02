import requests

class ApiClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.headers = { 
            "Content-Type": "application/json"
        }
        self.timeout = 10

    def get(self, endpoint):
        return requests.get(f"{self.BASE_URL}{endpoint}", headers=self.headers, timeout=self.timeout, verify=False)
    
    def post(self, endpoint, data):
        return requests.post(f"{self.BASE_URL}{endpoint}", headers=self.headers, timeout=self.timeout,json=data, verify=False)
    
    def put(self, endpoint, data):
        return requests.put(f"{self.BASE_URL}{endpoint}", headers=self.headers, timeout=self.timeout,json=data, verify=False)
    
    def patch(self, endpoint, data):
        return requests.patch(f"{self.BASE_URL}{endpoint}", headers=self.headers, timeout=self.timeout,json=data, verify=False)
    
    def delete(self, endpoint):
        return requests.delete(f"{self.BASE_URL}{endpoint}", headers=self.headers, timeout=self.timeout,verify=False)