from services.hash_helper import HashHelper

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    
    @property
    def password(self):
        return self.__password

    def to_json(self) -> dict:
        return {
            'username': self.username,
            'password': HashHelper.hash_password(self.__password)
        }
        