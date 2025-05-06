from datetime import datetime
from PySide6.QtWidgets import QFrame, QTextBrowser, QTextEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

class CentralPanel(QVBoxLayout):

    def __init__(self):
        super().__init__()
        self.topWidget = QTextBrowser()

        self.topWidget.setFrameShape(QFrame.Shape.Box)
        self.topWidget.setFixedWidth(600)

        self.editTextArea = QTextEdit()
        self.editTextArea.setFixedHeight(150)
        self.editTextArea.setFixedWidth(600)

        self.sendButton = QPushButton("Invia")
        self.resetButton = QPushButton("Reset Personalità")

        self.addWidget(self.topWidget)
        self.addWidget(self.editTextArea)
        self.addWidget(self.sendButton)
        self.addWidget(self.resetButton)
        self.setAlignment(Qt.AlignHCenter)

    def updateTextArea(self, history):
        self.itemAt(0).widget().setAlignment(Qt.AlignLeft)
        self.itemAt(0).widget().append("[IO] - " + datetime.today().strftime("%y-%m-%d %H:%M:%S") + "\n" + history[-2] + "\n\r")
        self.itemAt(0).widget().setAlignment(Qt.AlignRight)
        self.itemAt(0).widget().append("[AGENT] - " + datetime.today().strftime("%y-%m-%d %H:%M:%S") + "\n" + history[-1] + "\n\r")

    def registerResetSignal(self, handler):
        self.resetButton.clicked.connect(handler)

    def registerSendSignal(self, handler):
        self.sendButton.clicked.connect(handler)

    def getTextAndClearArea(self):
        message = self.editTextArea.toPlainText()
        self.editTextArea.clear()
        return message

