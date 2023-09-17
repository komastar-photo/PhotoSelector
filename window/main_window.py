import os
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QListView
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QPushButton

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
        self.directory_path_edit: QLineEdit
        self.directory_path_edit = None
        self.candidate_file_list: QListView
        self.candidate_file_list = None
        self.select_directory_button: QPushButton
        self.select_directory_button = None
        self.copy_button: QPushButton
        self.copy_button = None
        self.move_button: QPushButton
        self.move_button = None
        self.__selected_path: str
        self.__selected_path = ''

        self.setupUi(self)
        self.__bind()

    def __bind(self):
        self.select_directory_button.clicked.connect(self.__on_click_select)
        self.copy_button.clicked.connect(self.__on_click_copy)
        self.move_button.clicked.connect(self.__on_click_move)

    def __on_click_select(self):
        select_path = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.directory_path_edit.setText(select_path)
        self.__selected_path = select_path

    def __on_click_copy(self):
        pass

    def __on_click_move(self):
        pass
