from services.auth_contract import AuthContract
from services.hash_helper import HashHelper
from services.db_helper import DbHelper
from services.validator import Validator
from models.user import User

class Auth(AuthContract):
    db = DbHelper()
    signedIn = False

    def __init__(self):
        pass

    def logIn(self, username: str, password: str):
        try:
            users = self.db.users()

            if username not in users:
                print('no account found!')
                return False
            
            user = users[username]
            login_password = HashHelper.hash_password(password)
            stored_password = user['password']

            if login_password == stored_password:
                print('signed in!')
                self.signedIn = True
                return True
            
            print('wrong password!')
            return False
        except Exception as e:
            print('login error:', e)
            return False

    def signUp(self, user: User):
        try:
            users = self.db.users()

            valid, message = Validator.validate_username(user.username)
            if not valid:
                print(message)
                return
            
            valid, message = Validator.validate_password(user.password)
            if not valid:
                print(message)
                return
            
            if user.username in users:
                print('username taken.')
                return
            
            self.db.createData(user)
            print('account creted!')
            return
            
        except Exception as e:
            print('signup error:', e)
            return
    
    def signOut(self):
        self.signedIn = False
        print('signed out!')
        return
    
    def change_username(self, username, newUsername):
        try:
            users = self.db.users()

            valid, message = Validator.validate_username(newUsername)
            if not valid:
                print(message)
                return username
            
            if newUsername in users:
                print('username taken!')
                return username
            
            self.db.update_username(username, newUsername)
            print(f'username has been updated to {newUsername}')
            return newUsername

        except Exception as e:
            print('change username error:', e)
            return newUsername
        
    def change_password(self, username, newPassword):
        valid, message = Validator.validate_password(newPassword)
        if not valid:
            print(message)
            return

        self.db.update_password(username, newPassword)
        print('password has been updated!')
        
        
    def delete_account(self, username):
        self.db.deleteData(username)
        print('account deleted!')
        self.signOut()
