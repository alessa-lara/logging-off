from PyQt6 import QtWidgets
from .ui.mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def get_tags(self):
        pass

    def get_post_text(self):
        pass

    def send(self):
        pass
