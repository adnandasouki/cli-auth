from services.hash_helper import HashHelper
from models.user import User
import json

class DbHelper:
    db_path = 'data/users.json'
    
    def __init__(self):
        self.load_db()

    def load_db(self):
        try: 
            with open(self.db_path, 'r') as db_file:
                return json.load(db_file)
        except FileNotFoundError:
            return {}
            
    def save_db(self, data):
        with open(self.db_path, 'w') as db_file:
            json.dump(data, db_file, indent=4)

    def createData(self, user: User):
        users = self.load_db()
        users[user.username] = user.to_json()
        self.save_db(users)

    def users(self):
        return self.load_db()
    
    def update_username(self, username, newUsername):
        users = self.load_db()
        users[newUsername] = users.pop(username)
        users[newUsername]['username'] = newUsername
        self.save_db(users)

    def update_password(self, username, password: str):
        users = self.load_db()
        users[username]['password'] = HashHelper.hash_password(password)
        self.save_db(users)
        return 'password updated'
    
    def deleteData(self, username):
        users = self.load_db()
        del users[username]
        self.save_db(users)
        return 'data deleted'