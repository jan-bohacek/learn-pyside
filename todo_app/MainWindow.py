from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QLineEdit, QTextEdit
from PySide6.QtCore import Qt
from Task import Task

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToDo App")
        self.setMinimumSize(800, 400)

        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        new_task_layout = QVBoxLayout()

        main_layout.addLayout(left_layout, 5)
        main_layout.addLayout(new_task_layout, 3)

        # task list
        self.task_1 = Task()
        self.task_2 = Task()
        # self.task_3 = Task()

        self.tasks_layout = QVBoxLayout()
        self.tasks_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.tasks_layout.addWidget(self.task_1)
        self.tasks_layout.addWidget(self.task_2)
        # self.tasks_layout.addWidget(self.task_3)

        self.task_scroll = QScrollArea()
        # self.task_scroll.setMinimumWidth(500)
        self.task_scroll.setLayout(self.tasks_layout)

        left_layout.addWidget(self.task_scroll)

        # create new task
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_new_task)

        self.new_task_widget = QWidget()

        self.new_task_title = QLineEdit()
        self.new_task_title.setText("Enter Title")

        self.new_task_description = QTextEdit()
        self.new_task_description.setText("Enter Description")

        self.new_task_timestamp = QLineEdit()
        
        # layout
        self.new_task_layout = QVBoxLayout()
        self.new_task_layout.addWidget(self.new_task_title)
        self.new_task_layout.addWidget(self.new_task_description)
        self.new_task_layout.addWidget(self.new_task_timestamp)
        self.new_task_widget.setLayout(self.new_task_layout)

        new_task_layout.addWidget(self.create_button)
        new_task_layout.addWidget(self.new_task_widget)

        self.setLayout(main_layout)

    def create_new_task(self):
        print("Creating task")
