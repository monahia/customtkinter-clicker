from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(
        self, 
        username: str,
        password: str, 
        email: str = None
    ):
        self.username: str = username
        self.passwordHash = generate_password_hash(password)
        self.email: str = email
        self.createdAt: datetime = datetime.now()
        self.lastLogin = None
    
    def checkPassword(self, password: str) -> bool:
        return check_password_hash(self.passwordHash, password)
    
    def updateLastLogin(self):
        self.lastLogin = datetime.now()