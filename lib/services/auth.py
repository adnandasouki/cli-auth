from lib.services.auth_contract import AuthContract
from lib.services.hash_helper import HashHelper
from lib.services.db_helper import DbHelper
from lib.models.user import User

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
            
            if newUsername not in users:
                self.db.update_username(username, newUsername)
                print(f'username has been updated to {newUsername}')
                return newUsername
            
            print('username taken!')
            return
        except Exception as e:
            print('change username error:', e)
            return newUsername
        
    def change_password(self, username, newPassword):
        self.db.update_password(username, newPassword)
        print('password has been updated!')
        
        
    def delete_account(self, username):
        self.db.deleteData(username)
        print('account deleted!')
        self.signOut()
