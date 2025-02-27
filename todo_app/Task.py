from PySide6.QtWidgets import QFrame, QGridLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy

class Task(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(100)
        self.setStyleSheet("background-color: darkgreen")
        
        layout = QGridLayout()
        # layout.setSizeConstraint()

        self.timestamp = "2025-02-27   15:30"
        self.title = "Example Task"
        self.description = "Description of the task"

        self.timestamp_widget = QLabel(self.timestamp)
        self.title_widget = QLabel(self.title)
        self.description_widget = QLabel(self.description)
        
        self.show_button = QPushButton("Show More")
        self.show_button.setMinimumSize(100, 20)
        self.delete_button = QPushButton("Delete")
        self.delete_button.setMinimumSize(100, 20)

        layout.addWidget(self.timestamp_widget, 0, 0)
        layout.addWidget(self.title_widget, 1, 0)
        layout.addWidget(self.show_button, 2, 0)
        layout.addWidget(self.description_widget, 3, 0)
        spacer = QSpacerItem(200, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer, 0, 1)

        layout.addWidget(self.delete_button, 1, 2)


        self.setLayout(layout)


