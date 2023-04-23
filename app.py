import sys
from PySide6.QtWidgets import QApplication, QWidget

from src.views import LoginScreen

def main ():
    app = QApplication(sys.argv)

    login_screen = LoginScreen()
    login_screen.login_signal.connect(lambda username, password: print(f"Username: {username}\nPassword: {password}"))
    login_screen.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()