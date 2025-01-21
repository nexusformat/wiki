import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox
)
from PyQt5.QtGui import QTextCursor


class LinkCheckerEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LinkChecker Editor")
        self.resize(800, 600)

        self.current_index = 0
        self.linkchecker_data = []

        # Main layout and central widget
        self.fname = QLabel()
        self.msg = QLabel()
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        # Widgets
        self.instructions = QLabel("Load a LinkChecker output file to begin.")
        self.text_edit = QTextEdit()
        self.next_button = QPushButton("Next")
        self.load_button = QPushButton("Load LinkChecker Output")

        # Configure widgets
        self.text_edit.setReadOnly(True)
        self.next_button.setEnabled(False)

        # Add widgets to layout
        self.layout.addWidget(self.instructions)
        self.layout.addWidget(self.fname)
        self.layout.addWidget(self.msg)
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.next_button)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Connect signals
        self.load_button.clicked.connect(self.load_linkchecker_output)
        self.next_button.clicked.connect(self.process_next_file)

    def load_linkchecker_output(self):
        # Open a file dialog to select the LinkChecker output file
        file_path, _ = QFileDialog.getOpenFileName(self, "Select LinkChecker Output File", "", "Text Files (*.txt)")
        if not file_path:
            return

        try:
            with open(file_path, "r") as file:
                self.parse_linkchecker_output(file.readlines())
            self.instructions.setText("Loaded LinkChecker output. Click 'Next' to begin editing.")
            self.next_button.setEnabled(True)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file: {e}")

    def parse_linkchecker_output(self, lines):

        self.linkchecker_data = []
        parent_url = None
        line_number = 0
        for line in lines:
            if line.startswith("Parent URL"):
                parts = line.split(",")
                parent_url = parts[0].strip().replace('Parent URL file:// ', '')
                parent_url = parent_url.replace("Parent URL file:///mnt/c/Users/bergr/github/branches/11/wiki/source/_build/html/","C:/Users/bergr/github/branches/11/wiki/source/")
                parent_url = parent_url.replace(".html",".rst")
                line_number = int(parts[1].strip().replace('line ', ''))

            if line.startswith("Result     Error: "):
                error = line
                self.linkchecker_data.append((parent_url, line_number, error))
                parent_url = None

    def process_next_file(self):
        if self.current_index >= len(self.linkchecker_data):
            QMessageBox.information(self, "Done", "All files have been processed.")
            self.next_button.setEnabled(False)
            return

        parent_url, line_number, error = self.linkchecker_data[self.current_index]
        self.fname.setText(parent_url)
        self.msg.setText(error)

        self.current_index += 1

        try:
            with open(parent_url, "r") as file:
                content = file.readlines()

            # Highlight the specified line
            self.text_edit.setPlainText("".join(content))
            cursor = self.text_edit.textCursor()
            cursor.movePosition(QTextCursor.Start)
            for _ in range(line_number - 1):
                cursor.movePosition(QTextCursor.Down)
            self.text_edit.setTextCursor(cursor)
            self.text_edit.ensureCursorVisible()
            self.text_edit.setReadOnly(False)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open file {parent_url}: {e}")
            self.process_next_file()  # Move to the next file

    def save_current_file(self, file_path):
        try:
            with open(file_path, "w") as file:
                file.write(self.text_edit.toPlainText())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save file {file_path}: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinkCheckerEditor()
    window.show()
    sys.exit(app.exec_())
