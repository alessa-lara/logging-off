from PyQt6.QtWidgets import QApplication

from delegate.post_delegate import Post_Delegate
from model.post import Post
from model.post_model import Post_Model
from view.mainwindow import MainWindow

DEBUG = True
if DEBUG:
    posts: list[Post] = [
            Post("2022-04-22", 2020, "Hello human", ["tag1", "tag2"], ["home/lara"])
        ]


def main():
    app = QApplication([])

    post_model = Post_Model(posts)
    post_delegate = Post_Delegate()
    main_window = MainWindow(post_model, post_delegate)

    main_window.show()
    _ = app.exec()

if __name__ == "__main__":
    main()
