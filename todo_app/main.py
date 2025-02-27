import sys
from PySide6.QtWidgets import QApplication, QWidget
from MainWindow import MainWindow

def open_app():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    open_app()