import os
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow

ui_data = os.path.join(os.getcwd(), "resources/ui/app_window.ui")
ui_class = uic.loadUiType(ui_data)[0]


class MainApp:
    def __init__(self):
        self.__application = QApplication(sys.argv)
        self.__window = MainWindow()

    def show(self):
        self.__window.show()

    def exec(self):
        self.__application.exec()


class MainWindow(QMainWindow, ui_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
