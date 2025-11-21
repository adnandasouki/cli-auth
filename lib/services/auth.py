from services.auth_contract import AuthContract
from services.hash_helper import HashHelper
from services.db_helper import DbHelper
from services.validator import Validator
from services.logger import logging
from models.user import User

class Auth(AuthContract):
    db = DbHelper()
    signedIn = False

    def signIn(self, username: str, password: str):
        try:
            users = self.db.users()

            if username not in users:
                logging.warning(f"Login Failed: username '{username}' not found")
                return False, "no account found!"
            
            user = users[username]
            login_password = HashHelper.hash_password(password)
            stored_password = user['password']

            if login_password == stored_password:
                self.signedIn = True
                logging.info(f"user '{username}' signed in")
                return True, "signed in!"
            
            logging.warning(f"Login Failed: wrong password for '{username}'")
            return False, "wront password!"
            
        except Exception as e:
            logging.error(f"Exception in signin: {e}")
            return False, f"login error: {e}"

    def signUp(self, user: User):
        try:
            users = self.db.users()
            try:
                valid, message = Validator.validate_username(user.username)
                if not valid:
                    return False, message
                
                valid, message = Validator.validate_password(user.password)
                if not valid:
                    return False, message
            except Exception as e:
                return False, f'Validation Error: {e}'
            
            if user.username in users:
                return False, "username taken!"
            
            self.db.createData(user)
            logging.info(f"New account created for user: {user.username}")
            return True, "account created!"
            
        except Exception as e:
            logging.error(f"Exception in signup: {e}")
            return False, f'signup error: {e}'
    
    def signOut(self):
        self.signedIn = False
        return "signed out!"
    
    def change_username(self, username, newUsername):
        try:
            users = self.db.users()

            valid, message = Validator.validate_username(newUsername)
            if not valid:
                return False, username, message
            
            if newUsername in users:
                return False, username, message
            
            self.db.update_username(username, newUsername)
            logging.info(f"user '{username}' updated their username to '{newUsername}'")
            return True, newUsername, f"username has been updated to {newUsername}"

        except Exception as e:
            logging.error(f"Exception in change username: {e}")
            return False, newUsername, f"change username error: {e}"
        
    def change_password(self, username, newPassword):
        try:
            valid, message = Validator.validate_password(newPassword)
            if not valid:
                return False, message

            self.db.update_password(username, newPassword)
            logging.info(f"user '{username}' updated their password")
            return True, "password has been updated!"
        except Exception as e:
            logging.error(f"Exception in change password: {e}")
            return False, f"Exception in change password: {e}"
        
    def delete_account(self, username):
        self.db.deleteData(username)
        self.signedIn = False
        logging.info(f"user '{username}' deleted their account")
        return True, "account deleted!"
