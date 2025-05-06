import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTextBrowser, QFrame, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QRadioButton
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QColor, QPainter, QStandardItemModel, QStandardItem
from gui.navtree import NavTree
from gui.centralpanel import CentralPanel

class MainWindow(QMainWindow):

    def sendMessage(self):
        message = self.centralPanel.getTextAndClearArea()
        self.agent.run(message)
        self.centralPanel.updateTextArea(self.agent.getHistory())

    def changePersonality(self):
        itemClicked = self.behaviourTree.currentItem()
        personalities = self.agent.getPersonalitiesLabels()
        for i in range(0, len(personalities)):
            if itemClicked.text(0) == personalities[i]:
                self.agent.setPersonality(i)

    def resetPersonality(self):
        self.agent.resetHistory()
        self.changePersonality()
        self.centralPanel.itemAt(0).widget().setAlignment(Qt.AlignCenter)
        self.centralPanel.itemAt(0).widget().append("### CAMBIO DI PERSONALITÀ IN " + self.behaviourTree.currentItem().text(0) + " ###\n\r")

    def __init__(self, agent=None):
        super().__init__()
        self.agent = agent

        #DEV
        self.history = []

        self.centralPanel = CentralPanel()
        self.centralPanel.registerResetSignal(self.resetPersonality)
        self.centralPanel.registerSendSignal(self.sendMessage)

        self.leftPanel = QVBoxLayout()
        self.behaviourTree = NavTree(300, self.agent.getPersonalitiesLabels())
        self.behaviourTree.itemClicked.connect(self.changePersonality)
        self.leftPanel.addWidget(self.behaviourTree)
        self.leftPanel.setAlignment(Qt.AlignTop)


        self.mainWidget = QWidget()
        self.mainLayout = QHBoxLayout(self.mainWidget)


        self.mainLayout.addLayout(self.leftPanel)

        self.mainLayout.addLayout(self.centralPanel)

        self.setCentralWidget(self.mainWidget)

