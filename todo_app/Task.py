from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QLayoutItem

class Task(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(100)

        layout = QGridLayout()

        self.timestamp = "2025-02-27   15:30"
        self.title = "Example Task"
        self.description = "Description of the task"

        self.timestamp_widget = QLabel(self.timestamp)
        self.title_widget = QLabel(self.title)
        self.description_widget = QLabel(self.description)
        
        self.show_button = QPushButton("Show More")
        self.delete_button = QPushButton("Delete")

        layout.addWidget(self.timestamp_widget, 1, 1)
        layout.addWidget(self.title_widget, 2, 1)
        layout.addWidget(self.description_widget, 3, 1)

        self.setLayout(layout)


