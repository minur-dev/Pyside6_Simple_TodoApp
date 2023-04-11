import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QLineEdit, QListWidget, QFrame)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setWindowTitle("Todo App")
        self.setGeometry(100, 100, 600, 400)

        # Create a central widget with a vertical layout
        central_widget = QWidget(self)
        central_layout = QVBoxLayout(central_widget)
        central_layout.setContentsMargins(20, 20, 20, 20)

        # Create a label for the app title
        title_label = QLabel("My Todo List")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 36px; font-weight: bold;")

        # Create a horizontal layout for the input field and add button
        input_layout = QHBoxLayout()
        input_layout.setSpacing(10)

        input_field = QLineEdit()
        input_field.setPlaceholderText("Add a task...")
        input_field.setStyleSheet("font-size: 20px; padding: 10px; border: 2px solid #ccc; border-radius: 5px;")
        input_layout.addWidget(input_field)

        add_button = QPushButton("Add")
        add_button.setStyleSheet("font-size: 20px; background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;")
        input_layout.addWidget(add_button)

        # Create a frame to group the input field and add button
        input_frame = QFrame()
        input_frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        input_frame.setLayout(input_layout)

        # Create a list widget for the tasks
        task_list = QListWidget()
        task_list.setStyleSheet("font-size: 20px;")

        # Add the title label, input frame, and task list to the central layout
        central_layout.addWidget(title_label)
        central_layout.addWidget(input_frame)
        central_layout.addWidget(task_list)

        # Connect the add button to a function that adds a new task to the list widget
        add_button.clicked.connect(lambda: self.add_task(input_field, task_list))

        # Set the central widget of the window
        self.setCentralWidget(central_widget)

    def add_task(self, input_field, task_list):
        task_name = input_field.text().strip()
        if task_name:
            task_list.addItem(task_name)
            input_field.clear()
            input_field.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
