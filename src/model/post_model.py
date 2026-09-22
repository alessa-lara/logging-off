from typing import override
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from model.post import Post

from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt


class Post_Model(QAbstractListModel):
    _posts: list[Post]

    def __init__(self, posts: list[Post] | None) -> None:
        super().__init__()
        self._posts = posts or []

    @override
    def rowCount(self, parent: QModelIndex | None = None) -> int:
        return len(self._posts)

    @override
    def data(self, index: QModelIndex, role: int = 0) -> Post | None:
        if role == Qt.ItemDataRole.UserRole:
            return self._posts[index.row()]
