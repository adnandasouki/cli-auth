class Validator:
    @staticmethod
    def validate_username(username: str):
        if len(username) < 3:
            return False, "username must be at least 3 characters"
        
        if " " in username:
            return False, "username cannot contain spaces"
        
        if not username.isalnum():
            return False, "username must be alphanumeric only"
        
        return True, ""
    
    @staticmethod
    def validate_password(password: str):
        if len(password) < 6:
            return False, "password must be at least 6 characters"
        
        if " " in password:
            return False, "password cannot contain spaces"

        return True, ""