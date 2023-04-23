from PySide6.QtCore import QObject, Signal, Property

class User(QObject):
    usernameChanged = Signal(str)
    passwordChanged = Signal(str)

    def __init__(self, username="", password=""):
        super().__init__()
        self._username = username
        self._password = password

    @Property(str, notify=usernameChanged)
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value
        self.usernameChanged.emit(value)

    @Property(str, notify=passwordChanged)
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
        self.passwordChanged.emit(value)