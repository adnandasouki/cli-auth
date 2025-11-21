import re

class Validator:
    @staticmethod
    def validate_username(username: str) -> tuple[bool, str]:
        if len(username) < 3:
            return False, "Username must be at least 3 characters"
        
        if " " in username:
            return False, "Username cannot contain spaces"
        
        if not username.isalnum():
            return False, "Username must be alphanumeric only"
        
        return True, ""
    
    @staticmethod
    def validate_password(password: str) -> tuple[bool, str]:
        if len(password) < 6:
            return False, "Password must be at least 6 characters"
        
        if " " in password:
            return False, "Password cannot contain spaces"
        
        if not re.search(r"[A-Za-z]", password):
            return False, "Password must contain at least one letter"
        
        if not re.search(r"\d", password):
            return False, "Password must contain at least one number"

        return True, ""