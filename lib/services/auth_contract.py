from abc import ABC, abstractmethod

class AuthContract(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def signIn(self):
        pass

    @abstractmethod
    def signUp(self):
        pass

    @abstractmethod
    def signOut(self):
        pass