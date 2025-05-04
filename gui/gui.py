import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog,
                                QTextEdit, QPushButton,
                                QVBoxLayout, QTableWidget,
                                QLabel,  QTableWidgetItem)
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QColor

class Form(QMainWindow):

    def greetings(self):
        output = self.agent.run(self.edit.toPlainText())

        self.message_index += 1
        history = self.agent.getHistory()
        label = QLabel(history[-2])
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignLeft)
        self.mainLayout.insertWidget(self.message_index, label)

        self.message_index += 1
        label = QLabel(history[-1])
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignRight)
        self.mainLayout.insertWidget(self.message_index, label)

    def __init__(self, parent=None, agent=None):
        super(Form, self).__init__(parent)
        self.agent = agent
        self.message_index = -1

        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.edit = QTextEdit("Write my name here..")
        self.button = QPushButton("Show Greetings")
        self.button.clicked.connect(self.greetings)

        self.mainLayout = QVBoxLayout()

        subLayout = QVBoxLayout()
        subLayout.addWidget(self.edit)
        subLayout.addWidget(self.button)

        subLayout.setContentsMargins(100, 0, 100, 0)

        self.mainLayout.addLayout(subLayout)

