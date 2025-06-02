import yaml
import os

DATA_FILE = "data/user.yml"

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_dict(self):
        return {"username": self.username, "email": self.email}


class UserManager:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(DATA_FILE):
            return []

        f = open(DATA_FILE, "r", encoding="utf-8")
        try:
            data = yaml.safe_load(f)
            if data:
                return data
            else:
                return []
        finally:
            f.close()

    def save_users(self):
        f = open(DATA_FILE, "w", encoding="utf-8")
        try:
            yaml.dump(self.users, f, allow_unicode=True)
        finally:
            f.close()

    def add_user(self, username, email):
        user = User(username, email)
        self.users.append(user.to_dict())
        self.save_users()

    def list_users(self):
        return self.users
