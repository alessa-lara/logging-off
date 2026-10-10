from typing import override
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from model.post import Post

from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt


class Post_Model(QAbstractListModel):
    __posts: list[Post]

    def __init__(self, posts: list[Post] | None) -> None:
        super().__init__()
        self.__posts = posts or []

    @override
    def rowCount(self, parent: QModelIndex | None = None) -> int:
        return len(self.__posts)

    @override
    def data(self, index: QModelIndex, role: int = 0) -> Post | None:
        if role == Qt.ItemDataRole.UserRole:
            return self.__posts[index.row()]

    def add(self, post: Post):
        posts_len = len(self.__posts)
        self.beginInsertRows(QModelIndex(), posts_len, posts_len)
        self.__posts.append(post)
        self.endInsertRows()

