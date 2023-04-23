import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout , QLabel, QLineEdit, QPushButton
from PySide6.QtGui import  QIcon, QPalette, QColor, QPixmap
from PySide6.QtCore import Signal,Slot

WINDOW_TITLE = f"HHU Helper | Login"

class UsernameField(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setPlaceholderText("Username")
        self.setMinimumSize(375,36)
        self.setMaximumSize(375,36)

class PasswordField(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setPlaceholderText("Password")
        self.setEchoMode(QLineEdit.Password)
        self.setMinimumSize(375,36)
        self.setMaximumSize(375,36)

class LoginButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setText("Login")
        self.setMinimumSize(375,40)
        self.setMaximumSize(375,40)

class LoginLayout(QVBoxLayout):
    def __init__ (self)-> None:
        super().__init__()

        # Add the logo and brand title to the layout
        logo_label = QLabel()
        logo_pixmap = QPixmap("./public/images/logo.jpg")
        logo_label.setPixmap(logo_pixmap)
        logo_label.setMinimumSize(200,200)
        logo_label.setMaximumSize(200,200)
        self.addWidget(logo_label)

        brand_label = QLabel("HHU Helper")
        self.addWidget(brand_label)

        self.username_field = UsernameField()
        self.password_field = PasswordField()
        self.addWidget(self.username_field)
        self.addWidget(self.password_field)

class LoginScreen(QWidget):
    login_signal = Signal(str, str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("HHU Helper | Login")
        self.resize(720,540)

        # Load the QSS file
        with open("./src/views/login_screen.qss", "r") as f:
            self.setStyleSheet(f.read())

        # Create the layout
        layout = LoginLayout()
        self.setLayout(layout)

        # Add the login button to the layout
        self.login_button = LoginButton()
        layout.addWidget(self.login_button)

        # Connect the login button signal to the login signal
        self.login_button.clicked.connect(self.emit_login_signal)

    def get_username(self) -> str:
        return self.layout().username_field.text()

    def get_password(self) -> str:
        return self.layout().password_field.text()

    @Slot()
    def emit_login_signal(self):
        username = self.get_username()
        password = self.get_password()

        # Emit the login signal
        self.login_signal.emit(username, password)
