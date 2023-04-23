import hashlib
from db_helper import Database
from typing import List, Dict, Union

class UserRepository:
    def __init__(self, db: Database) -> None:
        self.db = db
        self.create_table()

    def create_table(self) -> None:
        sql = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
        self.db.execute(sql)

    def login(self, username: str, password: str) -> Union[Dict[str, str], None]:
        hashed_password = self._hash_password(password)
        sql = "SELECT * FROM users WHERE username = ? AND password = ?"
        params = (username, hashed_password)
        result = self.db.execute(sql, params)
        if result:
            return result[0]
        else:
            return None

    def register(self, username: str, password: str) -> None:
        hashed_password = self._hash_password(password)
        sql = "INSERT INTO users (username, password) VALUES (?, ?)"
        params = (username, hashed_password)
        self.db.execute(sql, params)
        self.db.commit()

    def get_all_users(self) -> List[Dict[str, str]]:
        sql = "SELECT * FROM users"
        return self.db.execute(sql)

    def get_user_by_username(self, username: str) -> Union[Dict[str, str], None]:
        sql = "SELECT * FROM users WHERE username = ?"
        params = (username,)
        result = self.db.execute(sql, params)
        if result:
            return result[0]
        else:
            return None

    def update_user_password(self, username: str, password: str) -> None:
        hashed_password = self._hash_password(password)
        sql = "UPDATE users SET password = ? WHERE username = ?"
        params = (hashed_password, username)
        self.db.execute(sql, params)
        self.db.commit()

    def delete_user(self, username: str) -> None:
        sql = "DELETE FROM users WHERE username = ?"
        params = (username,)
        self.db.execute(sql, params)
        self.db.commit()

    def _hash_password(self, password: str) -> str:
        salt = b'salt' # replace with a random salt
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return hashed_password.hex()