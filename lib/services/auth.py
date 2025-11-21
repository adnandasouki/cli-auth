from services.auth_contract import AuthContract
from services.hash_helper import HashHelper
from services.db_helper import DbHelper
from services.validator import Validator
from models.user import User

class Auth(AuthContract):
    db = DbHelper()
    signedIn = False

    def signIn(self, username: str, password: str):
        try:
            users = self.db.users()

            if username not in users:
                return False, "no account found!"
            
            user = users[username]
            login_password = HashHelper.hash_password(password)
            stored_password = user['password']

            if login_password == stored_password:
                self.signedIn = True
                return True, "signed in!"
            
            return False, "wront password!"
        
        except Exception as e:
            return False, f"login error: {e}"

    def signUp(self, user: User):
        try:
            users = self.db.users()

            valid, message = Validator.validate_username(user.username)
            if not valid:
                return False, message
            
            valid, message = Validator.validate_password(user.password)
            if not valid:
                return False, message
            
            if user.username in users:
                return False, "username taken!"
            
            self.db.createData(user)
            return True, "account created!"
            
        except Exception as e:
            return False, f'signup error: {e}'
    
    def signOut(self):
        self.signedIn = False
        return "signed out!"
    
    def change_username(self, username, newUsername):
        try:
            users = self.db.users()

            valid, message = Validator.validate_username(newUsername)
            if not valid:
                return username, message
            
            if newUsername in users:
                return username, message
            
            self.db.update_username(username, newUsername)
            return newUsername, f"username has been updated to {newUsername}"

        except Exception as e:
            return newUsername, f"change username error: {e}"
        
    def change_password(self, username, newPassword):
        valid, message = Validator.validate_password(newPassword)
        if not valid:
            return message

        self.db.update_password(username, newPassword)
        return "password has been updated!"
        
        
    def delete_account(self, username):
        self.db.deleteData(username)
        self.signedIn = False
        return True, "account deleted!"
