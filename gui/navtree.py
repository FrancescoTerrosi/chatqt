from PySide6.QtWidgets import QTreeWidgetItem, QTreeWidget

class NavTree(QTreeWidget):

    def __init__(self, maxWidth, labels):
        super().__init__()
        self.setHeaderLabel("PARAMETRI")
        self.setMaximumWidth(maxWidth)

        topHeader = QTreeWidgetItem(self)
        topHeader.setText(0, "Personalità")
        itemList = []

        for l in labels:
            item = QTreeWidgetItem(topHeader)
            item.setText(0, l)
            itemList.append(item)

        self.insertTopLevelItems(0, itemList)
        self.setCurrentItem(itemList[0])

