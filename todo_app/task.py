from PySide6.QtWidgets import QFrame, QGridLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy

class Task(QFrame):
    def __init__(self, timestamp, title, description):
        super().__init__()
        
        layout = QGridLayout()

        self.timestamp = timestamp
        self.title = title
        self.description = description

        self.timestamp_widget = QLabel(self.timestamp)
        self.title_widget = QLabel(self.title)
        self.description_widget = QLabel(self.description)
        self.description_widget.setHidden(True)
        
        self.show_button = QPushButton("Show More", objectName="show_button")
        self.show_button.setMinimumSize(100, 20)
        self.show_button.clicked.connect(self.toggle_details)

        self.delete_button = QPushButton("Delete", objectName="delete_button")
        self.delete_button.setMinimumSize(100, 20)
        self.delete_button.clicked.connect(self.delete_task)

        layout.addWidget(self.timestamp_widget, 0, 0)
        layout.addWidget(self.title_widget, 1, 0)
        layout.addWidget(self.show_button, 2, 0)
        layout.addWidget(self.description_widget, 3, 0)
        spacer = QSpacerItem(200, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer, 0, 1)

        layout.addWidget(self.delete_button, 1, 2)


        self.setLayout(layout)

    def toggle_details(self):
        if self.description_widget.isHidden():
            self.show_button.setText("Show Less")
            self.description_widget.setHidden(False)
        else:
            self.show_button.setText("Show More")
            self.description_widget.setHidden(True)

    def delete_task(self):
        parent = self.parent()
        layout = parent.layout()
        layout.removeWidget(self)
        self.deleteLater()

