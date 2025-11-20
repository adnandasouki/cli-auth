from .auth_contract import AuthContract
from utils.hash_helper import HashHelper
from utils.db_helper import DbHelper
from models.user import User

class Auth(AuthContract):
    db = DbHelper()
    signedIn = False

    def __init__(self):
        pass

    def logIn(self, username: str, password: str):
        if self.db.userData(username)['username'] == username and self.db.userData(username)['password'] == HashHelper.hash_password(password):
            self.signedIn = True
            return self.signedIn
        else:
            self.signedIn = False
            return self.signedIn
    
    def signUp(self, user: User):
        self.db.createData(user)
    
    def signOut(self):
        self.signedIn = False
        return self.signedIn
    
    def change_username(self, currentUsername, newUsername):
        self.db.update_username(currentUsername, newUsername)
        return newUsername
        

    def change_password(self, username, newPassword):
        self.db.update_password(username, newPassword)
        
    def delete_account(self, username):
        self.db.deleteData(username)
