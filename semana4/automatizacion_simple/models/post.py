class Post:

    def __init__(self, data):
        self.user_id = data["userId"]
        self.id = data["id"]
        self.title = data["title"]
        self.body = data["body"]