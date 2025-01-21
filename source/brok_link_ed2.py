import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QLabel, QWidget, QMessageBox
)
from PyQt5.QtGui import QTextCursor


class FileEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize UI components
        self.input_line = QLineEdit()
        self.text_edit = QTextEdit()
        self.save_button = QPushButton("Save")
        self.error_label = QLabel()

        # Set up layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Paste the Parent URL string here:"))
        layout.addWidget(self.input_line)
        layout.addWidget(self.error_label)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.save_button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect signals
        self.input_line.returnPressed.connect(self.load_file)
        self.save_button.clicked.connect(self.save_file)

        # State variables
        self.current_file_path = None

    def parse_input(self, input_string):
        """Parse the input string to extract file path and line number."""
        try:
            # Match the format of the input string
            parts = input_string.split(", ")
            # file_part = parts[0].split("file:///")[1].strip()
            # line_part = parts[1].split("line")[1].strip().split(",")[0]
            # parts = line.split(",")
            file_part = parts[0].strip().replace('Parent URL file:// ', '')
            file_part = file_part.replace(
                "Parent URL file:///mnt/c/Users/bergr/github/branches/11/wiki/source/_build/html/",
                "C:/Users/bergr/github/branches/11/wiki/source/")
            file_part = file_part.replace(".html", ".rst")
            line_part = parts[1].strip().replace('line ', '')

            return file_part, int(line_part)
        except (IndexError, ValueError):
            raise ValueError("Invalid input format. Expected format:\n"
                             "Parent URL file:///path/to/file, line X, col Y")

    def load_file(self):
        """Load the specified file and scroll to the specified line."""
        input_string = self.input_line.text()

        try:
            file_path, line_number = self.parse_input(input_string)
            self.current_file_path = file_path

            # Read the file content
            with open(file_path, "r") as file:
                content = file.read()
                self.text_edit.setText(content)

            # Scroll to the specified line
            cursor = self.text_edit.textCursor()
            cursor.movePosition(QTextCursor.Start)
            for _ in range(line_number - 1):  # Move cursor to the specified line
                cursor.movePosition(QTextCursor.Down)
            self.text_edit.setTextCursor(cursor)
            self.text_edit.setFocus()

            self.error_label.setText("")
        except Exception as e:
            self.error_label.setText(f"Error: {e}")
            self.current_file_path = None

    def save_file(self):
        """Save the current content of the text edit to the file."""
        if not self.current_file_path:
            QMessageBox.warning(self, "Error", "No file loaded to save.")
            return

        try:
            with open(self.current_file_path, "w") as file:
                file.write(self.text_edit.toPlainText())
            QMessageBox.information(self, "Success", f"File saved: {self.current_file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save file: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor_app = FileEditorApp()
    editor_app.resize(800, 600)
    editor_app.setWindowTitle("File Editor")
    editor_app.show()
    sys.exit(app.exec_())
