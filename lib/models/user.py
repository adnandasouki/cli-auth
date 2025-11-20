from utils.hash_helper import HashHelper

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    
    def check_credentials(self, username, password) -> bool:
        if password == HashHelper.hash_password(self.__password) and username == self.username:
            return True
        return False

    def to_json(self) -> dict:
        return {
            'username': self.username,
            'password': HashHelper.hash_password(self.__password)
        }
        