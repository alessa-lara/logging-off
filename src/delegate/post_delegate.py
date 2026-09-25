from typing import override, TYPE_CHECKING

if TYPE_CHECKING:
    from model.post import Post

from PyQt6.QtCore import QModelIndex, QRect, QSize, Qt
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem

class Post_Delegate(QStyledItemDelegate):
    def __init__(self) -> None:
        super().__init__()
        self.sizeHint = lambda opt, idx: QSize(opt.rect.width() or 400, 120)

    @override
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        role: int = Qt.ItemDataRole.UserRole
        data: Post = index.data(role)

        pad = 10
        gap = 6
        tag_h = 22

        painter.save()

        fm = painter.fontMetrics()
        r = option.rect.adjusted(pad, pad, -pad, -pad)

        top = QRect(r.left(), r.top(), r.width(), fm.height())
        _ = painter.drawText(
                top,
                Qt.AlignmentFlag.AlignLeft  | Qt.AlignmentFlag.AlignVCenter,
                str(data.id)
            )
        _ = painter.drawText(
                top,
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
                data.date
            )

        text_rect = QRect(r.left(), top.bottom() + gap, r.width(), r.bottom() - tag_h - gap - top.bottom() - gap)
        _ = painter.drawText(
                text_rect,
                Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop | Qt.TextFlag.TextWordWrap,
                data.text 
            )

        x = r.left()
        y = r.bottom() - tag_h
        for tag in data.tags:
            w = fm.horizontalAdvance(tag) + 16
            tag_rect = QRect(x, y, w, tag_h)
            painter.setBrush(QColor("#e0e7ff"))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRect(tag_rect)
            painter.setPen(QColor("#3730a3"))
            _ = painter.drawText(tag_rect, Qt.AlignmentFlag.AlignCenter, tag)
            x += w + 6

        painter.setPen(QColor("black"))
        painter.drawLine(r.left(), r.bottom() + 16, r.right(), r.bottom() + 16)

        painter.restore()
