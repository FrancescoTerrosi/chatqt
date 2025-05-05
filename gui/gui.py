import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTextBrowser, QFrame, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QTreeView, QTreeWidgetItem, QTreeWidget, QRadioButton
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QColor, QPainter, QStandardItemModel, QStandardItem


class MainWindow(QMainWindow):

    def sendMessage(self):
        self.message = self.edit.text()
        self.edit.clear()
        output = self.agent.run(self.message)
        #output = "Hello World!"

        self.message_index += 1

        #DEV
        history = self.agent.getHistory()
        #self.history.append("MESSAGGIO")
        #self.history.append(output)

        self.subLayout.itemAt(0).widget().setAlignment(Qt.AlignLeft)
        self.subLayout.itemAt(0).widget().append("[IO] - " + datetime.today().strftime("%y-%m-%d %H:%M:%S") + "\n" + history[-2] + "\n\r")
        self.message_index += 1
        self.subLayout.itemAt(0).widget().setAlignment(Qt.AlignRight)
        self.subLayout.itemAt(0).widget().append("[AGENT] - " + datetime.today().strftime("%y-%m-%d %H:%M:%S") + "\n" + history[-1] + "\n\r")

    def changePersonality(self):
        itemClicked = self.behaviourTree.currentItem()
        if itemClicked.text(0) == "CHEF GOURMET":
            self.agent.setPersonality(0)
        if itemClicked.text(0) == "STORICO PER BAMBINI":
            self.agent.setPersonality(1)
        if itemClicked.text(0) == "CONDUTTORE TV":
            self.agent.setPersonality(2)
        if itemClicked.text(0) == "GERRY SCOTTI":
            self.agent.setPersonality(3)

    def __init__(self, agent=None):
        super().__init__()
        self.agent = agent
        self.message_index = -1

        #DEV
        self.history = []

        self.top = QTextBrowser()

        self.top.setFrameShape(QFrame.Shape.Box)
        self.top.setFixedWidth(600)

        self.edit = QLineEdit()
        self.edit.setFixedHeight(200)
        self.edit.setFixedWidth(600)
        self.edit.returnPressed.connect(self.sendMessage)

        self.edit.setFixedHeight(100)
        self.edit.setFixedWidth(600)
        self.edit.setTextMargins(10, 0, 0, 60)

        self.button = QPushButton("Invia")
        self.button.clicked.connect(self.sendMessage)


        self.mainWidget = QDialog()
        self.mainLayout = QHBoxLayout(self.mainWidget)

        self.subLayout = QVBoxLayout()
        self.subLayout.addWidget(self.top)

        self.subLayout.addWidget(self.edit)
        self.subLayout.addWidget(self.button)
        self.subLayout.setAlignment(Qt.AlignHCenter)


        self.left = QVBoxLayout()
        self.behaviourTree = QTreeWidget()
        self.behaviourTree.setHeaderLabel("PARAMETRI")
        self.behaviourTree.setMaximumWidth(300)
        topHeader = QTreeWidgetItem(self.behaviourTree)
        topHeader.setText(0, "Personalità")
        item1 = QTreeWidgetItem(topHeader)
        item1.setText(0, "CHEF GOURMET")
        item2 = QTreeWidgetItem(topHeader)
        item2.setText(0, "STORICO PER BAMBINI")
        item3 = QTreeWidgetItem(topHeader)
        item3.setText(0, "CONDUTTORE TV")
        item4 = QTreeWidgetItem(topHeader)
        item4.setText(0, "GERRY SCOTTI")
        itemList = [item1, item2, item3, item4]
        self.behaviourTree.insertTopLevelItems(0, itemList)
        self.behaviourTree.itemClicked.connect(self.changePersonality)

        self.left.addWidget(self.behaviourTree)
        self.left.setAlignment(Qt.AlignTop)
        self.mainLayout.addLayout(self.left)

        self.mainLayout.addLayout(self.subLayout)

        self.setCentralWidget(self.mainWidget)

