import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from ui import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MarkCounter = QMainWindow()
    ui = Ui_MarksCounter()
    ui.setupUi(MarkCounter)
    MarkCounter.show()
    sys.exit(app.exec())
