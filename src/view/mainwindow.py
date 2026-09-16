from PyQt6 import QtWidgets
from .ui.mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_send.clicked.connect(self.send)
        self.button_attach.clicked.connect(self.attach)

    # probably can do something like:
    # write a "," we create a button with the tag as a label and, when we click on the button, we can modify its text
    def get_tags(self) -> list[str]:
        tags_post: list[str] = self.input_tags.toPlainText().strip().split(",")
        return tags_post

    def get_post_text(self) -> str:
        post_text: str = self.input_post.toMarkdown()
        return post_text

    # the simplest way to attach a file to a post is saving the file location and then, later, showing the file
    # not the most interesting or permanent way... but it works
    def attach(self) -> str:
        dialog = QtWidgets.QFileDialog()
        file: tuple[str, str] = dialog.getOpenFileName(
            self,
            caption = "Select File",
            directory = "/home",
        )

        return file[0]

    def send(self) -> None:
        pass
