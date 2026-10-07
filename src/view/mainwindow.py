from PyQt6 import QtWidgets

from delegate.post_delegate import Post_Delegate
from model.post_model import Post_Model
from .ui.mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, post_model: Post_Model, post_delegate: Post_Delegate):
        super().__init__()
        self.setupUi(self)

        _ = self.button_tag_add.clicked.connect(self.add_tag)
        _ = self.button_send.clicked.connect(self.send)
        _ = self.button_attach.clicked.connect(self.attach)

        self.list_posts.setModel(post_model)
        self.list_posts.setItemDelegate(post_delegate)

    def edit_tag(self, button: QtWidgets.QPushButton):
        layout = self.layout_frame_tags
        index: int = layout.indexOf(button)
        button.hide()

        line_edit = QtWidgets.QLineEdit(button.text())

        layout.insertWidget(index, line_edit)
        line_edit.grabKeyboard()
        _ = line_edit.editingFinished.connect(lambda: self.__edit_tag_connection(line_edit, button))


    def __edit_tag_connection(self, line_edit: QtWidgets.QLineEdit, button: QtWidgets.QPushButton):
        input: str = line_edit.text()
        button.setText(input)
        line_edit.deleteLater()

        button.show()

    def add_tag(self):
        layout = self.layout_frame_tags
        button_tag_add = self.button_tag_add

        button_tag_add.hide()

        line_edit = QtWidgets.QLineEdit()
        layout.insertWidget(1, line_edit)
        line_edit.grabKeyboard()
        _ = line_edit.editingFinished.connect(lambda: self.__add_tag_connection(line_edit))

    def __add_tag_connection(self, line_edit: QtWidgets.QLineEdit):
        text: str = line_edit.text()

        button = QtWidgets.QPushButton(text=text)
        _ = button.clicked.connect(lambda: self.edit_tag(button))
        self.layout_frame_tags.addWidget(button)
        line_edit.deleteLater()

        self.button_tag_add.show()

    def get_tags(self) -> list[str]:
        tags: list[str] = []

        for button in self.frame_tags.children():
            if isinstance(button, QtWidgets.QPushButton):
                tags.append(button.text())

        tags.remove("+")

        return tags

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
