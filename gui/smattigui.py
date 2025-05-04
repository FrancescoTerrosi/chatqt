import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QToolButton, QLineEdit
from PySide6.QtCore import Slot

@Slot()
def clicked():
    print("Button Clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello Worldo!")
    button = QPushButton("Click me")
    button.clicked.connect(clicked)
    button.show()
    label.show()
    button2 = QToolButton()
    line_edit = QLineEdit()
    button.clicked.connect(line_edit.clear)
    button2.show()
    line_edit.show()
    app.exec()

