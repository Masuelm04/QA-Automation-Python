class User:

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.username = data["username"]
        self.email = data["email"]
        self.phone = data["phone"]
        self.website = data["website"]