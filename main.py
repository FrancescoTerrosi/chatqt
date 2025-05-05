from gui.gui import MainWindow
from src.aichat import ChatBot
import sys
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    mainWindow = MainWindow(agent = ChatBot())
    mainWindow.resize(800, 600)
    mainWindow.show()
    # Run the main Qt loop
    sys.exit(app.exec())

