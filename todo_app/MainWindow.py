from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QLineEdit, QTextEdit, QSizePolicy
from PySide6.QtCore import Qt, QDateTime
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

        # TASKS LIST
        self.task_1 = Task()
        self.task_2 = Task()
        self.task_3 = Task()
        self.task_4 = Task()
        self.task_5 = Task()
        
        self.tasks_layout = QVBoxLayout()
        self.tasks_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.tasks_layout.addWidget(self.task_1)
        self.tasks_layout.addWidget(self.task_2)
        self.tasks_layout.addWidget(self.task_3)
        self.tasks_layout.addWidget(self.task_4)
        self.tasks_layout.addWidget(self.task_5)

        # scrolling
        self.tasks_widget = QWidget()
        self.tasks_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tasks_widget.setLayout(self.tasks_layout)
        self.tasks_scroll = QScrollArea()
        self.tasks_scroll.setWidget(self.tasks_widget)

        left_layout.addWidget(self.tasks_scroll)

        ## CREATE NEW TASK
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_new_task)

        self.new_task_widget = QWidget()

        self.new_task_title = QLineEdit()
        self.new_task_title.setText("Enter Title")

        self.new_task_description = QTextEdit()
        self.new_task_description.setText("Enter Description")

        self.new_task_timestamp = QLineEdit()
        self.new_task_timestamp.setText(QDateTime.currentDateTime().toString("yyyy-mm-dd hh:mm:ss"))
        
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
