from PySide6.QtWidgets import QApplication, QWidget
from MainWindow import MainWindow
import sys
import os

def open_app():
    app = QApplication(sys.argv)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    style_path = os.path.join(current_dir, "style.qss")
    with open(style_path, "r") as file:
        style = file.read()

    window = MainWindow()
    window.setStyleSheet(style)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    open_app()