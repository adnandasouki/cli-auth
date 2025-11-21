import hashlib

class HashHelper:
    def __init__(self):
        pass

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
