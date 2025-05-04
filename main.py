from gui.gui import Form
from src.aichat import ChatBot
import sys
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form(agent = ChatBot())
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())

