import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTextBrowser, QFrame, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QTreeView, QTreeWidgetItem, QTreeWidget
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QColor, QPainter, QStandardItemModel, QStandardItem


class MainWindow(QMainWindow):

    def sendMessage(self):
        output = self.agent.run(self.edit.text())
        #output = "Hello World!"

        self.message_index += 1

        #DEV
        history = self.agent.getHistory()
        #self.history.append("MESSAGGIO")
        #self.history.append(output)

        self.subLayout.itemAt(0).widget().setAlignment(Qt.AlignLeft)
        self.subLayout.itemAt(0).widget().append("[IO] - " + datetime.today().strftime("%y %m %d %H:%M:%S") + "\n" + history[-2] + "\n\r")
        self.message_index += 1
        self.subLayout.itemAt(0).widget().setAlignment(Qt.AlignRight)
        self.subLayout.itemAt(0).widget().append("[AGENT] - " + datetime.today().strftime("%y %m %d %H:%M:%S") + "\n" + history[-1] + "\n\r")

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

        self.button = QPushButton("Press Me!")
        self.edit.setFixedHeight(100)
        self.edit.setFixedWidth(600)
        self.edit.setTextMargins(10, 0, 0, 60)
        self.button.clicked.connect(self.sendMessage)


        self.mainWidget = QDialog()
        self.mainLayout = QHBoxLayout(self.mainWidget)

        self.subLayout = QVBoxLayout()
        self.subLayout.addWidget(self.top)

        self.subLayout.addWidget(self.edit)
        self.subLayout.addWidget(self.button)
        self.subLayout.setAlignment(Qt.AlignHCenter)


        #self.left = QVBoxLayout()
        #behaviourTree = QTreeWidget()
        #behaviourTree.setColumnCount(1)
        #item1 = QTreeWidgetItem("row %0 column %1")
        #behaviourTree. item1)
        #item2 = QTreeWidgetItem("row %0 column %1")
        #behaviourTree.setItem(1, item2)
        #item3 = QTreeWidgetItem("row %0 column %1")
        #behaviourTree.setItem(2, item3)
        #item4 = QTreeWidgetItem("row %0 column %1")
        #behaviourTree.setItem(3, item4)

        #treeView = QTreeView()
        #treeView.setModel(behaviourTree)

        #self.left.addWidget(treeView)
        #self.left.setAlignment(Qt.AlignTop)
        #self.mainLayout.addLayout(self.left)

        self.mainLayout.addLayout(self.subLayout)

        self.setCentralWidget(self.mainWidget)

