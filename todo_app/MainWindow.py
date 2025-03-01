from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, QLineEdit, QTextEdit, QSizePolicy, QFrame, QDateTimeEdit
from PySide6.QtCore import Qt, QDateTime
from task import Task


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
        # self.task_1 = Task()
        # self.task_2 = Task()
        # self.task_3 = Task()
        # self.task_4 = Task()
        # self.task_5 = Task()
        
        self.tasks_layout = QVBoxLayout()
        self.tasks_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        # self.tasks_layout.addWidget(self.task_1)
        # self.tasks_layout.addWidget(self.task_2)
        # self.tasks_layout.addWidget(self.task_3)
        # self.tasks_layout.addWidget(self.task_4)
        # self.tasks_layout.addWidget(self.task_5)

        # scrolling
        self.tasks_frame = QFrame(objectName="tasks_frame")
        self.tasks_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tasks_frame.setLayout(self.tasks_layout)
        self.tasks_scroll = QScrollArea()
        self.tasks_scroll.setWidgetResizable(True)
        self.tasks_scroll.setWidget(self.tasks_frame)

        left_layout.addWidget(self.tasks_scroll)

        ## CREATE NEW TASK
        self.create_task_button = QPushButton("Create", objectName="create_task_button")
        self.create_task_button.setMinimumHeight(30)
        self.create_task_button.clicked.connect(self.create_new_task)

        self.new_task_widget = QFrame(objectName="new_task_frame")

        self.new_task_title = QLineEdit()
        self.new_task_title.setPlaceholderText("Enter Title")

        self.new_task_description = QTextEdit()
        self.new_task_description.setPlaceholderText("Enter Description")

        self.new_task_timestamp = QDateTimeEdit()
        # self.new_task_timestamp.setText(QDateTime.currentDateTime().toString("yyyy-mm-dd hh:mm:ss"))
        self.new_task_timestamp.setMinimumDateTime(QDateTime.currentDateTime())
        
        # layout
        self.new_task_layout = QVBoxLayout()
        self.new_task_layout.addWidget(self.new_task_title)
        self.new_task_layout.addWidget(self.new_task_description)
        self.new_task_layout.addWidget(self.new_task_timestamp)
        self.new_task_widget.setLayout(self.new_task_layout)

        new_task_layout.addWidget(self.create_task_button)
        new_task_layout.addWidget(self.new_task_widget)

        self.setLayout(main_layout)

    def new_task_reset(self):
        self.new_task_title.setText("")
        self.new_task_description.setText("")
        self.new_task_timestamp.setMinimumDateTime(QDateTime.currentDateTime())

    def create_new_task(self):
        timestamp = self.new_task_timestamp.text()
        title = self.new_task_title.text()
        description = self.new_task_description.toPlainText()
        new_task = Task(timestamp, title, description)

        self.tasks_layout.addWidget(new_task)
        self.new_task_reset()
        
