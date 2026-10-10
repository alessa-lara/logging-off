from datetime import UTC, datetime

from model.post import Post
from model.post_model import Post_Model


class Controller:
    __model: Post_Model

    def __init__(self, model: Post_Model):
        self.__model = model

    def process(self, user_text: str, user_tags: list[str], user_attachments: list[str]) -> None:
        tags = self.__process_tags(user_tags)
        text = self.__process_text(user_text)
        attachments = self.__process_attachments(user_attachments)
        date = self.__get_date()
        id = self.__hash(text, date)

        post = Post(date, id, text, tags, attachments)

        self.__model.add(post)

    def __process_tags(self, tags: list[str]) -> list[str]:
        for tag in tags:
            tag = tag.lower()

        return tags

    def __process_text(self, text: str) -> str:
        text = text.strip()

        return text

    def __process_attachments(self, attachments: list[str]) -> list[str]:
        return attachments

    def __get_date(self) -> str:
        date_info: datetime = datetime.now(UTC)
        date_iso: str = date_info.isoformat()

        return date_iso

    def __hash(self, text: str, date: str) -> int:
        concat = text.join(date)

        val = hash(concat)

        return val
