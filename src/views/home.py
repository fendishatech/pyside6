import sys
from PySide6.QtWidgets import QApplication, QWidget

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HHU Helper | Home")
        self.setGeometry(100, 100, 300, 200)
