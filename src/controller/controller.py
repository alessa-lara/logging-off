from datetime import UTC, datetime

from model.post import Post
from model.post_model import Post_Model


class Controller:
    model: Post_Model

    def __init__(self, model: Post_Model):
        self.model = model

    def process(self, user_text: str, user_tags: list[str], user_attachments: list[str]) -> None:
        tags = self._process_tags(user_tags)
        text = self._process_text(user_text)
        attachments = self._process_attachments(user_attachments)
        date = self._get_date()
        id = self._hash_data(text, date)

        post = Post(date, id, text, tags, attachments)

        self.model.add(post)

    def _process_tags(self, tags: list[str]) -> list[str]:
        for tag in tags:
            tag = tag.lower()

        return tags

    def _process_text(self, text: str) -> str:
        text = text.strip()

        return text

    def _process_attachments(self, attachments: list[str]) -> list[str]:
        return attachments

    def _get_date(self) -> str:
        date_info: datetime = datetime.now(UTC)
        date_iso: str = date_info.isoformat()

        return date_iso

    def _hash_data(self, text: str, date: str) -> int:
        concat = text.join(date)

        val = hash(concat)

        return val
